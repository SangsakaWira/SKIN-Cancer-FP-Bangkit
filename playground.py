from flask import Flask,jsonify
from flask_cors import CORS,cross_origin
from flask import request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Model(Resource):
    def get(self,image):
        return {'result':image}

api.add_resource(Model,"/model/<string:image>")

app.run(port=5000)