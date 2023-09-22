from flask_restful import Resource
from flask import jsonify
from ratelimiter import limiter,limit
import json

#API route

class APIExotics(Resource):

    #api limiter
    decorators = [limiter.limit(limit)]

    def getData(self):
        file = open("/home/ubuntu/XurTracker/data/data.json","r")
        data = json.load(file)
        file.close()
        
        self.exoticWeapon = data["Exotics"]["Exotic Weapon"]
        self.exoticHawkmoon = data["Exotics"]["Hawkmoon"],
        self.exoticTitan = data["Exotics"]["Titan Exotic"],
        self.exoticHunter = data["Exotics"]["Hunter Exotic"],
        self.exoticWarlock = data["Exotics"]["Warlock Exotic"],
        self.exoticEngram = data["Exotics"]["Exotic Engram"],
        self.exoticQuest = data["Exotics"]["Exotic Quest"],
    def get(self):
        self.getData()
        return jsonify(
            Weapon=self.exoticWeapon,
            Hawkmoon=self.exoticHawkmoon,
            TitanArmor=self.exoticTitan,
            HunterArmor=self.exoticHunter,
            WarlockArmor=self.exoticWarlock,
            Engram=self.exoticEngram,
            Quest=self.exoticQuest,
        )
    