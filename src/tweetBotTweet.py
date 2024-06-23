import pydest, asyncio, aiohttp, json, requests, tweepy, random
import time
from datetime import date, timedelta
from credentials import *

SEND_TWEET = False


class main:
    def __init__(self, apiKey):
        self.headerParameters = {
            "X-API-Key": API_KEY,
            "Authorization": f"Bearer {ACCESS_TOKEN}",
        }
        self.destiny = pydest.Pydest(apiKey)
        self.DestinyURLBase = "https://www.bungie.net/Platform"
        self.apiKey = apiKey
        self.artificeString = None
        self.apiResponseJson = None
        self.forSaleItems = None
        self.hashList = []
        self.hashIDList = []
        self.artificePresent = False
        self.exoticCatalysts = []
        self.exoticWarlock = None
        self.exoticTitan = None
        self.exoticHunter = None

        self.week = str(date.today().strftime("%B %d"))

        self.membershipType = destinyMembershipType
        self.membershipId = destinyMembershipID
        self.characterIDWarlock = characterIDWarlock

    async def tweet(self, sendTweet):
        # none checks
        if self.exoticTitan == None:
            print("rerunning tweet func..")
            await self.getXurInventory()
        if self.exoticWarlock == None:
            print("rerunning tweet func..")
            await self.getXurInventory()
        if self.exoticHunter == None:
            print("rerunning tweet func..")
            await self.getXurInventory()
        if len(self.exoticCatalysts) != 2:
            print("rerunning tweet func..")
            await self.getXurInventory()

        # setup twitter auth for v2 and v1 endpoints
        client = tweepy.Client(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token=access_token,
            access_token_secret=access_token_secret,
        )

        authV1 = tweepy.OAuth1UserHandler(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token=access_token,
            access_token_secret=access_token_secret,
        )
        clientV1 = tweepy.API(authV1)

        # update profile statuses
        clientV1.update_profile(location="Bazaar, The Last City")
        clientV1.update_profile_banner(filename="/home/ubuntu/XurTracker/imgs/xur-tower.jpg")

        # calculate reset date
        resetDate = date.today() + timedelta((1 - date.today().weekday()) % 7)
        resetDate = resetDate.strftime("%B %d").replace(" 0", " ")
        resetDateOrdinaled = self.addOrdinal(resetDate)
        tweetStr = f"🌎  Xûr has arrived at the Tower!\n\n{self.artificeString}\n💠  {self.exoticCatalysts[0]}\n💠  {self.exoticCatalysts[1]}\n🛡  {self.exoticTitan}\n🛡  {self.exoticHunter}\n🛡  {self.exoticWarlock}\n\n\n\n🚀  Xûr will depart on {resetDateOrdinaled}.\n\nMore info at: https://xurtracker.com\n\n#Xur #Destiny  #Destiny2"

        # tweet check
        if sendTweet:
            client.create_tweet(text=str(tweetStr))
        else:
            print("tweet:\n\n", tweetStr, "\n")
            print("sendTweet bool is set to false.")

    # Make a GET request to api and return json
    def get_api_request(self, url):
        try:
            # get api request and parse to json
            res = requests.get(url, headers=self.headerParameters)
            jsonResponse = json.dumps(res.json(), sort_keys=True, indent=4)
        except aiohttp.client_exceptions.ClientResponseError as e:
            print("ERROR: Could not connect to Bungie.net Endpoint\n", e)
        return jsonResponse

    # decode the hash from the manifest
    async def decodeHash(self, hash, manifestValue):
        hashedData = await self.destiny.decode_hash(hash, manifestValue)
        return hashedData

    # run through the hash list and format each hash and pull out its data
    async def parseHash(self):

        for i in range(len(self.hashList)):
            decodedObj = await self.decodeHash(self.hashList[i], "DestinyInventoryItemDefinition")

            if(decodedObj["itemType"] == 2 and decodedObj["equippingBlock"].get("uniqueLabelHash") != 761097285):
                # there is artifice armor
                self.artificePresent = True
                self.artificeString = "\n⚠️  Artifice Armor"

            # if item is exotic
            if decodedObj["inventory"]["tierType"] == 6:

                name = decodedObj["displayProperties"]["name"]
                itemClass = decodedObj["classType"]

                # warlock
                if itemClass == 2:
                    self.exoticWarlock = name

                # titan
                elif itemClass == 0:
                    self.exoticTitan = name

                # hunter
                elif itemClass == 1:
                    self.exoticHunter = name

                # catalyst
                else:
                    if len(self.exoticCatalysts) > 2:
                        break

                    if decodedObj["traitIds"][0] == "item.exotic_catalyst":
                        self.exoticCatalysts.append(name)

    # get data from api
    def get_api_request(self, url):
        try:
            # get api request and store into a json format
            res = requests.get(url, headers=self.headerParameters)
            jsonResponse = json.dumps(res.json(), sort_keys=True, indent=4)
        except aiohttp.client_exceptions.ClientResponseError as e:
            print("ERROR: Could not connect to Bungie.net Endpoint\n", e)

        return jsonResponse

    # add endings like st or th to the date
    def addOrdinal(self, date):
        rawDate = int(date.split(" ")[1])
        rawDateOnes = rawDate % 10
        suffix = "th"

        # deal with most of the th endings first
        if rawDate <= 20 and rawDate > 3:
            suffix = "th"
        elif rawDateOnes == 1:
            suffix = "st"
        elif rawDateOnes == 2:
            suffix = "nd"
        elif rawDateOnes == 3:
            suffix = "rd"

        return date + suffix

    async def getXurInventory(self):

        unwanted_hashes = {2125848607, 1092685591, 4257549985, 353704689, 903043774}

        # store the inventory of for sale items to be parsed
        self.apiResponseJson = json.loads(self.get_api_request(f"{self.DestinyURLBase}/Destiny2/Vendors/?components=402"))
        self.forSaleItems = self.apiResponseJson["Response"]["sales"]["data"][list(self.apiResponseJson["Response"]["sales"]["data"].keys())[0]]["saleItems"]

        # add each hash and id to hashlists
        for i in range(len(self.forSaleItems)):
            self.hashList.append(self.apiResponseJson["Response"]["sales"]["data"][list(self.apiResponseJson["Response"]["sales"]["data"].keys())[0]]["saleItems"][list(self.forSaleItems)[i]]["itemHash"])
            self.hashIDList.append(self.apiResponseJson["Response"]["sales"]["data"][list(self.apiResponseJson["Response"]["sales"]["data"].keys())[0]]["saleItems"][list(self.forSaleItems)[i]].get('vendorItemIndex'))
        

        #remove unwanted items via their hash
        self.hashList = [hash_ for hash_ in self.hashList if hash_ not in unwanted_hashes]

        await self.parseHash()
        await self.tweet(sendTweet=SEND_TWEET)


def mainloop():
    # create and set new loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    TB = main(apiKey)
    loop.run_until_complete(TB.getXurInventory())


mainloop()
