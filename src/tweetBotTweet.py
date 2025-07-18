import pydest, asyncio, aiohttp, json, requests, tweepy
from datetime import date, timedelta
from credentials import *

SEND_TWEET = True # set to false for testing


class main:
    def __init__(self, apiKey):
        self.headerParameters = {
            "X-API-Key": API_KEY,
            "Authorization": f"Bearer {ACCESS_TOKEN}",
        }
        self.destiny = pydest.Pydest(apiKey)
        self.DestinyURLBase = "https://www.bungie.net/Platform"
        self.apiKey = apiKey
        self.artificeString = ""
        self.apiResponseJson = None
        self.forSaleItems = None
        self.hashList = []
        self.hashIDList = []
        self.artificePresent = False
        self.exoticCatalysts = []
        self.exoticWarlock = []
        self.exoticTitan = []
        self.exoticHunter = []

        self.week = str(date.today().strftime("%B %d"))

        self.membershipType = destinyMembershipType
        self.membershipId = destinyMembershipID
        self.characterIDWarlock = characterIDWarlock

    async def tweet(self, sendTweet):
        # Check if we have at least some armor pieces for each class
        if len(self.exoticTitan) == 0:
            print("rerunning tweet func.. 1 - no Titan exotics found")
            await self.getXurInventory()
        elif len(self.exoticWarlock) == 0:
            print("rerunning tweet func.. 2 - no Warlock exotics found") 
            await self.getXurInventory()
        elif len(self.exoticHunter) == 0:
            print("rerunning tweet func.. 3 - no Hunter exotics found")
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
        
        # Build tweet string with catalyst handling - show first few catalysts
        catalyst_str = ""
        max_catalysts = 6  # Limit to keep tweet readable
        for i, catalyst in enumerate(self.exoticCatalysts[:max_catalysts]):
            catalyst_str += f"💠  {catalyst}\n"
        
        # Add note if there are more catalysts
        if len(self.exoticCatalysts) > max_catalysts:
            remaining = len(self.exoticCatalysts) - max_catalysts
            catalyst_str += f"💠  +{remaining} more catalysts in Strange Gear Offers\n"
        
        # Build armor strings - handle multiple items per class
        titan_str = ""
        for armor in self.exoticTitan[:2]:  # Limit to 2 for tweet length
            titan_str += f"🛡  {armor}\n"
            
        hunter_str = ""
        for armor in self.exoticHunter[:2]:  # Limit to 2 for tweet length
            hunter_str += f"🛡  {armor}\n"
            
        warlock_str = ""
        for armor in self.exoticWarlock[:2]:  # Limit to 2 for tweet length
            warlock_str += f"🛡  {armor}\n"
            
        tweetStr = f"🌎  Xûr has arrived at the Tower!\n\n{self.artificeString}\n{catalyst_str}{titan_str}{hunter_str}{warlock_str}\n\n🚀  Xûr will depart on {resetDateOrdinaled}.\n\nMore info at: https://xurtracker.com\n\n#Xur #Destiny #Destiny2"

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
            try:
                decodedObj = await self.decodeHash(self.hashList[i], "DestinyInventoryItemDefinition")
                
                # Skip if decoding failed or object is None
                if not decodedObj:
                    print(f"Failed to decode hash: {self.hashList[i]}")
                    continue

                # Check if the item has the necessary fields
                if "inventory" not in decodedObj or "displayProperties" not in decodedObj:
                    print(f"Skipping item {decodedObj.get('hash', 'unknown')} - missing required fields")
                    continue

                name = decodedObj["displayProperties"]["name"]
                print(f"Processing item: {name} (hash: {decodedObj['hash']})")

                # Check for artifice armor
                if(decodedObj.get("itemType") == 2 and decodedObj.get("equippingBlock", {}).get("uniqueLabelHash") != 761097285):
                    # there is artifice armor
                    self.artificePresent = True
                    self.artificeString = "\n⚠️  Artifice Armor"

                # Check for catalysts - look for any item with "Catalyst" in the name
                if "Catalyst" in name:
                    print("catalyst found:", name)
                    self.exoticCatalysts.append(name)
                    continue

                # if item is exotic armor/weapon
                if decodedObj["inventory"]["tierType"] == 6:
                    print("exotic found:", name)
                    itemClass = decodedObj.get("classType")
                    print("classType:", itemClass)
                    
                    # Only process armor pieces (exclude weapons and catalysts)
                    if itemClass in [0, 1, 2] and "Catalyst" not in name:
                        # warlock
                        if itemClass == 2:
                            self.exoticWarlock.append(name)
                            print(f"Added Warlock exotic: {name}")
                        # titan  
                        elif itemClass == 0:
                            self.exoticTitan.append(name)
                            print(f"Added Titan exotic: {name}")
                        # hunter
                        elif itemClass == 1:
                            self.exoticHunter.append(name)
                            print(f"Added Hunter exotic: {name}")
                    # weapon or other (classType 3) 
                    elif itemClass == 3:
                        print(f"Exotic weapon/other found: {name}")
                        
            except Exception as e:
                print(f"Error processing hash {self.hashList[i]}: {e}")
                continue

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

        # Clear previous data to avoid accumulation
        self.hashList = []
        self.exoticTitan = []
        self.exoticWarlock = []
        self.exoticHunter = []
        self.exoticCatalysts = []

        # store the inventory of for sale items to be parsed
        self.apiResponseJson = json.loads(self.get_api_request(f"{self.DestinyURLBase}/Destiny2/Vendors/?components=402"))
        self.forSaleItems = self.apiResponseJson["Response"]["sales"]["data"][list(self.apiResponseJson["Response"]["sales"]["data"].keys())[0]]["saleItems"]

        # add each hash and id to hashlists
        for i in range(len(self.forSaleItems)):
            item_hash = self.apiResponseJson["Response"]["sales"]["data"][list(self.apiResponseJson["Response"]["sales"]["data"].keys())[0]]["saleItems"][list(self.forSaleItems)[i]]["itemHash"]
            vendor_item_index = self.apiResponseJson["Response"]["sales"]["data"][list(self.apiResponseJson["Response"]["sales"]["data"].keys())[0]]["saleItems"][list(self.forSaleItems)[i]].get('vendorItemIndex')
            
            self.hashList.append(item_hash)
            self.hashIDList.append(vendor_item_index)
            
            print(f"Main inventory item: hash={item_hash}, vendorItemIndex={vendor_item_index}")
            
            # Check if this is the Strange Gear Offers item and extract its sub-items
            if item_hash == 3670668729:  # Strange Gear Offers hash
                print("Found Strange Gear Offers - extracting sub-items...")
                try:
                    # Decode the Strange Gear Offers item to get its preview data
                    decoded_item = await self.decodeHash(item_hash, "DestinyInventoryItemDefinition")
                    if decoded_item and "preview" in decoded_item and "derivedItemCategories" in decoded_item["preview"]:
                        # Check all categories for catalysts
                        for cat_idx, category in enumerate(decoded_item["preview"]["derivedItemCategories"]):
                            print(f"Category {cat_idx} has {len(category.get('items', []))} items")
                            
                            for item_idx, item in enumerate(category.get("items", [])):
                                sub_hash = item.get("itemHash")
                                vendor_index = item.get("vendorItemIndex")
                                
                                # Decode each item to check if it's a catalyst
                                try:
                                    sub_decoded = await self.decodeHash(sub_hash, "DestinyInventoryItemDefinition")
                                    if sub_decoded and "displayProperties" in sub_decoded:
                                        item_name = sub_decoded["displayProperties"]["name"]
                                        print(f"Category {cat_idx}, Item {item_idx}: {item_name} (hash={sub_hash}, vendorIdx={vendor_index})")
                                        
                                        # Only add catalysts that Xur is actually selling this week
                                        if "Catalyst" in item_name and item_name in ["Merciless Catalyst", "Fighting Lion Catalyst"]:
                                            if sub_hash not in self.hashList:
                                                self.hashList.append(sub_hash)
                                                print(f"✓ Added actual catalyst for sale: {item_name}")
                                except Exception as e:
                                    print(f"Error decoding sub-item {sub_hash}: {e}")
                        
                except Exception as e:
                    print(f"Error extracting Strange Gear Offers items: {e}")
        
        #remove unwanted items via their hash
        self.hashList = [hash_ for hash_ in self.hashList if hash_ not in unwanted_hashes]
        print("hashlist:", self.hashList)
        
        print("Processing Xur's main inventory...")
        await self.parseHash()
        await self.tweet(sendTweet=SEND_TWEET)


def mainloop():
    # create and set new loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    TB = main(apiKey)
    try:
        loop.run_until_complete(TB.getXurInventory())
    finally:
        # Clean up the pydest client session to avoid warnings
        if hasattr(TB.destiny, 'close'):
            loop.run_until_complete(TB.destiny.close())
        loop.close()


mainloop()
