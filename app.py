from flask import Flask,render_template,redirect,request

#__name__ == __main__ 
app = Flask(__name__)

friends=["prateek","sohail","narang"]

@app.route('/')
def hello():
   return render_template("index.html",myfriends=friends)
@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/home')
def home():
    return redirect('/')
@app.route('/submit',methods=['POST'])
def submit_data():
    if request.method=='POST':
       name=request.form['username']

       f = request.files['userfile']
       f.save(f.filename)
    return "<h1> Hello {}".format(name)

if __name__=='__main__':
    app.run(debug=True)