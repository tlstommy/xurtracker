#functions related to weapon perks, such as getting the best perks from the community, sorting perks, and rating perks based on community data

from bs4 import BeautifulSoup
from destiny_api import get_api_request, decode_hash

import requests,json,aiohttp,asyncio

async def get_weapon_perks(destiny):
    #weapon Perk template
    IDtoWeaponHashDict = {}
    itemIDs402 = []
    socketIDs305 = []
    currentAvailableItems = []
    weaponPerkList = []




    #item sockets
    apiUrl305 = destiny.destinyURLBase + f"/Destiny2/{destiny.membershipType}/Profile/{destiny.membershipId}/Character/{destiny.warlockCharacterID}/Vendors/{destiny.strangeGearVendorHash}/?components=305"
    apiResponse305 = get_api_request(apiUrl305)
    apiResponse305Json = json.loads(apiResponse305)

    #itemplugs
    apiUrl310 = destiny.destinyURLBase + f"/Destiny2/{destiny.membershipType}/Profile/{destiny.membershipId}/Character/{destiny.warlockCharacterID}/Vendors/{destiny.strangeGearVendorHash}/?components=310"
    apiResponse310 = get_api_request(apiUrl310)
    apiResponse310Json = json.loads(apiResponse310)


    #destiny.combinedPerkJson = destiny.socketPlugs(apiResponse305Json,apiResponse310Json)


    #item ids
    apiUrl402 = destiny.destinyURLBase + f"/Destiny2/{destiny.membershipType}/Profile/{destiny.membershipId}/Character/{destiny.warlockCharacterID}/Vendors/{destiny.strangeGearVendorHash}/?components=402"
    apiResponse402 = get_api_request(apiUrl402)
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
    
    print(destiny.combinedPerksJson.items())


    for key, values in destiny.combinedPerksJson.items():
        
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
                decodedPlug = await decode_hash(destiny, plugHashVal,"DestinyInventoryItemDefinition")
                
                print(decodedPlug)
                #input("test!!!\n")
                
                
                
                #check if armor or not
                decodedWeaponHash = await decode_hash(destiny, IDtoWeaponHashDict[key],"DestinyInventoryItemDefinition")

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
                    weaponRollTemplate["isFavorablePerk"] = destiny.rateWeaponPerks(IDtoWeaponHashDict[key],decodedPlug["displayProperties"].get("name"))
                    destiny.weaponPerksTemplateList.append(weaponRollTemplate)

#get weapon perks from community
def get_weapon_perks_from_community(weapon_hash):
        favorablePerks = []
        url = "https://www.light.gg/db/items/"+str(weapon_hash)
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

#sort perks so they are grouped by their type
def perk_sort(perk_list):
        

        sorted_perk_dict = {}
        #group perks by perkSubType
        for perk in perk_list:
            perk_type = perk["perkSubType"]
            sorted_perk_dict.setdefault(perk_type, []).append(perk)

        sorted_perks = []

        for perks in sorted_perk_dict.values():
            sorted_perks.extend(perks)
        return sorted_perks

#rate perks based on community data, returns True if the weapon has the good perk, False otherwise
def rate_weapon_perks(destiny, weapon_hash, perk_name):
    topPerks = get_weapon_perks_from_community(weapon_hash)
    if(topPerks == -1):
        return False
    for i in range(len(topPerks)):
        if(topPerks[i] == perk_name):
            return True
    return False

