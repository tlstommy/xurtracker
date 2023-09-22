from flask_restful import Resource,reqparse
from flask import jsonify
from ratelimiter import limiter,limit
import json

#API route

class APIArmor(Resource):

    #api limiter
    decorators = [limiter.limit(limit)]

    

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('class', type=str, help='armor user class.')
        self.args = self.parser.parse_args(strict=True)
    def getArmor(self,_class):
        file = open("/home/ubuntu/XurTracker/data/data.json","r")
        data = json.load(file)
        file.close()
        
        #titan
        if(_class == 0):
            return jsonify(
                ExoticArmor=data["Exotics"]["Titan Exotic"],
                Helmet=data["Legendaries"]["Titan"]["Helmet"],
                Arms=data["Legendaries"]["Titan"]["Arms"],
                Chest=data["Legendaries"]["Titan"]["Chest"],
                Legs=data["Legendaries"]["Titan"]["Legs"],
                ClassItem=data["Legendaries"]["Titan"]["Class Item"],
            )
        #hunter
        elif(_class == 1):
            return jsonify(
                ExoticArmor=data["Exotics"]["Hunter Exotic"],
                Helmet=data["Legendaries"]["Hunter"]["Helmet"],
                Arms=data["Legendaries"]["Hunter"]["Arms"],
                Chest=data["Legendaries"]["Hunter"]["Chest"],
                Legs=data["Legendaries"]["Hunter"]["Legs"],
                ClassItem=data["Legendaries"]["Hunter"]["Class Item"],
            )
        #warlock
        elif(_class == 2):
            return jsonify(
                ExoticArmor=data["Exotics"]["Warlock Exotic"],
                Helmet=data["Legendaries"]["Warlock"]["Helmet"],
                Arms=data["Legendaries"]["Warlock"]["Arms"],
                Chest=data["Legendaries"]["Warlock"]["Chest"],
                Legs=data["Legendaries"]["Warlock"]["Legs"],
                ClassItem=data["Legendaries"]["Warlock"]["Class Item"],
            )
        
    def get(self):
        self.arg = str(self.args.get("class"))

        if(self.arg == 'titan'):
            return self.getArmor(0)
        elif(self.arg == 'hunter'):
            return self.getArmor(1)
        elif(self.arg == 'warlock'):
            return self.getArmor(2)
        else:
            #error
            return {'Error': "Invalid Arguments!"}
    