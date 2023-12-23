from flask_restful import Resource,reqparse
from flask import jsonify
from ratelimiter import limiter,limit
import json

#API route

class APIData(Resource):

    #api limiter
    decorators = [limiter.limit(limit)]

    

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('class', type=str, help='armor user class.')
        self.args = self.parser.parse_args(strict=True)
    
        

        
    def get(self):
        file = open("/home/ubuntu/XurTracker/data/data.json","r")
        data = json.load(file)
        file.close()
        

        return jsonify(data)
    