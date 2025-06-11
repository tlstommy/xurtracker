#inventory items 
from destiny_api import get_api_request, decode_hash
from perk_utils import get_weapon_perks

from material_prices import *

import requests,json,aiohttp,asyncio

async def getXurStrangeGearOffers(destiny):
    return None

async def get_material_offers(destiny):
    #get the one item from xurs main inventory first
        apiUrl402 = destiny.destinyURLBase + f"/Destiny2/{destiny.membershipType}/Profile/{destiny.membershipId}/Character/{destiny.warlockCharacterID}/Vendors/{destiny.vendorHash}/?components=402"
        apiResponse402 = get_api_request(apiUrl402)
        apiResponse402Json = json.loads(apiResponse402)
        
        
        for itemID, itemIDData in apiResponse402Json["Response"]["sales"]["data"].items():
            hashedData = await decode_hash(destiny, itemIDData.get("itemHash"),"DestinyInventoryItemDefinition")
            if itemIDData.get("itemHash") in destiny.multivariousOfferableItems:
                
                hashedData = await decode_hash(destiny, itemIDData.get("itemHash"),"DestinyInventoryItemDefinition")

                

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

                
                destiny.MaterialOffers.append(itemTemplate)
                break

            

            if itemIDData.get("itemHash") in destiny.miscItemHashes:
                
                hashedData = await decode_hash(destiny, itemIDData.get("itemHash"),"DestinyInventoryItemDefinition")

                if hashedData.get("loreHash"):
                    lore =  await decode_hash(destiny, hashedData.get("loreHash"),"DestinyLoreDefinition")
                
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

                if itemTemplate not in destiny.MiscOffers:
                    destiny.MiscOffers.append(itemTemplate)
                break
        
        
        #now get the other items from the actual tab inside his menu

        #get the one item from xurs main inventory first
        apiUrl402 = destiny.destinyURLBase + f"/Destiny2/{destiny.membershipType}/Profile/{destiny.membershipId}/Character/{characterIDWarlock}/Vendors/{destiny.strangeMaterialVendorHash}/?components=402"
        apiResponse402 = get_api_request(apiUrl402)
        apiResponse402Json = json.loads(apiResponse402)

        for itemID, itemIDData in apiResponse402Json["Response"]["sales"]["data"].items():
            if itemIDData.get("itemHash") not in destiny.excludeableMaterialHashes:
                print(itemID,itemIDData.get("itemHash"))

                hashedData = await decode_hash(destiny, itemIDData.get("itemHash"),"DestinyInventoryItemDefinition")

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

                
                destiny.MaterialOffers.append(itemTemplate)


        
        destiny.MaterialOffers.sort(key=lambda item: item['name'])

async def get_hidden_material_offers(destiny):
    apiResponse402Json = json.loads(get_api_request(f"{destiny.destinyURLBase}/Destiny2/Vendors/?components=402"))
    forSaleItems = apiResponse402Json["Response"]["sales"]["data"][list(apiResponse402Json["Response"]["sales"]["data"].keys())[0]]["saleItems"]
    for i in range(len(forSaleItems)):
        hash = apiResponse402Json["Response"]["sales"]["data"][list(apiResponse402Json["Response"]["sales"]["data"].keys())[0]]["saleItems"][list(forSaleItems)[i]]["itemHash"]

        if hash in destiny.miscItemHashes:
            
            hashedData = await decode_hash(destiny, hash,"DestinyInventoryItemDefinition")

            if hashedData.get("loreHash"):
                lore =  await decode_hash(destiny, hashedData.get("loreHash"),"DestinyLoreDefinition")
            
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

            
            if itemTemplate not in destiny.MiscOffers:
                destiny.MiscOffers.append(itemTemplate)
            break