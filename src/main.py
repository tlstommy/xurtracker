import requests,aiohttp,asyncio,json,pydest
from bs4 import BeautifulSoup
from datetime import date
from material_prices import *
from credentials import *

from weapons import get_weapons, get_exotic_catalysts,masterwork_check
from armor import get_exotic_armor, get_legendary_armor, get_artifice_armor
from inventory import get_material_offers, get_hidden_material_offers
from utils import bind_stats_to_weapon, check_for_artifice
from destiny_api import get_api_request, decode_hash
from utils import socket_plugs, get_location




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
        self.miscItemHashes = [3158812152,]

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

        self.SellingExoticClassItems = False


        #hunter,warlock,titan
        self.ArtificeArmor = [None,None,None] 

        #class specific armor
        self.WarlockHelmet = None
        self.WarlockArms = None
        self.WarlockChest = None
        self.WarlockLegs = None
        self.WarlockClassItem = None

        self.HunterHelmet = None
        self.HunterArms = None
        self.HunterChest = None
        self.HunterLegs = None
        self.HunterClassItem = None
        
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
        if write:
            for path in [
                "data-refactored-code-test.json",
                "destinyData-refactored-code-test.json"
            ]:
                with open(path, "w", encoding="utf-8") as outfile:
                    json.dump(JSONTemplate, outfile, indent=4)



    async def getXurInventory(self,charID):

        if await check_for_artifice(self):
            await get_artifice_armor(self, charID, "warlock")
            await get_artifice_armor(self, charID, "hunter")
            await get_artifice_armor(self, charID, "titan")


        
        #get all xurs inventory items
        apiUrl = f"{self.destinyURLBase}/Destiny2/{self.membershipType}/Profile/{self.membershipId}/Character/{charID}/Vendors/{self.vendorHash}/?components=402"
        self.apiResponse = get_api_request(apiUrl)
        self.apiResponseJson = json.loads(self.apiResponse)
        apiUrl305 = f"{self.destinyURLBase}/Destiny2/{self.membershipType}/Profile/{self.membershipId}/Character/{characterIDWarlock}/Vendors/{self.strangeGearVendorHash}/?components=305"
        apiResponse305 = get_api_request(apiUrl305)
        apiUrl310 = f"{self.destinyURLBase}/Destiny2/{self.membershipType}/Profile/{self.membershipId}/Character/{characterIDWarlock}/Vendors/{self.strangeGearVendorHash}/?components=310"
        apiResponse310 = get_api_request(apiUrl310)

        self.combinedPerksJson = await socket_plugs(apiResponse305, apiResponse310)
        self.forSaleItems = self.apiResponseJson["Response"]["sales"]["data"]



        await get_weapons(self)
        await get_exotic_catalysts(self)
        await get_exotic_armor(self, charID, "warlock")  # example
        await get_legendary_armor(self, charID, "warlock")
        await get_material_offers(self)
        await get_hidden_material_offers(self)
        await bind_stats_to_weapon(self)
        await check_for_artifice(self)
        await masterwork_check(self)
        
        self.buildJSON(True)

        return None
        







   

#main loop

def mainloop():
    #create and set new loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    #init class
    XI = main(API_KEY)
    loop.run_until_complete(XI.getXurInventory(characterIDWarlock))


if __name__ == "__main__":
    mainloop()
