from flask_restful import Resource
from flask import jsonify
from ratelimiter import limiter,limit
import json

#API route

class APILegendaryWeapons(Resource):
    #api limiter
    decorators = [limiter.limit(limit)]

    def getData(self):
        file = open("/home/ubuntu/XurTracker/data/data.json","r")
        data = json.load(file)
        file.close()
        self.weapon0 = data["Legendaries"]["Legendary weapons"][0]
        self.weapon1 = data["Legendaries"]["Legendary weapons"][1]
        self.weapon2 = data["Legendaries"]["Legendary weapons"][2]
        self.weapon3 = data["Legendaries"]["Legendary weapons"][3]
        self.weapon4 = data["Legendaries"]["Legendary weapons"][4]
        self.weapon5 = data["Legendaries"]["Legendary weapons"][5]
        self.weapon6 = data["Legendaries"]["Legendary weapons"][6]
        
    def get(self):
        self.getData()
        return jsonify(
            Weapon0=self.weapon0,
            Weapon1=self.weapon1,
            Weapon2=self.weapon2,
            Weapon3=self.weapon3,
            Weapon4=self.weapon4,
            Weapon5=self.weapon5,
            Weapon6=self.weapon6
        )
    
    