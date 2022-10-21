#server for flask
#Thomas Logan Smith

from flask import Flask, render_template
import datetime
from datetime import date
import json 

#reset hour
D2_RESET_TIME_UTC = 17

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True



@app.route('/exotics')
def exotics():
   return render_template('exotic_items.html')

@app.route('/status')
def xurStatus():
   return render_template('xur_gone.html')

@app.route('/searching')
def xurSearch():
   return render_template('xur_search.html')


@app.route('/legendary-weapons')
def legendaryWeapons():
   return render_template('legendary_weapons.html')
   
@app.route('/warlock')
def legendaryArmorWarlock():
   return render_template('warlock_armor.html')

@app.route('/titan')
def legendaryArmorTitan():
   return render_template('titan_armor.html')

@app.route('/hunter')
def legendaryArmorHunter():
   return render_template('hunter_armor.html')

@app.route('/all')
def home():
   return render_template('all_items.html')

@app.route('/')
def main():
   today = date.today()
   currentUTCTime = datetime.datetime.utcnow().time().strftime("%H")
   print(currentUTCTime)
   print("TD:",today.weekday())
   if(today.weekday() <= 1 or today.weekday() >= 4):
      #do time checks
      if(today.weekday() == 4):
         if int(currentUTCTime) >= D2_RESET_TIME_UTC:
            #update check
            currentTime = str(today.strftime("%B %d, %Y"))
            with open('/home/ubuntu/XurTracker/data/data.json', 'r') as f:
               data = json.load(f)
               if(currentTime == data["Week"]):
                  #updated so return to all items
                  return render_template('all_items.html') 
            return xurSearch()
         else:
            return xurStatus()
      if(today.weekday() == 1):
         if int(currentUTCTime) < D2_RESET_TIME_UTC: 
            return render_template('all_items.html')
         else:
            return xurStatus()
      return render_template('all_items.html')
   else:
      return xurStatus()
   #return render_template('xur_gone.html')
if __name__ == '__main__':
   app.run(ssl_context=('/home/ubuntu/XurTracker/data/cert.pem', '/home/ubuntu/XurTracker/data/key.pem'))
   