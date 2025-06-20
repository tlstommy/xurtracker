#functions for armor handling

from destiny_api import get_api_request, decode_hash
from utils import decode_stat_hash

import requests,json,aiohttp,asyncio


async def get_exotic_armor(destiny,class_id,class_type):
    #armor stat template
        IDtoArmorHashDict = {}
        socketStatDict = {}
        itemIDs402 = []
        socketIDs305 = []
        currentAvailableItems = []
        currentAvailableArmorItems = []
        
        #item sockets
        apiUrl304 = destiny.destinyURLBase + f"/Destiny2/{destiny.membershipType}/Profile/{destiny.membershipId}/Character/{class_id}/Vendors/{destiny.vendorHash}/?components=304"
        apiResponse304 = get_api_request(apiUrl304)
        apiResponse304Json = json.loads(apiResponse304)

        #item ids
        apiUrl402 = destiny.destinyURLBase + f"/Destiny2/{destiny.membershipType}/Profile/{destiny.membershipId}/Character/{class_id}/Vendors/{destiny.vendorHash}/?components=402"
        apiResponse402 = get_api_request(apiUrl402)
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
            hashData = await decode_hash(destiny,IDtoArmorHashDict[currentAvailableItems[i]],"DestinyInventoryItemDefinition")

            
            #it is armor   
            if hashData.get("itemType") == 2:
                currentAvailableArmorItems.append(currentAvailableItems[i])

        #now get rid of the exotics for the other class
        removalIDS = []
        for i in range(len(currentAvailableArmorItems)):
            hashData = await decode_hash(destiny,IDtoArmorHashDict[currentAvailableArmorItems[i]],"DestinyInventoryItemDefinition")

            #titan
            if hashData.get("classType") == 0:
                if(class_type != "titan"):
                    removalIDS.append(currentAvailableArmorItems[i])
            #hunter
            if hashData.get("classType") == 1:
                if(class_type != "hunter"):
                    removalIDS.append(currentAvailableArmorItems[i])
            #warlock
            if hashData.get("classType") == 2:
                if(class_type != "warlock"):
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
            
            for key, val in statDict.items():
                statTotal += val.get("value")
                statTypeStr = decode_stat_hash(int(key))
                
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
            armorData = await decode_hash(destiny,IDtoArmorHashDict[item],"DestinyInventoryItemDefinition")
            print(stats)
            print(armorData)
            

            #check if its an exotic armorpeice
            if(armorData["inventory"].get("tierTypeName") == "Exotic"):
                #socketTypeHash:965959289
                for key in armorData["sockets"]["socketEntries"]:
                    print(key)
                    print(key.get("socketTypeHash"))
                    try:
                        armorSocketHash = await decode_hash(destiny,key.get("singleInitialItemHash"),"DestinyInventoryItemDefinition")
                        print(armorSocketHash["displayProperties"].get("name")) 
                    except Exception as e:
                        print(e)
                        continue


                    if(armorSocketHash.get("itemTypeDisplayName") == "Intrinsic" or armorSocketHash.get("itemTypeDisplayName") == "Aeon Cult Mod"):
                        
                        exPerkHashed = await decode_hash(destiny,key.get("singleInitialItemHash"),"DestinyInventoryItemDefinition")
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
                armorLore = await decode_hash(destiny,str(loreHash),"DestinyLoreDefinition")
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
            if(class_type == "warlock"):
                if(isExoticBool):
                    destiny.WarlockExotic = jsonTemplate
                
            if(class_type == "hunter"):
                if(isExoticBool):
                    destiny.HunterExotic = jsonTemplate
                
            if(class_type == "titan"):
                if(isExoticBool):
                    destiny.TitanExotic = jsonTemplate







