from flask import Flask,jsonify
from flask_cors import CORS,cross_origin
from flask import request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

predicted = np.array([0., 0., 0., 1.])
print(predicted)
index = predicted.index(1.)
print(index)