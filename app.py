#server for flask
#Thomas Logan Smith

from flask import Flask, render_template, send_from_directory, request
from flask_restful import Resource, Api

import datetime
from datetime import date
import json 

#api endpoint resources
from resources.apiPrediction import APIPrediction
from resources.apiExoticWeapons import APIExoticWeapons
from resources.apiLocation import APILocation
from resources.apiDates import APIDates
from resources.apiData import APIData
from resources.apiArmor import APIArmor
from resources.apiLegendaryWeapons import APILegendaryWeapons
from resources.apiExotics import APIExotics
from ratelimiter import limiter

#reset hour
D2_RESET_TIME_UTC = 17

app = Flask(__name__)
api = Api(app)
app.config['TEMPLATES_AUTO_RELOAD'] = True



#init api rate limiter
limiter.init_app(app)

#api routes

#since tfs no longer needed
#api.add_resource(APIPrediction, '/api/prediction-data')

api.add_resource(APIData, '/api/get-data')
#api.add_resource(APIExotics, '/api/get-exotics')

# api/get-armor?class=titan
api.add_resource(APIArmor, '/api/get-armor')
api.add_resource(APILocation, '/api/get-location')
api.add_resource(APIDates, '/api/get-dates')
#api.add_resource(APIExoticWeapons, '/api/get-exotic-weapons')
api.add_resource(APILegendaryWeapons, '/api/get-legendary-weapons')




@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


if __name__ == '__main__':
   app.run(ssl_context=('/home/ubuntu/XurTracker/data/cert.pem', '/home/ubuntu/XurTracker/data/key.pem'),static_folder='static')
   