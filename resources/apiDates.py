from flask_restful import Resource
from datetime import date,timedelta
from flask import jsonify
from ratelimiter import limiter,limit

#API route

class APIDates(Resource):
    
    #api limiter
    decorators = [limiter.limit(limit)]

    def calculateReturn(self):
        returnDate = str(date.today() + timedelta((1-date.today().weekday()) % 3 ))
        return returnDate
    def calculateDepart(self):
        departDate = str(date.today() + timedelta((1-date.today().weekday()) % 7 ))
        return departDate
    
    def get(self):
        return jsonify(
            ReturnDate=self.calculateReturn(),
            DepartureDate=self.calculateDepart()
        )
    