#handles weapons and their stats
from destiny_api import get_api_request, decode_hash
from perk_utils import get_weapon_perks

import requests,json,aiohttp,asyncio



async def get_weapons(destiny):
    weaponHashList = []

    apiUrl402 = destiny.destinyURLBase + f"/Destiny2/{destiny.membershipType}/Profile/{destiny.membershipId}/Character/{characterIDWarlock}/Vendors/{destiny.strangeGearVendorHash}/?components=402"
    apiResponse402 = get_api_request(apiUrl402)
    apiResponse402Json = json.loads(apiResponse402)
    
    for itemID, itemIDData in apiResponse402Json["Response"]["sales"]["data"].items():
        weaponID = await decode_hash(itemIDData.get("itemHash"),"DestinyInventoryItemDefinition")
        #check if the hash is tied to a weapon
        if(weaponID.get("itemType") == 3):
            weaponHashList.append(itemIDData.get("itemHash"))
    
    #run through hash list and get data for each weapon
    for item in weaponHashList:
        weaponHashData = await decode_hash(item,"DestinyInventoryItemDefinition")
        loreHash = weaponHashData.get("loreHash")
        if(loreHash == None):
            weaponLore = None
        else:
            weaponLore = await decode_hash(str(loreHash),"DestinyLoreDefinition")
            weaponLore = weaponLore["displayProperties"].get("description")

        #decode elemental information
        elementData = await decode_hash(str(weaponHashData["damageTypeHashes"][0]),"DestinyDamageTypeDefinition")

        damageType = weaponHashData["itemCategoryHashes"][0]
        damageTypeHash = await decode_hash(damageType,"DestinyItemCategoryDefinition")


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
            destiny.LegendaryWeapons.append(jsonTemplate)

        destiny.weaponsTemplatesList.append(jsonTemplate)
    await get_weapon_perks(destiny)
    await destiny.bindStatToWeapon()


    for item in destiny.weaponsTemplatesList:
        perkHashList = []
        
        for perk in item["weaponPerks"]:
            perkHashList.append(perk["hashID"])
        destiny.XursInventoryItems.append(item)



async def get_exotic_catalysts(destiny):
    exoticCatalysts = []

    apiUrl308 = destiny.destinyURLBase + f"/Destiny2/{destiny.membershipType}/Profile/{destiny.membershipId}/Character/{characterIDWarlock}/Vendors/{destiny.vendorHash}/?components=308"
    apiResponse308 = get_api_request(apiUrl308)
    apiResponse308Json = json.loads(apiResponse308)

    for itemID, itemIDData in apiResponse308Json["Response"]["itemComponents"]["plugStates"]["data"].items():
        if len(exoticCatalysts) > 2:
            break
        
        hashedData = await decode_hash(itemIDData.get("plugItemHash"),"DestinyInventoryItemDefinition")
        if(hashedData.get('traitIds') == ['item.exotic_catalyst']):
            
            catalystPerks = []

            #get perks of the catalyst
            for perk in hashedData.get("perks"):
                hashedPerkData = await decode_hash(perk.get("perkHash"),"DestinySandboxPerkDefinition")
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
        destiny.FirstCatalyst = exoticCatalysts[0]
        destiny.SecondCatalyst = exoticCatalysts[1]


#checks for missing masterwork data on weapons
async def masterwork_check(destiny):
    print(destiny.LegendaryWeapons)
    for weapon in destiny.LegendaryWeapons:
        if(weapon["masterworkData"] == None):
            print("No mw found!")
            apiUrl402 = destiny.destinyURLBase + f"/Destiny2/{destiny.membershipType}/Profile/{destiny.membershipId}/Character/{characterIDWarlock}/Vendors/{destiny.strangeGearVendorHash}/?components=402"
            apiResponse402 = get_api_request(apiUrl402)
            apiResponse402Json = json.loads(apiResponse402)
            
            for key, value in apiResponse402Json["Response"]["sales"]["data"].items():
                
                if(value["itemHash"] == int(weapon["itemHash"])):
                    
                    hashedValData = await decode_hash(value["itemHash"],"DestinyInventoryItemDefinition")
                    
                    weaponSockets = hashedValData["sockets"].get("socketEntries")
                    for socket in weaponSockets:
                        print(socket.get("singleInitialItemHash"))
                        print(socket)
                        try:
                            socketData = await decode_hash(socket.get("singleInitialItemHash"),"DestinyInventoryItemDefinition")
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