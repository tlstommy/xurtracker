from bs4 import BeautifulSoup
from destiny_api import get_api_request, decode_hash

import requests,json,aiohttp,asyncio


async def get_location(destiny):
    return "deprecated since TFS."


async def socket_plugs(socket_json, plug_json):
     # convert JSON if they are not already
        if isinstance(socket_json, str):
            socket_json = json.loads(socket_json)
        if isinstance(plug_json, str):
            plug_json = json.loads(plug_json)

        # extracting the relevant data from the JSON
        sockets = socket_json["Response"]["itemComponents"]["sockets"]["data"]
        plugs = plug_json["Response"]["itemComponents"]["reusablePlugs"]["data"]

        combined_data = {}

        #iterate through the sockets data and combine with plugs data
        for item_id, socket_info in sockets.items():
            seen_hashes = set()  # Set to track seen hashes
            hashes = []

            # function to add hash if not seen
            def add_hash(hash_value):
                if hash_value not in seen_hashes:
                    seen_hashes.add(hash_value)
                    hashes.append({"hash": hash_value})

            #Add hashes from sockets
            for socket in socket_info["sockets"]:
                if "plugHash" in socket and socket["isEnabled"]:
                    add_hash(socket["plugHash"])
                
            #Add hashes from plugs
            if item_id in plugs:
                for plug_list in plugs[item_id]["plugs"].values():
                    for plug in plug_list:
                        if plug["enabled"]:
                            add_hash(plug["plugItemHash"])

            combined_data[item_id] = {"hashes": hashes}

        return combined_data

async def bind_stats_to_weapon(destiny):
    for item in destiny.weaponsTemplatesList:
        weaponHash = item.get("itemHash")
        print(item.get("name"))
        for perk in destiny.weaponPerksTemplateList:
            
            perkWHash = perk.get("weaponHash")
            
            if weaponHash == str(perkWHash):
                
                #if the perk is a masterwork decode it
                if perk.get("description") == "Base-level weapon. Increase the tier to forge a Masterwork item.":    
                    print(perk)
                    masterWorkDecoded = await decode_hash(perk.get("hashID"),"DestinyInventoryItemDefinition")
                    statIcon = "https://www.bungie.net"+str(masterWorkDecoded["displayProperties"].get("icon"))
                    statTypeHash = str(masterWorkDecoded["investmentStats"][0].get("statTypeHash"))
                    statHashDecoded = await decode_hash(statTypeHash,"DestinyStatDefinition")

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
                if (await decode_hash(perk.get("hashID"),"DestinyInventoryItemDefinition")).get("uiItemDisplayStyle") == "ui_display_style_intrinsic_plug" and item.get("rarity") != "Exotic":
                    data = await decode_hash(perk.get("hashID"),"DestinyInventoryItemDefinition")
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
        item["weaponPerks"] = perk_sort(item["weaponPerks"])
            

#check to see if xur is selling an artifice armor piece
async def check_for_artifice(destiny):
    #get the one item from xurs main inventory first
    apiUrl401 = destiny.destinyURLBase + f"/Destiny2/{destiny.membershipType}/Profile/{destiny.membershipId}/Character/{characterIDHunter}/Vendors/{destiny.vendorHash}/?components=401"
    apiResponse401 = get_api_request(apiUrl401)
    apiResponse401Json = json.loads(apiResponse401)

    apiUrl402 = destiny.destinyURLBase + f"/Destiny2/{destiny.membershipType}/Profile/{destiny.membershipId}/Character/{characterIDHunter}/Vendors/{destiny.vendorHash}/?components=402"
    apiResponse402 = get_api_request(apiUrl402)
    apiResponse402Json = json.loads(apiResponse402)

    for item in apiResponse401Json["Response"]["categories"]["data"]["categories"]:
        
        
        for id in item.get('itemIndexes')[::-1]:

            hashedData = await decode_hash(apiResponse402Json["Response"]["sales"]["data"][str(id)].get("itemHash"),"DestinyInventoryItemDefinition")
            
            if hashedData["itemType"] == 2 and hashedData["equippingBlock"].get("uniqueLabelHash") != 761097285:
                
                #there is artifice armor 
                destiny.ArtificePresent = True
                return True

def decode_stat_hash(hash):
    stat_map = {
            144602215: "Intellect",
            392767087: "Resilience",
            1735777505: "Discipline",
            1943323491: "Recovery",
            2996146975: "Mobility",
            4244567218: "Strength"
        }
    return stat_map.get(hash)

#determines if an item already exists in the json before its added
def json_conflict_check(destiny,json_dict):
    
    for item in destiny.XursInventoryItems:
        if (item["itemHash"] == json_dict["itemHash"] and item["class"] == json_dict["class"] and json_dict["class"] != 3):
            return True
    return False