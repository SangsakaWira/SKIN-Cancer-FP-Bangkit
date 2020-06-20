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
CORS(app)
 
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
           
            
        return jsonify({'result':predicted[0],'msg':'success'})
    except ValueError:
        return jsonify({'result':"Data anda bukan gambar!",'msg':'not success'})
    except AttributeError:
        return jsonify({'result':"Server is Down!"})

app.run(host='0.0.0.0',port=3500)