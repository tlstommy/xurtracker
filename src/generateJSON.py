import requests,aiohttp,asyncio,json,pydest
from bs4 import BeautifulSoup
from datetime import date
from material_prices import *
from credentials import *

HEADERS = { "X-API-Key": API_KEY, "Authorization": f"Bearer {ACCESS_TOKEN}" }



#strange gear offers hash 3751514131

class main:
    def __init__(self, apiKey):
        #destiny pydest object
        self.destiny = pydest.Pydest(apiKey)
        self.apiKey = apiKey
        self.membershipId = destinyMembershipID
        self.membershipType = destinyMembershipType
        self.warlockCharacterID = characterIDWarlock
        self.titanCharacterID = characterIDTitan
        self.hunterCharacterID = characterIDHunter
        self.destinyURLBase = "https://www.bungie.net/Platform"
        self.vendorHash = "2190858386" #xur
        self.strangeGearVendorHash = "3751514131" #xur's strange gear tab inside of the xurs menu
        self.strangeMaterialVendorHash = "537912098" #xur's strange material offerings tab

        #hashes of items that xur can sell under multivarious strange offers
        self.multivariousOfferableItems = [2979281381, 3282419336, 1260977951, 554159122, 3036656991, 451915085, 2207883242, 3643918802]
        
        #excludeable material hashes from xur, 1 coin engram, favor of the nine etc
        self.excludeableMaterialHashes = [4032296272,3581456570]

        #misc other items xur can offer, like the xurfboard
        self.miscItemHashes = [3158812152]

        self.ArtificePresent = False

        #hunter warlock titan
        self.artificeHashes = [None,None,None]

        self.combinedPerksJson = None

        self.apiResponse = None
        self.apiResponseJson = None
        self.location = None

        #dict of xurs for sale items
        self.forSaleItems = None

        #more general logistics
        self.location = None
        self.planet = None
        self.landingZone = None
        self.locationHash = None
        self.planetHash = None
        self.week = None

        #for weapon rating
        self.ratingList = []


        #class specific exotics
        self.WarlockExotic = None
        self.TitanExotic = None
        self.HunterExotic = None

        #hunter,warlock,titan
        self.ArtificeArmor = [None,None,None] 

        #class specific armor
        self.WarlockExotic = None
        self.WarlockHelmet = None
        self.WarlockArms = None
        self.WarlockChest = None
        self.WarlockLegs = None
        self.WarlockClassItem = None
        
        self.HunterExotic = None
        self.HunterHelmet = None
        self.HunterArms = None
        self.HunterChest = None
        self.HunterLegs = None
        self.HunterClassItem = None
        
        self.TitanExotic = None
        self.TitanHelmet = None
        self.TitanArms = None
        self.TitanChest = None
        self.TitanLegs = None
        self.TitanClassItem = None

        #exotic weapons
        self.ExoticWeapons = []
        self.Hawkmoon = None

        #exotic weapon catalysts
        self.FirstCatalyst = None
        self.SecondCatalyst = None

        #the regular weapons that xur sells
        self.LegendaryWeapons = []

        #different resurces/engrams xur sells
        self.MaterialOffers = []

        #misc items, i.e xurfboard
        self.MiscOffers = []
        
        #general items
        self.ExoticEngram = {
            "name": "Exotic Engram",
            "type": "Exotic Engram",
            "description": "An engram with a predestined outcome.\n\nContains a new Exotic if any of the possible rewards remain to be collected. Preview contents for possible rewards.",
            "lore": "",
            "ExtLore": None,
            "itemHash": "3875551374",
            "itemRating": None,
            "icon": "https://www.bungie.net/common/destiny2_content/icons/ee21b5bc72f9e48366c9addff163a187.png",
            "rarity": "Exotic",
            "class": 3,
            "statRolls": [],
            "weaponPerks": [],
            "exoticArmorPerk": None,
            "legendWeaponFrame": None,
            "legendWeaponDamageType": None,
            "legendWeaponDamageElement": None,
            "masterworkData": None,
        }
        self.ExoticQuest = {
            "name": "Xenology",
            "type": "Exotic Quest Step",
            "description": "Complete Vanguard playlist activities, or win matches in Crucible or Gambit.\n\nExtra progress is awarded for more challenging activities and for succeeding with clanmates.",
            "lore": "",
            "ExtLore": None,
            "itemHash": "2125848607",
            "itemRating": None,
            "icon": "https://www.bungie.net/common/destiny2_content/icons/7f9e6e79bb7a8ce59de9258a7d674af2.jpg",
            "rarity": "Exotic",
            "class": 3,
            "statRolls": [],
            "weaponPerks": [],
            "exoticArmorPerk": None,
            "legendWeaponFrame": None,
            "legendWeaponDamageType": None,
            "legendWeaponDamageElement": None,
            "masterworkData": None,
        }

        #makes tying weapons to rolls easier, prob could have done this cleaner
        self.weaponPerksTemplateList = []
        self.weaponsTemplatesList = []

        self.XursInventoryItems = []


    #loop through items and assing json template items
    async def bindJsonData(self):

        #set date
        today = date.today()
        self.week = str(today.strftime("%B %d, %Y"))
        await self.getLocation()


        for item in self.XursInventoryItems:
            if item["rarity"] == "Exotic":
                if item["itemHash"] != "3856705927":
                    self.ExoticWeapons.append(item)
                else:
                    self.Hawkmoon = item
                    


    #create a json file from all of the collected data
    def buildJSON(self,write):
        JSONTemplate = {
                    "Location":self.location,
                    "Planet":self.planet,
                    "Landing Zone":self.landingZone,
                    "Week":self.week,
                    "Artifice":self.ArtificePresent,
                    "Catalysts":{
                        "Primary":self.FirstCatalyst,
                        "Secondary":self.SecondCatalyst,
                    },
                    "Exotics":{
                        "Exotic Engram":self.ExoticEngram,
                        "Exotic Quest":self.ExoticQuest,
                        "Hawkmoon":self.Hawkmoon,
                        "Exotic Weapons":self.ExoticWeapons,
                        "Warlock Exotic":self.WarlockExotic,
                        "Hunter Exotic":self.HunterExotic,
                        "Titan Exotic":self.TitanExotic,
                    },
                    "Material Offers":self.MaterialOffers,
                    "Miscellaneous Offers":self.MiscOffers,
                    "Artifice Armor":{
                        "Warlock":self.ArtificeArmor[1],
                        "Hunter":self.ArtificeArmor[0],
                        "Titan":self.ArtificeArmor[2],
                    },
                    "Legendaries":{
                        "Legendary weapons":self.LegendaryWeapons,
                        "Warlock":{
                            "Helmet":self.WarlockHelmet,
                            "Arms":self.WarlockArms,
                            "Chest":self.WarlockChest,
                            "Legs":self.WarlockLegs,
                            "Class Item":self.WarlockClassItem,
                        },
                        "Hunter":{
                            "Helmet":self.HunterHelmet,
                            "Arms":self.HunterArms,
                            "Chest":self.HunterChest,
                            "Legs":self.HunterLegs,
                            "Class Item":self.HunterClassItem,
                        },
                        "Titan":{
                            "Helmet":self.TitanHelmet,
                            "Arms":self.TitanArms,
                            "Chest":self.TitanChest,
                            "Legs":self.TitanLegs,
                            "Class Item":self.TitanClassItem,
                        },
                    }
                }
        if(write == True):
            #serialize JSON
            with open("/home/ubuntu/XurTracker/data/data.json","w",encoding='utf-8') as outfile:
                json.dump(JSONTemplate,outfile,indent=4)
            outfile.close()

            with open("/home/ubuntu/XurTracker/frontend/src/destinyData.json","w",encoding='utf-8') as outfile:
                json.dump(JSONTemplate,outfile,indent=4)    
            outfile.close()

    async def getLocation(self):
        apiUrl400 = self.destinyURLBase + f"/Destiny2/{self.membershipType}/Profile/{self.membershipId}/Character/{characterIDWarlock}/Vendors/?components=400"
        apiResponse400 = self.get_api_request(apiUrl400)
        apiResponse400Json = json.loads(apiResponse400)
        
        xurVendorLoc = apiResponse400Json["Response"]["vendors"]["data"]["2190858386"].get("vendorLocationIndex")
        
        if xurVendorLoc == 0:
            self.planet = "Earth"
            self.location = "The Last City"
            self.landingZone = "Tower Hangar"
        if xurVendorLoc == 1:
            self.planet = "Earth"
            self.location = "European Dead Zone"
            self.landingZone = "Winding Cove"
        if xurVendorLoc == 2:
            self.planet = "Nessus"
            self.location = "Arcadian Valley"
            self.landingZone = "Watcher's Grave"

    #combines a list of sockets and plugs together
    def socketPlugs(self, socketJSON, plugJSON):
        # Convert JSON if they are not already
        if isinstance(socketJSON, str):
            socketJSON = json.loads(socketJSON)
        if isinstance(plugJSON, str):
            plugJSON = json.loads(plugJSON)

        # Extracting the relevant data from the JSON
        sockets = socketJSON["Response"]["itemComponents"]["sockets"]["data"]
        plugs = plugJSON["Response"]["itemComponents"]["reusablePlugs"]["data"]

        combined_data = {}

        # Iterate through the sockets data and combine with plugs data
        for item_id, socket_info in sockets.items():
            seen_hashes = set()  # Set to track seen hashes
            hashes = []

            # Function to add hash if not seen
            def add_hash(hash_value):
                if hash_value not in seen_hashes:
                    seen_hashes.add(hash_value)
                    hashes.append({"hash": hash_value})

            # Add hashes from sockets
            for socket in socket_info["sockets"]:
                if "plugHash" in socket and socket["isEnabled"]:
                    add_hash(socket["plugHash"])
                
            # Add hashes from plugs
            if item_id in plugs:
                for plug_slot, plug_list in plugs[item_id]["plugs"].items():
                    for plug in plug_list:
                        if plug["enabled"]:
                            add_hash(plug["plugItemHash"])

            combined_data[item_id] = {"hashes": hashes}

        return combined_data

    #sorts weapon perks so that grouped perks are next to eachother
    def perkSort(self,perkList):

        newPerkListDict = {}

        #group by subtypes
        for perk in perkList:
            perkType = perk["perkSubType"]
            if perkType not in newPerkListDict:
                newPerkListDict[perkType] = []
            newPerkListDict[perkType].append(perk)

        newPerkList = []

        for perkType, perks in newPerkListDict.items():
            newPerkList.extend(perks)

        return newPerkList


    async def getWeaponPerks(self):

        #weapon Perk template
        IDtoWeaponHashDict = {}
        itemIDs402 = []
        socketIDs305 = []
        currentAvailableItems = []
        weaponPerkList = []
        
        
        
        
        #item sockets
        apiUrl305 = self.destinyURLBase + f"/Destiny2/{self.membershipType}/Profile/{self.membershipId}/Character/{characterIDWarlock}/Vendors/{self.strangeGearVendorHash}/?components=305"
        apiResponse305 = self.get_api_request(apiUrl305)
        apiResponse305Json = json.loads(apiResponse305)

        #itemplugs
        apiUrl310 = self.destinyURLBase + f"/Destiny2/{self.membershipType}/Profile/{self.membershipId}/Character/{characterIDWarlock}/Vendors/{self.strangeGearVendorHash}/?components=310"
        apiResponse310 = self.get_api_request(apiUrl310)
        apiResponse310Json = json.loads(apiResponse310)
        
        
        #self.combinedPerkJson = self.socketPlugs(apiResponse305Json,apiResponse310Json)


        #item ids
        apiUrl402 = self.destinyURLBase + f"/Destiny2/{self.membershipType}/Profile/{self.membershipId}/Character/{characterIDWarlock}/Vendors/{self.strangeGearVendorHash}/?components=402"
        apiResponse402 = self.get_api_request(apiUrl402)
        apiResponse402Json = json.loads(apiResponse402)
        
        for itemID, itemIDData in apiResponse402Json["Response"]["sales"]["data"].items():
            itemIDs402.append(itemID)
        
        for socketID, socketIDData in apiResponse305Json["Response"]["itemComponents"]["sockets"]["data"].items():
            socketIDs305.append(socketID)
            
        for i in range(len(itemIDs402)):
            if itemIDs402[i] in socketIDs305:
                currentAvailableItems.append(itemIDs402[i])
        
        print(currentAvailableItems)
        



        for key, value in apiResponse402Json["Response"]["sales"]["data"].items():
            
            #if key in currentavailableitems list of ids append it to the dict
            if key in currentAvailableItems:
                IDtoWeaponHashDict[key]=value.get("itemHash")


        print(IDtoWeaponHashDict)
        


        #now get each individual weapons perks

        print(self.combinedPerksJson.items())
    
        
        for key, values in self.combinedPerksJson.items():
            
            hashList = values.get("hashes")
            
            for item in hashList:
                
                if(key in currentAvailableItems):   
                    
                    isArmor = False
                    try:
                        plugHashVal = item["hash"]
                    except KeyError as e:
                        print("keyerror plughash: ",e)
                        continue
                    print(plugHashVal)    
                    decodedPlug = await self.decodeHash(plugHashVal,"DestinyInventoryItemDefinition")
                    
                    print(decodedPlug)
                    #input("test!!!\n")
                    
                    
                    
                    #check if armor or not
                    decodedWeaponHash = await self.decodeHash(IDtoWeaponHashDict[key],"DestinyInventoryItemDefinition")

                    #if it is the armor type
                    if(decodedWeaponHash.get("itemType") == 2):
                        continue
                    

                    #make sure its a trait of sometype
                    perkType = decodedPlug["plug"].get("plugCategoryIdentifier")
                    
                    if perkType == "" or decodedPlug["displayProperties"].get("name") == "Crucible Tracker":
                        continue
                        
                    
                    perkType = decodedPlug.get("itemTypeDisplayName")
                    
                    perkSubType = decodedPlug["plug"].get("plugCategoryIdentifier")


                    #get ivestment stats for perk

                    #weapon Perk template
                    weaponRollTemplate = {
                        "name":decodedPlug["displayProperties"].get("name"),
                        "description":decodedPlug["displayProperties"].get("description"),
                        "perkIcon":"https://www.bungie.net"+str(decodedPlug["displayProperties"].get("icon")),
                        "hashID":decodedPlug.get("hash"),
                        "weaponHash":IDtoWeaponHashDict[key],
                        "isPerk":True,
                        "isFavorablePerk":False,
                        "perkType":perkType,
                        "perkSubType":perkSubType
                    }

                    
                    
                    

                    #filter out unwanted perks
                    if(weaponRollTemplate["name"] != 'Empty Mod Socket' and weaponRollTemplate["name"] != '' and weaponRollTemplate["name"] != 'Tracker Disabled' and weaponRollTemplate["name"] != 'Default Shader' 
                        and weaponRollTemplate["name"] != 'Default Ornament' and weaponRollTemplate["name"] != 'Change Energy Type' and weaponRollTemplate["name"] !='Empty Catalyst Socket' and "catalyst" not in weaponRollTemplate["name"]
                        and "Catalyst" not in weaponRollTemplate["name"] and weaponRollTemplate["name"] != "Rasputin's Arsenal" and weaponRollTemplate["name"] != "Kill Tracker" and weaponRollTemplate["name"] != "Empty Memento Socket" and weaponRollTemplate["name"] != "Empty Weapon Level Boost Socket" and weaponRollTemplate["name"] != "Empty Deepsight Socket"):
                        weaponRollTemplate["isFavorablePerk"] = self.rateWeaponPerks(IDtoWeaponHashDict[key],decodedPlug["displayProperties"].get("name"))
                        self.weaponPerksTemplateList.append(weaponRollTemplate)
                    
                        
    #pull community perk rating data
    def grabPerks(self,weaponHash):
        favorablePerks = []
        url = "https://www.light.gg/db/items/"+str(weaponHash)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        try:
            communityPerksRows = soup.find(id = "community-average").find_all("ul")
        except AttributeError as e:
            return -1
        for row in communityPerksRows:
            perks = row.find_all("li")
            if(len(perks) > 1):
                topPerk = perks[0].find("img")
                topPerkStr = str(topPerk).split('" ')
                topPerkStr = topPerkStr[0].replace('<img alt="','')
                favorablePerks.append(topPerkStr)
            else:
                favorablePerks.append("")
                continue
        return favorablePerks

    #determine if its a "god" perk
    def rateWeaponPerks(self,weaponHash,perkName):
        topPerks = self.grabPerks(weaponHash)
        if(topPerks == -1):
            return False
        for i in range(len(topPerks)):
            if(topPerks[i] == perkName):
                return True
        return False

    #get data for the weapons
    async def getWeapons(self):

        weaponHashList = []

        apiUrl402 = self.destinyURLBase + f"/Destiny2/{self.membershipType}/Profile/{self.membershipId}/Character/{characterIDWarlock}/Vendors/{self.strangeGearVendorHash}/?components=402"
        apiResponse402 = self.get_api_request(apiUrl402)
        apiResponse402Json = json.loads(apiResponse402)
        
        for itemID, itemIDData in apiResponse402Json["Response"]["sales"]["data"].items():
            weaponID = await self.decodeHash(itemIDData.get("itemHash"),"DestinyInventoryItemDefinition")
            #check if the hash is tied to a weapon
            if(weaponID.get("itemType") == 3):
                weaponHashList.append(itemIDData.get("itemHash"))
        
        #run through hash list and get data for each weapon
        for item in weaponHashList:
            weaponHashData = await self.decodeHash(item,"DestinyInventoryItemDefinition")
            loreHash = weaponHashData.get("loreHash")
            if(loreHash == None):
                weaponLore = None
            else:
                weaponLore = await self.decodeHash(str(loreHash),"DestinyLoreDefinition")
                weaponLore = weaponLore["displayProperties"].get("description")

            #decode elemental information
            elementData = await self.decodeHash(str(weaponHashData["damageTypeHashes"][0]),"DestinyDamageTypeDefinition")

            damageType = weaponHashData["itemCategoryHashes"][0]
            damageTypeHash = await self.decodeHash(damageType,"DestinyItemCategoryDefinition")


            #template for item jsons
            jsonTemplate = {
                "name":weaponHashData["displayProperties"].get("name"),
                "type":weaponHashData.get("itemTypeAndTierDisplayName"),
                "description":weaponHashData["displayProperties"].get("description"),
                "lore":weaponHashData.get("flavorText"),
                "ExtLore":weaponLore,
                "itemHash":str(item),
                "ammoType":weaponHashData["equippingBlock"].get("ammoType"),
                "itemRating":None,
                "icon":"https://www.bungie.net"+str(weaponHashData["displayProperties"].get("icon")),
                "backgroundImage" : "https://www.bungie.net"+str(weaponHashData.get("screenshot")),
                "rarity":weaponHashData["inventory"].get("tierTypeName"),
                "class":weaponHashData.get("classType"), 
                "statRolls":[],
                "weaponPerks":[],
                "originTrait":None,
                "exoticArmorPerk":None,
                "legendWeaponFrame":None,
                "legendWeaponDamageType":damageTypeHash.get("shortTitle"),
                "legendWeaponDamageElement":elementData["displayProperties"].get("name"),
                "masterworkData":None,
                "damageTypeIcon":"https://www.bungie.net"+str(elementData["displayProperties"].get("icon")),
            }

            print("\n")
            
            
            if(jsonTemplate.get("rarity") != "Exotic"):
                self.LegendaryWeapons.append(jsonTemplate)

            self.weaponsTemplatesList.append(jsonTemplate)
        await self.getWeaponPerks()
        await self.bindStatToWeapon()


        for item in self.weaponsTemplatesList:
            perkHashList = []
            
            for perk in item["weaponPerks"]:
                perkHashList.append(perk["hashID"])
            self.XursInventoryItems.append(item)

    
    async def bindStatToWeapon(self):

        for item in self.weaponsTemplatesList:
            weaponHash = item.get("itemHash")
            print(item.get("name"))
            for perk in self.weaponPerksTemplateList:
                
                perkWHash = perk.get("weaponHash")
                
                if weaponHash == str(perkWHash):
                    
                    #if the perk is a masterwork decode it
                    if perk.get("description") == "Base-level weapon. Increase the tier to forge a Masterwork item.":    
                        print(perk)
                        masterWorkDecoded = await self.decodeHash(perk.get("hashID"),"DestinyInventoryItemDefinition")
                        statIcon = "https://www.bungie.net"+str(masterWorkDecoded["displayProperties"].get("icon"))
                        statTypeHash = str(masterWorkDecoded["investmentStats"][0].get("statTypeHash"))
                        statHashDecoded = await self.decodeHash(statTypeHash,"DestinyStatDefinition")

                        masterworkTemplate = {
                            "name":statHashDecoded["displayProperties"].get("name"),
                            "description":statHashDecoded["displayProperties"].get("description"),
                            "icon":statIcon,
                            "mwHash":perk.get("hashID"),
                        }
                        item["masterworkData"] = masterworkTemplate
                        
                        print(item)
                        print(masterworkTemplate)
                        continue

                    #decode perk to see if its a "frame-related" perk
                    if (await self.decodeHash(perk.get("hashID"),"DestinyInventoryItemDefinition")).get("uiItemDisplayStyle") == "ui_display_style_intrinsic_plug" and item.get("rarity") != "Exotic":
                        data = await self.decodeHash(perk.get("hashID"),"DestinyInventoryItemDefinition")
                        item["legendWeaponFrame"] = {
                            "name":data["displayProperties"].get("name"),
                            "description":data["displayProperties"].get("description"),
                            "icon":"https://www.bungie.net"+str(data["displayProperties"].get("icon")),
                        }
                        print("MATCH")
                        continue       
                    
                    
                    
                    #append origin traits if present
                    if perk.get("perkSubType") == "origins":
                        item["originTrait"] = perk
                        continue
                        
                    
                    if "masterwork" not in perk.get("perkSubType"):

                        item["weaponPerks"].append(perk)

                    
            
            #group perks on the item
            item["weaponPerks"] = self.perkSort(item["weaponPerks"])
            
            
   
                        




    
    def decodeStatHash(self,hash):
        if hash == 144602215:
            return "Intellect"
        if hash == 392767087:
            return "Resilience"
        if hash == 1735777505:
            return "Discipline"
        if hash == 1943323491:
            return "Recovery"
        if hash == 2996146975:
            return "Mobility"
        if hash == 4244567218:
            return "Strength"

    async def getExoticArmor(self,classID,classType):
        #armor stat template
        IDtoArmorHashDict = {}
        socketStatDict = {}
        itemIDs402 = []
        socketIDs305 = []
        currentAvailableItems = []
        currentAvailableArmorItems = []
        
        #item sockets
        apiUrl304 = self.destinyURLBase + f"/Destiny2/{self.membershipType}/Profile/{self.membershipId}/Character/{classID}/Vendors/{self.vendorHash}/?components=304"
        apiResponse304 = self.get_api_request(apiUrl304)
        apiResponse304Json = json.loads(apiResponse304)

        #item ids
        apiUrl402 = self.destinyURLBase + f"/Destiny2/{self.membershipType}/Profile/{self.membershipId}/Character/{classID}/Vendors/{self.vendorHash}/?components=402"
        apiResponse402 = self.get_api_request(apiUrl402)
        apiResponse402Json = json.loads(apiResponse402)
        
        for itemID, itemIDData in apiResponse402Json["Response"]["sales"]["data"].items():
            itemIDs402.append(itemID)
            
        
        for socketID, socketIDData in apiResponse304Json["Response"]["itemComponents"]["stats"]["data"].items():
            socketIDs305.append(socketID)
            socketStatDict[socketID]=socketIDData
            
        for i in range(len(itemIDs402)):
            if itemIDs402[i] in socketIDs305:
                currentAvailableItems.append(itemIDs402[i])
        for key, value in apiResponse402Json["Response"]["sales"]["data"].items():
            if key in currentAvailableItems:
                IDtoArmorHashDict[key]=value.get("itemHash")
                
        #look through currentAvailableItems for armor peices hash and then see if the hash relates to armor or not
        for i in range(len(currentAvailableItems)):
            hashData = await self.decodeHash(IDtoArmorHashDict[currentAvailableItems[i]],"DestinyInventoryItemDefinition")

            
            #it is armor   
            if hashData.get("itemType") == 2:
                currentAvailableArmorItems.append(currentAvailableItems[i])

        #now get rid of the exotics for the other class
        removalIDS = []
        for i in range(len(currentAvailableArmorItems)):
            hashData = await self.decodeHash(IDtoArmorHashDict[currentAvailableArmorItems[i]],"DestinyInventoryItemDefinition")

            #titan
            if hashData.get("classType") == 0:
                if(classType != "titan"):
                    removalIDS.append(currentAvailableArmorItems[i])
            #hunter
            if hashData.get("classType") == 1:
                if(classType != "hunter"):
                    removalIDS.append(currentAvailableArmorItems[i])
            #warlock
            if hashData.get("classType") == 2:
                if(classType != "warlock"):
                    removalIDS.append(currentAvailableArmorItems[i])



        for i in range(len(removalIDS)):
            currentAvailableArmorItems.remove(removalIDS[i])

        

        #now get each individual armors perks


        
        for item in currentAvailableArmorItems:
            

            #total, mobility, resilince , recovery ,discipline, intelect, strength
            statsList = [0,0,0,0,0,0,0]
            statTotal = 0
            isExoticBool = False
            statDict = socketStatDict[item]["stats"]
            print(socketStatDict[item]["stats"])
            print(item)
            for key, val in statDict.items():
                statTotal += val.get("value")
                statTypeStr = self.decodeStatHash(int(key))
                
                if statTypeStr == "Intellect":
                    statsList[5] = int(val.get("value"))
                if statTypeStr == "Resilience":
                    statsList[2] = int(val.get("value"))
                if statTypeStr == "Discipline":
                    statsList[4] = int(val.get("value"))
                if statTypeStr == "Recovery":
                    statsList[3] = int(val.get("value"))
                if statTypeStr == "Mobility":
                    statsList[1] = int(val.get("value"))
                if statTypeStr == "Strength":
                    statsList[6] = int(val.get("value"))
            statsList[0] = statTotal
            print(statsList)






            exArmorPerk = None

            print("[ID]   ",item)
            print("[HASH] ",IDtoArmorHashDict[item])
            stats = apiResponse304Json["Response"]["itemComponents"]["stats"]["data"].get(item)
            armorData = await self.decodeHash(IDtoArmorHashDict[item],"DestinyInventoryItemDefinition")
            print(stats)
            print(armorData)
            

            #check if its an exotic armorpeice
            if(armorData["inventory"].get("tierTypeName") == "Exotic"):
                #socketTypeHash:965959289
                for key in armorData["sockets"]["socketEntries"]:
                    print(key)
                    print(key.get("socketTypeHash"))
                    try:
                        armorSocketHash = await self.decodeHash(key.get("singleInitialItemHash"),"DestinyInventoryItemDefinition")
                        print(armorSocketHash["displayProperties"].get("name")) 
                    except Exception as e:
                        print(e)
                        continue


                    if(armorSocketHash.get("itemTypeDisplayName") == "Intrinsic" or armorSocketHash.get("itemTypeDisplayName") == "Aeon Cult Mod"):
                        
                        exPerkHashed = await self.decodeHash(key.get("singleInitialItemHash"),"DestinyInventoryItemDefinition")
                        isExoticBool = True
                        exArmorPerk = {
                            "name": exPerkHashed["displayProperties"].get("name"),
                            "icon": "https://www.bungie.net"+str(exPerkHashed["displayProperties"].get("icon")),
                            "desc": exPerkHashed["displayProperties"].get("description")
                        },
                
            loreHash = armorData.get("loreHash")
            if(loreHash == None):
                armorLore = None
            else:
                armorLore = await self.decodeHash(str(loreHash),"DestinyLoreDefinition")
                armorLore = armorLore["displayProperties"].get("description")

            try:
                print("[HASH] ",IDtoArmorHashDict[item])
                
                armorType = armorData["itemTypeDisplayName"]
                
                

                jsonTemplate = {
                    "name":armorData["displayProperties"].get("name"),
                    "type":armorData.get("itemTypeAndTierDisplayName"),
                    "description":armorData["displayProperties"].get("description"),
                    "lore":armorData.get("flavorText"),
                    "ExtLore":armorLore,
                    "itemHash":str(IDtoArmorHashDict[item]),
                    "itemRating":None,
                    "icon":"https://www.bungie.net"+str(armorData["displayProperties"].get("icon")),
                    "backgroundImage" : "https://www.bungie.net"+str(armorData.get("screenshot")),
                    "rarity":armorData["inventory"].get("tierTypeName"),
                    "class":armorData.get("classType"), 
                    "statRolls":statsList,
                    "weaponPerks":[],
                    "exoticArmorPerk":exArmorPerk,
                    "legendWeaponFrame":None,
                    "legendWeaponDamageType":None,
                    "legendWeaponDamageElement":None,
                    "masterworkData":None,
                }
            except KeyError:
                pass

            #store values
            if(classType == "warlock"):
                if(isExoticBool):
                    self.WarlockExotic = jsonTemplate
                
            if(classType == "hunter"):
                if(isExoticBool):
                    self.HunterExotic = jsonTemplate
                
            if(classType == "titan"):
                if(isExoticBool):
                    self.TitanExotic = jsonTemplate

    #get legendary armor from the strange gear offers vendor
    async def getLegendaryArmor(self,classID,classType):
        #armor stat template
        IDtoArmorHashDict = {}
        socketStatDict = {}
        itemIDs402 = []
        socketIDs305 = []
        currentAvailableItems = []
        currentAvailableArmorItems = []
        
        #item sockets
        apiUrl304 = self.destinyURLBase + f"/Destiny2/{self.membershipType}/Profile/{self.membershipId}/Character/{classID}/Vendors/{self.strangeGearVendorHash}/?components=304"
        apiResponse304 = self.get_api_request(apiUrl304)
        apiResponse304Json = json.loads(apiResponse304)

        #item ids
        apiUrl402 = self.destinyURLBase + f"/Destiny2/{self.membershipType}/Profile/{self.membershipId}/Character/{classID}/Vendors/{self.strangeGearVendorHash}/?components=402"
        apiResponse402 = self.get_api_request(apiUrl402)
        apiResponse402Json = json.loads(apiResponse402)
        
        for itemID, itemIDData in apiResponse402Json["Response"]["sales"]["data"].items():
            itemIDs402.append(itemID)
            
        
        for socketID, socketIDData in apiResponse304Json["Response"]["itemComponents"]["stats"]["data"].items():
            socketIDs305.append(socketID)
            socketStatDict[socketID]=socketIDData
            
        for i in range(len(itemIDs402)):
            if itemIDs402[i] in socketIDs305:
                currentAvailableItems.append(itemIDs402[i])
        for key, value in apiResponse402Json["Response"]["sales"]["data"].items():
            if key in currentAvailableItems:
                IDtoArmorHashDict[key]=value.get("itemHash")
                
        #look through currentAvailableItems for armor peices hash and then see if the hash relates to armor or not
        for i in range(len(currentAvailableItems)):
            hashData = await self.decodeHash(IDtoArmorHashDict[currentAvailableItems[i]],"DestinyInventoryItemDefinition")
            #it is armor   
            if hashData.get("itemType") == 2:
                currentAvailableArmorItems.append(currentAvailableItems[i])

        #now get rid of the exotics for the other class
        removalIDS = []
        for i in range(len(currentAvailableArmorItems)):
            hashData = await self.decodeHash(IDtoArmorHashDict[currentAvailableArmorItems[i]],"DestinyInventoryItemDefinition")

            #titan
            if hashData.get("classType") == 0:
                if(classType != "titan"):
                    removalIDS.append(currentAvailableArmorItems[i])
            #hunter
            if hashData.get("classType") == 1:
                if(classType != "hunter"):
                    removalIDS.append(currentAvailableArmorItems[i])
            #warlock
            if hashData.get("classType") == 2:
                if(classType != "warlock"):
                    removalIDS.append(currentAvailableArmorItems[i])



        for i in range(len(removalIDS)):
            currentAvailableArmorItems.remove(removalIDS[i])

        

        #now get each individual armors perks
        for item in currentAvailableArmorItems:
            

            #total, mobility, resilince , recovery ,discipline, intelect, strength
            statsList = [0,0,0,0,0,0,0]
            statTotal = 0
            isExoticBool = False
            statDict = socketStatDict[item]["stats"]
            print(socketStatDict[item]["stats"])
            print(item)
            for key, val in statDict.items():
                statTotal += val.get("value")
                statTypeStr = self.decodeStatHash(int(key))
                
                if statTypeStr == "Intellect":
                    statsList[5] = int(val.get("value"))
                if statTypeStr == "Resilience":
                    statsList[2] = int(val.get("value"))
                if statTypeStr == "Discipline":
                    statsList[4] = int(val.get("value"))
                if statTypeStr == "Recovery":
                    statsList[3] = int(val.get("value"))
                if statTypeStr == "Mobility":
                    statsList[1] = int(val.get("value"))
                if statTypeStr == "Strength":
                    statsList[6] = int(val.get("value"))
            statsList[0] = statTotal
            print(statsList)

            exArmorPerk = None

            print("[ID]   ",item)
            print("[HASH] ",IDtoArmorHashDict[item])
            stats = apiResponse304Json["Response"]["itemComponents"]["stats"]["data"].get(item)
            armorData = await self.decodeHash(IDtoArmorHashDict[item],"DestinyInventoryItemDefinition")
            print(stats)
            print(armorData)
            
            loreHash = armorData.get("loreHash")
            if(loreHash == None):
                armorLore = None
            else:
                armorLore = await self.decodeHash(str(loreHash),"DestinyLoreDefinition")
                armorLore = armorLore["displayProperties"].get("description")

            try:
                print("[HASH] ",IDtoArmorHashDict[item])
                
                armorType = armorData["itemTypeDisplayName"]
                
                

                jsonTemplate = {
                    "name":armorData["displayProperties"].get("name"),
                    "type":armorData.get("itemTypeAndTierDisplayName"),
                    "description":armorData["displayProperties"].get("description"),
                    "lore":armorData.get("flavorText"),
                    "ExtLore":armorLore,
                    "itemHash":str(IDtoArmorHashDict[item]),
                    "itemRating":None,
                    "icon":"https://www.bungie.net"+str(armorData["displayProperties"].get("icon")),
                    "backgroundImage" : "https://www.bungie.net"+str(armorData.get("screenshot")),
                    "rarity":armorData["inventory"].get("tierTypeName"),
                    "class":armorData.get("classType"), 
                    "statRolls":statsList,
                    "weaponPerks":[],
                    "exoticArmorPerk":exArmorPerk,
                    "legendWeaponFrame":None,
                    "legendWeaponDamageType":None,
                    "legendWeaponDamageElement":None,
                    "masterworkData":None,
                }
            except KeyError:
                pass

            #store values
            if(classType == "warlock"):
                if(armorType == "Helmet" and jsonTemplate["rarity"] != "Exotic"):
                    self.WarlockHelmet = jsonTemplate
                if(armorType == "Gauntlets" and jsonTemplate["rarity"] != "Exotic"):
                    self.WarlockArms = jsonTemplate
                if(armorType == "Chest Armor" and jsonTemplate["rarity"] != "Exotic"):
                    self.WarlockChest = jsonTemplate
                if(armorType == "Leg Armor" and jsonTemplate["rarity"] != "Exotic"):
                    self.WarlockLegs = jsonTemplate                    
                if(armorType == "Warlock Bond" and jsonTemplate["rarity"] != "Exotic"):
                    self.WarlockClassItem = jsonTemplate
            if(classType == "hunter"):
                if(armorType == "Helmet" and jsonTemplate["rarity"] != "Exotic"):
                    self.HunterHelmet = jsonTemplate
                if(armorType == "Gauntlets" and jsonTemplate["rarity"] != "Exotic"):
                    self.HunterArms = jsonTemplate 
                if(armorType == "Chest Armor" and jsonTemplate["rarity"] != "Exotic"):
                    self.HunterChest = jsonTemplate
                if(armorType == "Leg Armor" and jsonTemplate["rarity"] != "Exotic"):
                    self.HunterLegs = jsonTemplate
                if(armorType == "Hunter Cloak" and jsonTemplate["rarity"] != "Exotic"):
                    self.HunterClassItem = jsonTemplate
            if(classType == "titan"):
                if(armorType == "Helmet" and jsonTemplate["rarity"] != "Exotic"):
                    self.TitanHelmet = jsonTemplate
                if(armorType == "Gauntlets" and jsonTemplate["rarity"] != "Exotic"):
                    self.TitanArms = jsonTemplate
                if(armorType == "Chest Armor" and jsonTemplate["rarity"] != "Exotic"):
                    self.TitanChest = jsonTemplate       
                if(armorType == "Leg Armor" and jsonTemplate["rarity"] != "Exotic"):
                    self.TitanLegs = jsonTemplate
                if(armorType == "Titan Mark" and jsonTemplate["rarity"] != "Exotic"):
                    self.TitanClassItem = jsonTemplate

    async def getExoticCatalysts(self):

        exoticCatalysts = []

        apiUrl308 = self.destinyURLBase + f"/Destiny2/{self.membershipType}/Profile/{self.membershipId}/Character/{characterIDWarlock}/Vendors/{self.vendorHash}/?components=308"
        apiResponse308 = self.get_api_request(apiUrl308)
        apiResponse308Json = json.loads(apiResponse308)

        for itemID, itemIDData in apiResponse308Json["Response"]["itemComponents"]["plugStates"]["data"].items():
            if len(exoticCatalysts) > 2:
                break
            
            hashedData = await self.decodeHash(itemIDData.get("plugItemHash"),"DestinyInventoryItemDefinition")
            if(hashedData.get('traitIds') == ['item.exotic_catalyst']):
               
                catalystPerks = []

                #get perks of the catalyst
                for perk in hashedData.get("perks"):
                    hashedPerkData = await self.decodeHash(perk.get("perkHash"),"DestinySandboxPerkDefinition")
                    if(hashedPerkData["displayProperties"].get("hasIcon")):
                        
                        print(hashedPerkData["displayProperties"].get("name"))

                        perkTemplate = {
                            "name":hashedPerkData["displayProperties"].get("name"),
                            "type":"Exotic Catalyst Perk",
                            "description":hashedPerkData["displayProperties"].get("description"),
                            "itemHash":perk.get("perkHash"),
                            "icon":"https://www.bungie.net"+str(hashedPerkData["displayProperties"].get("icon")),
                            
                        }

                        catalystPerks.append(perkTemplate)


                jsonTemplate = {
                    "name":hashedData["displayProperties"].get("name"),
                    "type":"Exotic Catalyst",
                    "description":hashedData["displayProperties"].get("description"),
                    "itemHash":str(itemIDData.get("plugItemHash")),
                    "icon":"https://www.bungie.net"+str(hashedData["displayProperties"].get("icon")),
                    "rarity":hashedData["inventory"].get("tierTypeName"),
                    "catalyst perks":catalystPerks
                }
            

                

                exoticCatalysts.append(jsonTemplate)
        self.FirstCatalyst = exoticCatalysts[0]
        self.SecondCatalyst = exoticCatalysts[1]

    async def getXurStrangeGearOffers(self):
        return None
   


    #determines if an item already exists in the json before its added
    def jsonConflictCheck(self,jsonToTest):
        
        
        for i in range(len(self.XursInventoryItems)):
            if(self.XursInventoryItems[i]["itemHash"] == jsonToTest["itemHash"] and (self.XursInventoryItems[i]["class"] == jsonToTest["class"] and jsonToTest["class"] != 3)):
                return True
        return False


    #check for missing mw's
    async def masterWorkCheck(self):
        print(self.LegendaryWeapons)
        for weapon in self.LegendaryWeapons:
            if(weapon["masterworkData"] == None):
                print("No mw found!")
                apiUrl402 = self.destinyURLBase + f"/Destiny2/{self.membershipType}/Profile/{self.membershipId}/Character/{characterIDWarlock}/Vendors/{self.strangeGearVendorHash}/?components=402"
                apiResponse402 = self.get_api_request(apiUrl402)
                apiResponse402Json = json.loads(apiResponse402)
                
                for key, value in apiResponse402Json["Response"]["sales"]["data"].items():
                    
                    if(value["itemHash"] == int(weapon["itemHash"])):
                        
                        hashedValData = await self.decodeHash(value["itemHash"],"DestinyInventoryItemDefinition")
                        
                        weaponSockets = hashedValData["sockets"].get("socketEntries")
                        for socket in weaponSockets:
                            print(socket.get("singleInitialItemHash"))
                            print(socket)
                            try:
                                socketData = await self.decodeHash(socket.get("singleInitialItemHash"),"DestinyInventoryItemDefinition")
                            except Exception as e:
                                print(f"error: {e}, moving onto next perk..")
                                continue
                            if "masterworks" in socketData["plug"].get("plugCategoryIdentifier") and str(socketData.get("hash")) != "905869860":
                                print(socketData)
                                try: 
                                    name = socketData["displayProperties"].get("name").split(": ")[1]
                                    description = socketData["displayProperties"].get("name").split(": ")[1]
                                    icon = "https://www.bungie.net" + str(socketData["displayProperties"].get("icon"))
                                    masterworkHash = socketData.get("hash")
                                except IndexError as e:
                                    print(f"index error: {e}")
                                    name = "Unknown Masterwork"
                                    description = "This master work could not be found, perhaps it does not exist?"
                                    icon = "https://www.bungie.net/common/destiny2_content/icons/cc3be955cb34b918e90d0f8e654a11c1.png"
                                    masterworkHash = "231101171"

                                
                                masterworkTemplate = {
                                    
                                    "name":name,
                                    "description":description,
                                    "icon":icon,
                                    "mwHash":masterworkHash,
                                }
                                weapon["masterworkData"] = masterworkTemplate
                        




    async def getMaterialOffers(self):


        #get the one item from xurs main inventory first
        apiUrl402 = self.destinyURLBase + f"/Destiny2/{self.membershipType}/Profile/{self.membershipId}/Character/{characterIDWarlock}/Vendors/{self.vendorHash}/?components=402"
        apiResponse402 = self.get_api_request(apiUrl402)
        apiResponse402Json = json.loads(apiResponse402)

        for itemID, itemIDData in apiResponse402Json["Response"]["sales"]["data"].items():
            hashedData = await self.decodeHash(itemIDData.get("itemHash"),"DestinyInventoryItemDefinition")
            if itemIDData.get("itemHash") in self.multivariousOfferableItems:
                
                hashedData = await self.decodeHash(itemIDData.get("itemHash"),"DestinyInventoryItemDefinition")

                

                itemTemplate = {
                    "name":hashedData["displayProperties"].get("name"),
                    "icon":"https://www.bungie.net" + str(hashedData["displayProperties"].get("icon")),
                    "description":hashedData["displayProperties"].get("description"),
                    "count":itemIDData.get("quantity"),
                    "cost":itemIDData["costs"][0].get("quantity"),
                    "lowest price":lowest_prices[itemIDData.get("itemHash")].get(itemIDData.get("quantity")),
                    "is lowest": bool(lowest_prices[itemIDData.get("itemHash")].get(itemIDData.get("quantity")) == itemIDData["costs"][0].get("quantity")),
                    "hash":itemIDData.get("itemHash"),
                    
                }

                
                self.MaterialOffers.append(itemTemplate)
                break
                
            if itemIDData.get("itemHash") in self.miscItemHashes:
                
                hashedData = await self.decodeHash(itemIDData.get("itemHash"),"DestinyInventoryItemDefinition")

                if hashedData.get("loreHash"):
                    lore =  await self.decodeHash(hashedData.get("loreHash"),"DestinyLoreDefinition")
                
                if hashedData["displayProperties"].get("description"):
                    desc = hashedData["displayProperties"].get("description")
                else:
                    desc = hashedData.get("flavorText")
                
                


                itemTemplate = {
                    "name":hashedData["displayProperties"].get("name"),
                    "icon":"https://www.bungie.net" + str(hashedData["displayProperties"].get("icon")),
                    "description":desc,
                    "backgroundImage":"https://www.bungie.net"+str(hashedData.get("screenshot")),
                    "type":hashedData.get("itemTypeDisplayName"),
                    "lore":lore["displayProperties"].get("description"),
                    "hash":hashedData.get("hash"),
                    
                }

                
                self.MiscOffers.append(itemTemplate)
                break
        
        
        #now get the other items from the actual tab inside his menu

        #get the one item from xurs main inventory first
        apiUrl402 = self.destinyURLBase + f"/Destiny2/{self.membershipType}/Profile/{self.membershipId}/Character/{characterIDWarlock}/Vendors/{self.strangeMaterialVendorHash}/?components=402"
        apiResponse402 = self.get_api_request(apiUrl402)
        apiResponse402Json = json.loads(apiResponse402)

        for itemID, itemIDData in apiResponse402Json["Response"]["sales"]["data"].items():
            if itemIDData.get("itemHash") not in self.excludeableMaterialHashes:
                print(itemID,itemIDData.get("itemHash"))

                hashedData = await self.decodeHash(itemIDData.get("itemHash"),"DestinyInventoryItemDefinition")

                try: 
                    cost = itemIDData["costs"][0].get("quantity")
                except:
                    cost = 0
                    
                
                try: 
                    lowest_price = lowest_prices[itemIDData.get("itemHash")].get(itemIDData.get("quantity"))
                except:
                    lowest_price = 0

                try:
                    is_lowest_price = bool((lowest_price) == itemIDData["costs"][0].get("quantity"))
                except:
                    is_lowest_price = True
                
                

                
                itemTemplate = {
                    "name":hashedData["displayProperties"].get("name"),
                    "icon":"https://www.bungie.net" + str(hashedData["displayProperties"].get("icon")),
                    "description":hashedData["displayProperties"].get("description"),
                    "count":itemIDData.get("quantity"),
                    "cost":cost,
                    "lowest price":lowest_price,
                    "is lowest": is_lowest_price,
                    "hash":itemIDData.get("itemHash"),
                }

                
                self.MaterialOffers.append(itemTemplate)


        
        self.MaterialOffers.sort(key=lambda item: item['name'])
        
        
    async def checkForArtifice(self):
        #get the one item from xurs main inventory first
        apiUrl401 = self.destinyURLBase + f"/Destiny2/{self.membershipType}/Profile/{self.membershipId}/Character/{characterIDHunter}/Vendors/{self.vendorHash}/?components=401"
        apiResponse401 = self.get_api_request(apiUrl401)
        apiResponse401Json = json.loads(apiResponse401)

        apiUrl402 = self.destinyURLBase + f"/Destiny2/{self.membershipType}/Profile/{self.membershipId}/Character/{characterIDHunter}/Vendors/{self.vendorHash}/?components=402"
        apiResponse402 = self.get_api_request(apiUrl402)
        apiResponse402Json = json.loads(apiResponse402)

        for item in apiResponse401Json["Response"]["categories"]["data"]["categories"]:
            
            
            for id in item.get('itemIndexes')[::-1]:

                hashedData = await self.decodeHash(apiResponse402Json["Response"]["sales"]["data"][str(id)].get("itemHash"),"DestinyInventoryItemDefinition")
                
                if hashedData["itemType"] == 2 and hashedData["equippingBlock"].get("uniqueLabelHash") != 761097285:
                    
                    #there is artifice armor 
                    self.ArtificePresent = True
                    return True

       

    async def getArtificeArmor(self,classID,classType):

        
        socketStatDict = {}
        

        artificeHash = None
        artificeID = None

        #item sockets
        apiUrl304 = self.destinyURLBase + f"/Destiny2/{self.membershipType}/Profile/{self.membershipId}/Character/{classID}/Vendors/{self.vendorHash}/?components=304"
        apiResponse304 = self.get_api_request(apiUrl304)
        apiResponse304Json = json.loads(apiResponse304)
        
        apiUrl401 = self.destinyURLBase + f"/Destiny2/{self.membershipType}/Profile/{self.membershipId}/Character/{classID}/Vendors/{self.vendorHash}/?components=401"
        apiResponse401 = self.get_api_request(apiUrl401)
        apiResponse401Json = json.loads(apiResponse401)

        apiUrl402 = self.destinyURLBase + f"/Destiny2/{self.membershipType}/Profile/{self.membershipId}/Character/{classID}/Vendors/{self.vendorHash}/?components=402"
        apiResponse402 = self.get_api_request(apiUrl402)
        apiResponse402Json = json.loads(apiResponse402)

        for item in apiResponse401Json["Response"]["categories"]["data"]["categories"]:
            if artificeHash:
                break
            for id in item.get('itemIndexes')[::-1]:
                hashedData = await self.decodeHash(apiResponse402Json["Response"]["sales"]["data"][str(id)].get("itemHash"),"DestinyInventoryItemDefinition")
                if hashedData["itemType"] == 2 and hashedData["equippingBlock"].get("uniqueLabelHash") != 761097285:
                    
                    #there is artifice armor 
                    artificeHash = apiResponse402Json["Response"]["sales"]["data"][str(id)].get("itemHash")
                    artificeID = id
                    break
                
        
        socketStatDict = apiResponse304Json["Response"]["itemComponents"]["stats"]["data"][str(artificeID)]
        
        
        hashData = await self.decodeHash(artificeHash,"DestinyInventoryItemDefinition")
        
        #total, mobility, resilince , recovery ,discipline, intelect, strength
        statsList = [0,0,0,0,0,0,0]
        statTotal = 0
        statDict = socketStatDict["stats"]
        
        
        for key, val in statDict.items():
            statTotal += val.get("value")
            statTypeStr = self.decodeStatHash(int(key))
            
            if statTypeStr == "Intellect":
                statsList[5] = int(val.get("value"))
            if statTypeStr == "Resilience":
                statsList[2] = int(val.get("value"))
            if statTypeStr == "Discipline":
                statsList[4] = int(val.get("value"))
            if statTypeStr == "Recovery":
                statsList[3] = int(val.get("value"))
            if statTypeStr == "Mobility":
                statsList[1] = int(val.get("value"))
            if statTypeStr == "Strength":
                statsList[6] = int(val.get("value"))
        statsList[0] = statTotal

       
        stats = apiResponse304Json["Response"]["itemComponents"]["stats"]["data"].get(artificeID)
        armorData = await self.decodeHash(artificeHash,"DestinyInventoryItemDefinition")
        
        loreHash = armorData.get("loreHash")
        if(loreHash == None):
            armorLore = None
        else:
            armorLore = await self.decodeHash(str(loreHash),"DestinyLoreDefinition")
            armorLore = armorLore["displayProperties"].get("description")

        try:
           
            
            armorType = armorData["itemTypeDisplayName"]
            
            

            jsonTemplate = {
                "name":armorData["displayProperties"].get("name"),
                "type":armorData.get("itemTypeAndTierDisplayName"),
                "description":armorData["displayProperties"].get("description"),
                "lore":armorData.get("flavorText"),
                "ExtLore":armorLore,
                "itemHash":str(artificeHash),
                "itemRating":None,
                "icon":"https://www.bungie.net"+str(armorData["displayProperties"].get("icon")),
                "backgroundImage" : "https://www.bungie.net"+str(armorData.get("screenshot")),
                "rarity":armorData["inventory"].get("tierTypeName"),
                "class":armorData.get("classType"), 
                "statRolls":statsList,
                "isArtifice":True,
                
            }
        except KeyError:
            pass

        
        #store values
        if(classType == "warlock"):
            self.ArtificeArmor[1] = jsonTemplate
        if(classType == "hunter"):
            self.ArtificeArmor[0] = jsonTemplate
        if(classType == "titan"):
            self.ArtificeArmor[2] = jsonTemplate

    #decode the hash from the manifest
    async def decodeHash(self,hash,manifestValue):
        hashedData = await self.destiny.decode_hash(hash,manifestValue)
        return hashedData




    #Make an GET request to api and return json
    def get_api_request(self, url):
        try:

                #get api request
                res = requests.get(url, headers=HEADERS)
                
                #parse to json
                jsonResponse = json.dumps(res.json(), sort_keys=True, indent=4)
                
                
                #store json response
                #self.apiResponseJson = jsonResponse
        except aiohttp.client_exceptions.ClientResponseError as e:
            print("ERROR: Could not connect to Bungie.net Endpoint")

        return jsonResponse
    #grab xurs inventory data from the endpoint
    #https://bungie-net.github.io/multi/schema_Destiny-Definitions-DestinyInventoryItemDefinition.html#schema_Destiny-Definitions-DestinyInventoryItemDefinition
    
    async def getXurInventory(self,charID):
        
        if await self.checkForArtifice():
            await self.getArtificeArmor(self.warlockCharacterID,"warlock")
            await self.getArtificeArmor(self.hunterCharacterID,"hunter")
            await self.getArtificeArmor(self.titanCharacterID,"titan")
        
        #do this first before everything
        apiUrl = self.destinyURLBase + f"/Destiny2/{self.membershipType}/Profile/{self.membershipId}/Character/{charID}/Vendors/{self.vendorHash}/?components=402"        #format url data
        self.apiResponse = self.get_api_request(apiUrl)

        #store into a dict
        self.apiResponseJson = json.loads(self.apiResponse)
        
        print(self.apiResponseJson)
            
        #print(self.apiResponseJson)


        #store perk info
        apiUrl305 = self.destinyURLBase + f"/Destiny2/{self.membershipType}/Profile/{self.membershipId}/Character/{characterIDWarlock}/Vendors/{self.strangeGearVendorHash}/?components=305"
        apiResponse305 = self.get_api_request(apiUrl305)
    
        apiUrl310 = self.destinyURLBase + f"/Destiny2/{self.membershipType}/Profile/{self.membershipId}/Character/{characterIDWarlock}/Vendors/{self.strangeGearVendorHash}/?components=310"
        apiResponse310 = self.get_api_request(apiUrl310)
        
        self.combinedPerksJson = self.socketPlugs(apiResponse305,apiResponse310)

        print(self.combinedPerksJson)
        #input("\n")
        #store the inventory of for sale items to be parsed 
        self.forSaleItems = self.apiResponseJson["Response"]["sales"]["data"]
        await self.getExoticArmor(self.warlockCharacterID,"warlock")
        await self.getExoticArmor(self.hunterCharacterID,"hunter")
        await self.getExoticArmor(self.titanCharacterID,"titan")
    
        await self.getLegendaryArmor(self.warlockCharacterID,"warlock")
        await self.getLegendaryArmor(self.hunterCharacterID,"hunter")
        await self.getLegendaryArmor(self.titanCharacterID,"titan")
        
        await self.getWeapons()
        await self.getExoticCatalysts()

        await self.getMaterialOffers()

        await self.bindJsonData()
        await self.masterWorkCheck()
        

        print(self.weaponPerksTemplateList)

        print(self.weaponsTemplatesList)

        self.buildJSON(True)
        #close loop
        await self.destiny.close()

#main loop

def mainloop():
    #create and set new loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    #init class
    XI = main(API_KEY)
    loop.run_until_complete(XI.getXurInventory(characterIDWarlock))

mainloop()
