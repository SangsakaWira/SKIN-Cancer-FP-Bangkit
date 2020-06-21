# Load package for inference and flask library
import tensorflow as tf
import numpy as np
import pandas as pd
import os
import json 
from tensorflow.keras.models import load_model
from flask import Flask,jsonify
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask_cors import CORS,cross_origin
from flask import request
from numpy import loadtxt
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

UPLOAD_FOLDER = "uploads"
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
 
# load model
model = load_model('model_fp_72.h5')
 
# load and prepare the image
def load_image(filename):
	# load the image
	img = load_img(filename, target_size=(150, 150))
	# convert to array
	img = img_to_array(img)
	# reshape into a single sample with 3 channels
	img = img.reshape(1, 150, 150, 3)
	# center pixel data
	img = img.astype('float32')
	img = img - [123.68, 116.779, 103.939]
	return img

# allow file
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# load and return class
def load_predict(predicted):
    print("this one: "+str(predicted))
    print("this one 1.0: "+str(predicted[5]))
    print(type(predicted))
    predicted = np.array(predicted).tolist()
    class_index = predicted.index(1.)
    print(class_index)
    classes = ["Melanocytic Nevi","Melanoma","Benign Keratosis-like Lesions","Basal Cell Carcinoma","Actinic Keratoses","Vascular Lesions","Dermatofibroma","Squamous Cell Carcinoma"]
    result = classes[class_index]
    return result

@app.route("/predict")
def predict():
    return jsonify({'result':result[0]})

@app.route("/test")
def test():
    return jsonify({'result':'online'})

@app.route("/predict_post",methods=["POST"])
def predict_post():
    request_data = request.get_json()
    
    print("Type: "+str(type(request_data)))
    print("JSON: "+str(request_data))
    try:
        if request.method == 'POST':
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            # if user does not select file, browser also
            # submit a empty part without filename
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                image_path = "./uploads/"+filename
                image = load_image(image_path)
                predicted = model.predict(image)
                hasil = load_predict(predicted[0])
                return jsonify({'result':str(hasil),'msg':'success'})

        return jsonify({'result':predicted[0],'msg':'success'})
    except ValueError:
        return jsonify({'result':"Data anda bukan gambar!",'msg':'not success'})
    except AttributeError:
        return jsonify({'result':"Server is Down!"})

app.run(host='0.0.0.0',port=3500)