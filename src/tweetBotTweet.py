import pydest,asyncio,aiohttp,json,requests,tweepy,random
import time
from datetime import date,timedelta
from credentials import * 

SEND_TWEET = False

class main:
    def __init__(self, apiKey):
        self.headerParameters = { "X-API-Key": API_KEY, "Authorization": f"Bearer {ACCESS_TOKEN}" }
        self.destiny = pydest.Pydest(apiKey)
        self.DestinyURLBase = "https://www.bungie.net/Platform"
        self.apiKey = apiKey
        self.apiResponseJson = None
        self.forSaleItems = None
        self.hashList = []
        self.hashIDList = []
        self.artificePresent = False
        self.exoticCatalysts = []
        self.exoticWarlock = None
        self.exoticTitan = None
        self.exoticHunter = None
        self.exoticWarlockTotalStat = None
        self.exoticTitanTotalStat = None
        self.exoticHunterTotalStat = None
        self.location = None
        self.week = str(date.today().strftime("%B %d"))
        self.dataJson = {}
        self.membershipType = destinyMembershipType
        self.membershipId = destinyMembershipID
        self.characterIDWarlock = characterIDWarlock
    
    async def tweet(self,sendTweet):
        

        #none checks
        if self.exoticTitan == None:
            print("rerunning tweet func..")
            await self.getXurInventory()
        if self.exoticWarlock == None:
            print("rerunning tweet func..")
            await self.getXurInventory()
        if self.exoticHunter== None:
            print("rerunning tweet func..")
            await self.getXurInventory()
        if len(self.exoticCatalysts) != 2:
            print("rerunning tweet func..")
            await self.getXurInventory()

        #setup twitter auth for v2 and v1 endpoints
        
        client = tweepy.Client(
            consumer_key=consumer_key, consumer_secret=consumer_secret,
            access_token=access_token, access_token_secret=access_token_secret
        )

        authV1 = tweepy.OAuth1UserHandler(
            consumer_key=consumer_key, consumer_secret=consumer_secret,
            access_token=access_token, access_token_secret=access_token_secret
        )
        clientV1 = tweepy.API(authV1)

       
        #update profile statuses
        
        clientV1.update_profile(location="The Last City")
        clientV1.update_profile_banner(filename="/home/ubuntu/XurTracker/imgs/xur-tower.jpg") 
        
        

        #calculate reset date    
        resetDate = date.today() + timedelta((1-date.today().weekday()) % 7 )
        resetDate = resetDate.strftime("%B %d").replace(' 0', ' ')
        resetDateOrdinaled = self.addOrdinal(resetDate) 
        tweetStr = f"🌎  Xûr has arrived at the Tower!\n\n\n💠  {self.exoticCatalysts[0]}\n💠  {self.exoticCatalysts[1]}\n🛡  {self.exoticTitan}\n🛡  {self.exoticHunter}\n🛡  {self.exoticWarlock}\n\n\n\n🚀  Xûr will depart on {resetDateOrdinaled}.\n\nMore info at: https://xurtracker.com\n\n#Xur #Destiny  #Destiny2"

        #tweet
        if(sendTweet):
            client.create_tweet(text=str(tweetStr))
        else:
            print("tweet:\n\n",tweetStr,"\n")
            print("sendTweet bool is set to false.")

    def combineStats(self,itemId,jsonObj):
        statTotal = 0
        statTotal += int(jsonObj["Response"]["itemComponents"]["stats"]["data"][str(itemId)]["stats"]["144602215"]["value"])
        statTotal += int(jsonObj["Response"]["itemComponents"]["stats"]["data"][str(itemId)]["stats"]["392767087"]["value"])
        statTotal += int(jsonObj["Response"]["itemComponents"]["stats"]["data"][str(itemId)]["stats"]["1735777505"]["value"])
        statTotal += int(jsonObj["Response"]["itemComponents"]["stats"]["data"][str(itemId)]["stats"]["1943323491"]["value"])
        statTotal += int(jsonObj["Response"]["itemComponents"]["stats"]["data"][str(itemId)]["stats"]["2996146975"]["value"])
        statTotal += int(jsonObj["Response"]["itemComponents"]["stats"]["data"][str(itemId)]["stats"]["4244567218"]["value"])
        return statTotal

    def getArmorStats(self,itemId):
        apiUrl304 = self.DestinyURLBase + f"/Destiny2/{self.membershipType}/Profile/{self.membershipId}/Character/{characterIDWarlock}/Vendors/2190858386/?components=304"
        apiResponse304 = self.get_api_request(apiUrl304)
        apiResponse304Json = json.loads(apiResponse304)
        return self.combineStats(itemId,apiResponse304Json)
      

    #Make a GET request to api and return json
    def get_api_request(self, url):
        try:
                #get api request and parse to json
                res = requests.get(url, headers=self.headerParameters)
                jsonResponse = json.dumps(res.json(), sort_keys=True, indent=4)
        except aiohttp.client_exceptions.ClientResponseError as e:
            print("ERROR: Could not connect to Bungie.net Endpoint\n",e)
        return jsonResponse
    
    #create a json file from all of the collected data
    def buildJSON(self):
        JSONTemplate = {
            "Location":self.location,
            "Week":self.week,
            "Exotic Weapon":self.exoticWeapon,
            "Warlock Exotic":self.exoticWarlock,
            "Hunter Exotic":self.exoticHunter,
            "Titan Exotic":self.exoticTitan,
            }
        self.dataJson = JSONTemplate

    #decode the hash from the manifest
    async def decodeHash(self,hash,manifestValue):
        hashedData = await self.destiny.decode_hash(hash,manifestValue)
        return hashedData

    #run through the hash list and format each hash and pull out its data
    async def parseHash(self):
        jsonObj = []
        for i in range(len(self.hashList)):
            decodedObj = await self.decodeHash(self.hashList[i],"DestinyInventoryItemDefinition")
            
            #if item is exotic
            if decodedObj["inventory"]["tierType"] == 6:
                
                name = decodedObj["displayProperties"]["name"]
                itemClass = decodedObj["classType"]
                
                
                #print(decodedObj["traitIds"][0])
                

                #warlock
                if(itemClass == 2):
                    self.exoticWarlock = name
                    
                #titan
                elif(itemClass == 0):
                    self.exoticTitan = name
                    
                #hunter
                elif(itemClass == 1):
                    self.exoticHunter = name
                    
                #catalyst
                else:
                    if len(self.exoticCatalysts) > 2:
                        break
                    
                    if decodedObj["traitIds"][0] == "item.exotic_catalyst":
                        self.exoticCatalysts.append(name)
                

    #get data from api
    def get_api_request(self, url):
        try:
                #get api request and store into a json format
                res = requests.get(url, headers=self.headerParameters)
                jsonResponse = json.dumps(res.json(), sort_keys=True, indent=4)
        except aiohttp.client_exceptions.ClientResponseError as e:
            print("ERROR: Could not connect to Bungie.net Endpoint\n",e)

        return jsonResponse

    #add endings like st or th to the date
    def addOrdinal(self,date):
        rawDate = int(date.split(" ")[1])
        rawDateOnes = rawDate % 10
        #deal with most of the th endings first
        if rawDate <= 20 and rawDate > 3:
            suffix = "th"
        elif rawDateOnes == 1:
            suffix = "st"
        elif rawDateOnes == 2:
            suffix = "nd"
        elif rawDateOnes == 3:
            suffix = "rd"
        else:
            suffix = "th"
        
        return date+suffix

    async def getXurInventory(self):
        
        unwanted_hashes = {2125848607,1092685591,4257549985,353704689,903043774}
        
        self.location = "Tower"

        #format url data    
        apiUrl = self.DestinyURLBase + "/Destiny2/Vendors/?components=402"
        self.apiResponse = self.get_api_request(apiUrl)
        
        #store the inventory of for sale items to be parsed 
        self.apiResponseJson = json.loads(self.apiResponse)
        self.forSaleItems = self.apiResponseJson["Response"]["sales"]["data"][list(self.apiResponseJson["Response"]["sales"]["data"].keys())[0]]["saleItems"]
        
        #add each hash and id to hashlists
        for i in range(len(self.forSaleItems)):
            self.hashList.append(self.apiResponseJson["Response"]["sales"]["data"][list(self.apiResponseJson["Response"]["sales"]["data"].keys())[0]]["saleItems"][list(self.forSaleItems)[i]]["itemHash"])
            self.hashIDList.append(self.apiResponseJson["Response"]["sales"]["data"][list(self.apiResponseJson["Response"]["sales"]["data"].keys())[0]]["saleItems"][list(self.forSaleItems)[i]].get('vendorItemIndex'))
        print(self.hashIDList)
        #remove unwanted items via their hash
        self.hashList = [hash_ for hash_ in self.hashList if hash_ not in unwanted_hashes]
        
        print(self.hashIDList)
        await self.parseHash()
        await self.tweet(sendTweet=SEND_TWEET)

def mainloop():
    #create and set new loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    TB = main(apiKey)
    loop.run_until_complete(TB.getXurInventory())

mainloop()