async def get_legendary_armor(destiny, class_id, class_type):
    #armor stat template
        IDtoArmorHashDict = {}
        socketStatDict = {}
        itemIDs402 = []
        socketIDs305 = []
        currentAvailableItems = []
        currentAvailableArmorItems = []
        
        #item sockets
        apiUrl304 = destiny.destinyURLBase + f"/Destiny2/{destiny.membershipType}/Profile/{destiny.membershipId}/Character/{class_id}/Vendors/{destiny.strangeGearVendorHash}/?components=304"
        apiResponse304 = get_api_request(apiUrl304)
        apiResponse304Json = json.loads(apiResponse304)

        #item ids
        apiUrl402 = destiny.destinyURLBase + f"/Destiny2/{destiny.membershipType}/Profile/{destiny.membershipId}/Character/{class_id}/Vendors/{destiny.strangeGearVendorHash}/?components=402"
        apiResponse402 = get_api_request(apiUrl402)
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
            hashData = await decode_hash(destiny,IDtoArmorHashDict[currentAvailableItems[i]],"DestinyInventoryItemDefinition")
            #it is armor   
            if hashData.get("itemType") == 2:
                currentAvailableArmorItems.append(currentAvailableItems[i])

        #now get rid of the exotics for the other class
        removalIDS = []
        for i in range(len(currentAvailableArmorItems)):
            hashData = await decode_hash(destiny,IDtoArmorHashDict[currentAvailableArmorItems[i]],"DestinyInventoryItemDefinition")

            #titan
            if hashData.get("classType") == 0:
                if(class_type!= "titan"):
                    removalIDS.append(currentAvailableArmorItems[i])
            #hunter
            if hashData.get("classType") == 1:
                if(class_type!= "hunter"):
                    removalIDS.append(currentAvailableArmorItems[i])
            #warlock
            if hashData.get("classType") == 2:
                if(class_type!= "warlock"):
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
                statTypeStr = decode_stat_hash(int(key))
                
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
            armorData = await decode_hash(destiny,IDtoArmorHashDict[item],"DestinyInventoryItemDefinition")
            print(stats)
            print(armorData)
            
            loreHash = armorData.get("loreHash")
            if(loreHash == None):
                armorLore = None
            else:
                armorLore = await decode_hash(destiny,str(loreHash),"DestinyLoreDefinition")
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
            if(class_type== "warlock"):
                if(armorType == "Helmet" and jsonTemplate["rarity"] != "Exotic"):
                    destiny.WarlockHelmet = jsonTemplate
                if(armorType == "Gauntlets" and jsonTemplate["rarity"] != "Exotic"):
                    destiny.WarlockArms = jsonTemplate
                if(armorType == "Chest Armor" and jsonTemplate["rarity"] != "Exotic"):
                    destiny.WarlockChest = jsonTemplate
                if(armorType == "Leg Armor" and jsonTemplate["rarity"] != "Exotic"):
                    destiny.WarlockLegs = jsonTemplate                    
                if(armorType == "Warlock Bond" and jsonTemplate["rarity"] != "Exotic"):
                    destiny.WarlockClassItem = jsonTemplate
            if(class_type== "hunter"):
                if(armorType == "Helmet" and jsonTemplate["rarity"] != "Exotic"):
                    destiny.HunterHelmet = jsonTemplate
                if(armorType == "Gauntlets" and jsonTemplate["rarity"] != "Exotic"):
                    destiny.HunterArms = jsonTemplate 
                if(armorType == "Chest Armor" and jsonTemplate["rarity"] != "Exotic"):
                    destiny.HunterChest = jsonTemplate
                if(armorType == "Leg Armor" and jsonTemplate["rarity"] != "Exotic"):
                    destiny.HunterLegs = jsonTemplate
                if(armorType == "Hunter Cloak" and jsonTemplate["rarity"] != "Exotic"):
                    destiny.HunterClassItem = jsonTemplate
            if(class_type== "titan"):
                if(armorType == "Helmet" and jsonTemplate["rarity"] != "Exotic"):
                    destiny.TitanHelmet = jsonTemplate
                if(armorType == "Gauntlets" and jsonTemplate["rarity"] != "Exotic"):
                    destiny.TitanArms = jsonTemplate
                if(armorType == "Chest Armor" and jsonTemplate["rarity"] != "Exotic"):
                    destiny.TitanChest = jsonTemplate       
                if(armorType == "Leg Armor" and jsonTemplate["rarity"] != "Exotic"):
                    destiny.TitanLegs = jsonTemplate
                if(armorType == "Titan Mark" and jsonTemplate["rarity"] != "Exotic"):
                    destiny.TitanClassItem = jsonTemplate



async def get_artifice_armor(destiny, class_id, class_type):
    socketStatDict = {}
        

    artificeHash = None
    artificeID = None

    #item sockets
    apiUrl304 = destiny.destinyURLBase + f"/Destiny2/{destiny.membershipType}/Profile/{destiny.membershipId}/Character/{class_id}/Vendors/{destiny.vendorHash}/?components=304"
    apiResponse304 = get_api_request(apiUrl304)
    apiResponse304Json = json.loads(apiResponse304)
    
    apiUrl401 = destiny.destinyURLBase + f"/Destiny2/{destiny.membershipType}/Profile/{destiny.membershipId}/Character/{class_id}/Vendors/{destiny.vendorHash}/?components=401"
    apiResponse401 = get_api_request(apiUrl401)
    apiResponse401Json = json.loads(apiResponse401)

    apiUrl402 = destiny.destinyURLBase + f"/Destiny2/{destiny.membershipType}/Profile/{destiny.membershipId}/Character/{class_id}/Vendors/{destiny.vendorHash}/?components=402"
    apiResponse402 = get_api_request(apiUrl402)
    apiResponse402Json = json.loads(apiResponse402)
    
    for item in apiResponse401Json["Response"]["categories"]["data"]["categories"]:
        if artificeHash:
            break
        for id in item.get('itemIndexes')[::-1]:
            hashedData = await decode_hash(destiny,apiResponse402Json["Response"]["sales"]["data"][str(id)].get("itemHash"),"DestinyInventoryItemDefinition")
            if hashedData["itemType"] == 2 and hashedData["equippingBlock"].get("uniqueLabelHash") != 761097285:
                
                #there is artifice armor 
                artificeHash = apiResponse402Json["Response"]["sales"]["data"][str(id)].get("itemHash")
                artificeID = id
                break
            
    
    socketStatDict = apiResponse304Json["Response"]["itemComponents"]["stats"]["data"][str(artificeID)]
    
    
    hashData = await decode_hash(destiny,artificeHash,"DestinyInventoryItemDefinition")
    
    #total, mobility, resilince , recovery ,discipline, intelect, strength
    statsList = [0,0,0,0,0,0,0]
    statTotal = 0
    statDict = socketStatDict["stats"]
    
    
    for key, val in statDict.items():
        statTotal += val.get("value")
        statTypeStr = destiny.decodeStatHash(int(key))
        
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
    armorData = await decode_hash(destiny,artificeHash,"DestinyInventoryItemDefinition")
    
    loreHash = armorData.get("loreHash")
    if(loreHash == None):
        armorLore = None
    else:
        armorLore = await decode_hash(destiny,str(loreHash),"DestinyLoreDefinition")
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
    if(class_type== "warlock"):
        destiny.ArtificeArmor[1] = jsonTemplate
    if(class_type== "hunter"):
        destiny.ArtificeArmor[0] = jsonTemplate
    if(class_type== "titan"):
        destiny.ArtificeArmor[2] = jsonTemplate