#Importing libraries we need to run the model 
from flask import Flask, request
# from PIL import Image 
# import numpy as np
# from skimage import transform 
# import tensorflow as tf
# import os

# abspath = os.path.abspath(__file__)
# dname = os.path.dirname(abspath)
# os.chdir(dname)

#Created a flask application with the name (__name__)
application = Flask(__name__)

# class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
#                'dog', 'frog', 'horse', 'ship', 'truck']
# #loads saved CNN model and had the class names on here to help with labeling the prediction

#Creating a route for the website 
@application.route("/")
def home():
    return "IDS 594 Project"

#Post to use for sending something to the website 
#Also had to upload image and transform it to match dimensions for the CNN
# @application.route("/pred/", methods=["POST"])
# def pred():
#     model = tf.keras.models.load_model('Models/my_save_model.h5')
#     file = request.files['image']
#     image = Image.open(file.stream)
#     image = np.array(image).astype('float32')/255
#     image = transform.resize(image, (32, 32, 3))
#     image = np.expand_dims(image, axis=0)
#     #Predicting and getting class label 
#     predict = model.predict(image)
#     label = predict.argmax(axis=-1)
#     class_name = class_names[label[0]]
#     return class_name

#launches when you run the program 
if __name__ == '__main__':
    application.run()