from flask import Flask,render_template,redirect,request

import gan

#__name__ == __main__ 
app = Flask(__name__)
@app.route('/')
def hello():
   return render_template("index.html")
@app.route('/home')
def home():
    return redirect('/')
@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/submit',methods=['POST'])
def submit_data():
    if request.method=='POST':
       path="./static/{}"
       path2="/static/{}"
       path3="/static1/{}"
       images =request.files["userfile"]
       images.save(path.format(images.filename))
       generated=gan.load(path.format(images.filename))
       out=gan.output(generated)
       gan.save(out,path.format("gen"+images.filename))

       return render_template("index.html",your_image=path2.format("gen"+images.filename))

if __name__=='__main__':
    app.run(debug=True)