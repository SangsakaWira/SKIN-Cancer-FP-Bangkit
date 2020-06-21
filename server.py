# Load package for inference and flask library
import tensorflow as tf
from tensorflow.keras.models import load_model
from flask import Flask,jsonify
import numpy as np
import pandas as pd
from flask_cors import CORS,cross_origin
from flask import request
from numpy import loadtxt
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import json 

UPLOAD_FOLDER = "uploads"
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)

UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
 
# load model
model = load_model('model_fp_59.h5')
 
# load and prepare the image
def load_image(filename):
	# load the image
	img = load_img(filename, target_size=(128, 128))
	# convert to array
	img = img_to_array(img)
	# reshape into a single sample with 3 channels
	img = img.reshape(1, 128, 128, 3)
	# center pixel data
	img = img.astype('float32')
	img = img - [123.68, 116.779, 103.939]
	return img

# load and return class
def load_predict(predicted):
    index = predicted.index(1)
    classes = ["Melanocytic Nevi","Melanoma","Benign Keratosis-like Lesions","Basal Cell Carcinoma","Actinic Keratoses","Vascular Lesions","Dermatofibroma","Squamous Cell Carcinoma"]
    result = classes[index]
    return result

@app.route("/predict")
def predict():
    return jsonify({'result':result[0]})

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
                image = load_image("uploads/"+filename)
                model.predict(image)

            
        return jsonify({'result':predicted[0],'msg':'success'})
    except ValueError:
        return jsonify({'result':"Data anda bukan gambar!",'msg':'not success'})
    except AttributeError:
        return jsonify({'result':"Server is Down!"})

app.run(host='0.0.0.0',port=3500)