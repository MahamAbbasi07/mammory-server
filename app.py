from flask import Flask, jsonify, request, make_response
from flask_restful import Api, Resource
from threading import Thread
import json
import base64
from PIL import Image
import io
# from gunicorn import glogging
import os

# code for endpoints
from mammo_detect import Mammogram
from ultrasound_detect import Ultrasound

from get_hospitals import Hospitals
from get_reports import Reports

app = Flask(__name__)
api = Api(app)

# API Endpoints
#For mammogram Model
api.add_resource(Mammogram, '/api/mammogram', methods=['POST'])

#For ultrasound Model
api.add_resource(Ultrasound, '/api/ultrasound',methods= ['POST'])

#
api.add_resource(Hospitals, '/api/gethospitals', methods=['GET'])
api.add_resource(Reports, '/api/getreports', methods=['GET'])

if __name__ == '__main__':
    # run app with os environment host and port
    host = os.environ.get('HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port, threaded = True)