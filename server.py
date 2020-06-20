# Load package for inference and flask library
from numpy import loadtxt
from keras.models import load_model
from flask import Flask,jsonify
import numpy as np
import pandas as pd
from flask_cors import CORS,cross_origin
from flask import request
import json 

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)

UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
 
# load model
model = load_model('model_fp59.h5')

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
            
        return jsonify({'result':predicted[0],'msg':'success'})
    except ValueError:
        return jsonify({'result':"Data anda bukan gambar!",'msg':'not success'})
    except AttributeError:
        return jsonify({'result':"Server is Down!"})

app.run(host='0.0.0.0',port=3500)