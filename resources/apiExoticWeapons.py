from flask_restful import Resource
from flask import jsonify
from ratelimiter import limiter,limit
import json

#API route

class APIExoticWeapons(Resource):

    #api limiter
    decorators = [limiter.limit(limit)]

    def getData(self):
        file = open("/home/ubuntu/XurTracker/data/data.json","r")
        data = json.load(file)
        file.close()
        self.exoticWeapon = data["Exotics"]["Exotic Weapon"]
        self.exoticHawkmoon = data["Exotics"]["Hawkmoon"],
    def get(self):
        self.getData()
        return jsonify(
            ExoticWeapon=self.exoticWeapon,
            ExoticHawkmoon=self.exoticHawkmoon
        )
    