from flask_restful import Resource
import json
from flask import jsonify
from ratelimiter import limiter,limit

#API route

class APILocation(Resource):

    #api limiter
    decorators = [limiter.limit(limit)]

    def getData(self):
        file = open("/home/ubuntu/XurTracker/data/data.json","r")
        data = json.load(file)
        file.close()
        self.location = data["Location"]
        self.planet = data["Planet"]
        self.lz = data["Landing Zone"]
    def get(self):
        self.getData()
        return jsonify(
            Location=self.location,
            Planet=self.planet,
            LandingZone=self.lz,
        )
    