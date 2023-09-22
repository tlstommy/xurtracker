from flask_restful import Resource
from datetime import date
from flask import jsonify
from ratelimiter import limiter,limit
import json
from datetime import date, timedelta


#API route for data for prediction system

class APIPrediction(Resource):

    #api limiter
    decorators = [limiter.limit(limit)]

    def getWeeksSince(self,startDate):
        
        days = date.today() - startDate

        weeks = days.days // 7
        
        return weeks-1
        
    def getID(self):

        file = open("/home/ubuntu/XurTracker/data/data.json","r")
        data = json.load(file)
        file.close()
        self.location = data["Location"]

        if self.location == "The Last City":
            return 0
        elif self.location == "Winding Cove":
            return 1
        else:
            return 2
        
    
    def get(self):
        return jsonify(
            week=str(self.getWeeksSince(date(2020,11,13))),
            id=self.getID(),
            date=str(date.today())

        )
