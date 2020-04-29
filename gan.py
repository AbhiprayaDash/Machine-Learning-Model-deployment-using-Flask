import tensorflow as tf
from keras.models import load_model
from PIL import Image
import numpy as np
import cv2

def load(filename):
   np_image = Image.open(filename)
   np_image = np.array(np_image).astype('float32')/255
   np_image = cv2.resize(np_image, (256, 256))
   np_image = np.expand_dims(np_image, axis=0)
   return np_image


def output(image):
    model = load_model('models1/model_010000.h5')
    model._make_predict_function()
    images=model.predict(image)
    return images

def save(images,path):
   im = Image.fromarray(images[0],'RGB')
   im.save(path,subsampling=0,quality=100)