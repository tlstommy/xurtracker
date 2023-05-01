#!/usr/bin/env python
#generates html data for main.html from the json
import json
def buildWeaponPerkTable(perks):
    tableString = ""
    topStat = 0
    tableRowTemp = """
    <tr>
        <th scope="row"><img src="https://www.bungie.net/common/destiny2_content/icons/9f8f1a477734b3189a7e26b03cdd159e.png" width="40" height="40" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="<p></p>"></th>
        <td>Four-Headed Dog</td>
    </tr>
    """

    for i in range(len(perks)):
        if(perks[i]["isFavorablePerk"] == True):
            topStat = "3"
        else:
            topStat = "0"

        tableString = tableString + """
        <tr>
            <th scope="row">
                <img src="{icon}" width="40" height="40" style="border:solid {topStatSz}px yellow; border-radius: 40px;" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="<p>{desc}</p>">
                </img>
            </th>
            <td style="word-break:normal;">
                {perkName}
            </td>
        </tr>
        """.format(icon = perks[i]["perkIcon"],topStatSz = topStat,desc = perks[i]["description"],perkName = perks[i]["name"])
    return tableString

def buildExArmorStatTable(perks):
    htmlStr = """<tr>
                          <th scope="row"><img src="https://www.bungie.net/common/destiny2_content/icons/e26e0e93a9daf4fdd21bf64eb9246340.png" width="40" height="40" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Mobility"></th>
                            <td>{mob}</td>
                          </tr>
                          <tr>
                            <th scope="row"><img src="https://www.bungie.net/common/destiny2_content/icons/202ecc1c6febeb6b97dafc856e863140.png" width="40" height="40" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Resilience"></th>
                            <td>{res}</td>
                          </tr>
                          <tr>
                            <th scope="row"><img src="https://www.bungie.net/common/destiny2_content/icons/128eee4ee7fc127851ab32eac6ca91cf.png" width="40" height="40" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Recovery"></th>
                            <td>{rec}</td>
                          </tr>
                          <tr>
                            <th scope="row"><img src="https://www.bungie.net/common/destiny2_content/icons/ca62128071dc254fe75891211b98b237.png" width="40" height="40" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Discipline"></th>
                            <td>{dis}</td>
                          </tr>
                          <tr>
                            <th scope="row"><img src="https://www.bungie.net/common/destiny2_content/icons/59732534ce7060dba681d1ba84c055a6.png" width="40" height="40" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Intellect"></th>
                            <td>{inte}</td>
                          </tr>
                          <tr>
                            <th scope="row"><img src="https://www.bungie.net/common/destiny2_content/icons/c7eefc8abbaa586eeab79e962a79d6ad.png" width="40" height="40" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Strength"></th>
                            <td>{stre}</td>
                          </tr>
                          <tr>
                            <th scope="row">Total</th>
                            <td><b>{total}</b></td>
                          </tr>""".format(mob = perks["statRolls"][1],res = perks["statRolls"][2],rec = perks["statRolls"][3],dis = perks["statRolls"][4],inte = perks["statRolls"][5],stre = perks["statRolls"][6],total = perks["statRolls"][0])

    return htmlStr

def updateEnergyIcon(archetype,elemental,num):
    
    iconUrl = ""
    damageString = ""


    if(elemental == "Kinetic"):
        iconUrl = "https://www.bungie.net/common/destiny2_content/icons/DestinyDamageTypeDefinition_3385a924fd3ccb92c343ade19f19a370.png"
        damageString = elemental
    if(elemental == "Void"):
        iconUrl = "https://www.bungie.net/common/destiny2_content/icons/DestinyDamageTypeDefinition_ceb2f6197dccf3958bb31cc783eb97a0.png"
        damageString = elemental +" "+archetype
    if(elemental == "Arc"):
        iconUrl = "https://www.bungie.net/common/destiny2_content/icons/DestinyDamageTypeDefinition_092d066688b879c807c3b460afdd61e6.png"
        damageString = elemental +" "+archetype
    if(elemental == "Solar"):
        iconUrl = "https://www.bungie.net/common/destiny2_content/icons/DestinyDamageTypeDefinition_2a1773e10968f2d088b97c22b22bba9e.png"
        damageString = elemental +" "+archetype
    if(elemental == "Stasis"):
        iconUrl = "https://www.bungie.net/common/destiny2_content/icons/DestinyDamageTypeDefinition_530c4c3e7981dc2aefd24fd3293482bf.png"
        damageString = elemental +" "+archetype
    return iconUrl,damageString

def buildLegendArmorStatTable(perks):
    htmlStr = """
                    <td class="text-center">{mob}</td>
                    <td class="text-center">{res}</td>
                    <td class="text-center">{rec}</td>
                    <td class="text-center">{dis}</td>
                    <td class="text-center">{inte}<br><b style="font-size: 120%;">Total: </b></td>
                    <td class="text-center">{stre}<br><b style="font-size: 120%;">{total}</b></td>
                </tr>""".format(mob = perks["statRolls"][1],res = perks["statRolls"][2],rec = perks["statRolls"][3],dis = perks["statRolls"][4],inte = perks["statRolls"][5],stre = perks["statRolls"][6],total = perks["statRolls"][0])

    return htmlStr

def cleanHTML(html):
    html = html.replace("\u2022","<br>&#8226;")
    html = html.replace("\u2014","&nbsp;&#8212&nbsp;")
    html = html.replace("\u201c","&#8220;")
    html = html.replace("\u201d","&#8221;")
    html = html.replace("\u2026","&#8230;")
    cleanedHTML = html
    return cleanedHTML




def setHtmlVals():
    #read in the json doc
    file = open("/home/ubuntu/XurTracker/data/data.json")
    data = json.load(file)
    file.close()

    #set all vals
    location = data["Location"]
    planet = data["Planet"]
    landingZone = data["Landing Zone"]
    week = data["Week"]
    exoticWeaponName = data["Exotics"]["Exotic Weapon"]["name"]
    exoticWeaponType = data["Exotics"]["Exotic Weapon"]["type"].replace("Exotic ","")
    exoticWeaponIcon = data["Exotics"]["Exotic Weapon"]["icon"]
    exoticWeaponLore = data["Exotics"]["Exotic Weapon"]["lore"].replace('"','&quot').replace("\u2014","</em><br><br>&#8212&nbsp;")
    exoticWeaponPerkTable = buildWeaponPerkTable(data["Exotics"]["Exotic Weapon"]["weaponPerks"])
    hawkmoonWeaponPerkTable = buildWeaponPerkTable(data["Exotics"]["Hawkmoon"]["weaponPerks"])
    hawkmoonRating = data["Exotics"]["Hawkmoon"]["itemRating"]
    deadMansTalePerkTable = buildWeaponPerkTable(data["Exotics"]["Dead Mans Tale"]["weaponPerks"])
    deadMansTaleRating = data["Exotics"]["Dead Mans Tale"]["itemRating"]
    exoticWarlockStatTable = buildExArmorStatTable(data["Exotics"]["Warlock Exotic"])
    exoticWarlockName = data["Exotics"]["Warlock Exotic"]["name"]
    exoticWarlockType = data["Exotics"]["Warlock Exotic"]["type"].replace("Exotic ","")
    exoticWarlockIcon = data["Exotics"]["Warlock Exotic"]["icon"]
    exoticWarlockLore = data["Exotics"]["Warlock Exotic"]["lore"].replace('"','&quot').replace("\u2014","</em><br><br>&#8212&nbsp;")
    exoticHunterStatTable = buildExArmorStatTable(data["Exotics"]["Hunter Exotic"])
    exoticHunterName = data["Exotics"]["Hunter Exotic"]["name"]
    exoticHunterType = data["Exotics"]["Hunter Exotic"]["type"].replace("Exotic ","")
    exoticHunterIcon = data["Exotics"]["Hunter Exotic"]["icon"]
    exoticHunterLore = data["Exotics"]["Hunter Exotic"]["lore"].replace('"','&quot').replace("\u2014","</em><br><br>&#8212&nbsp;")
    exoticTitanStatTable = buildExArmorStatTable(data["Exotics"]["Titan Exotic"])
    exoticTitanName = data["Exotics"]["Titan Exotic"]["name"]
    exoticTitanType = data["Exotics"]["Titan Exotic"]["type"].replace("Exotic ","")
    exoticTitanIcon = data["Exotics"]["Titan Exotic"]["icon"]
    exoticTitanLore = data["Exotics"]["Titan Exotic"]["lore"].replace('"','&quot').replace("\u2014","</em><br><br>&#8212&nbsp;")
    legendaryWeapon1Name = data["Legendaries"]["Legendary weapons"][0]["name"]
    legendaryWeapon1Type = data["Legendaries"]["Legendary weapons"][0]["type"].replace("Legendary ","")
    legendaryWeapon1Rating = data["Legendaries"]["Legendary weapons"][0]["itemRating"]
    legendaryWeapon1Icon = data["Legendaries"]["Legendary weapons"][0]["icon"]
    legendaryWeapon1Lore = data["Legendaries"]["Legendary weapons"][0]["lore"].replace('"','&quot').replace("\u2014","</em><br><br>&#8212&nbsp;")
    legendaryWeapon1PerkTable = buildWeaponPerkTable(data["Legendaries"]["Legendary weapons"][0]["weaponPerks"])
    legendaryWeapon1DamageType = data["Legendaries"]["Legendary weapons"][0]["legendWeaponDamageType"]
    legendaryWeapon1DamageElement = data["Legendaries"]["Legendary weapons"][0]["legendWeaponDamageElement"]

    legendaryWeapon2Name = data["Legendaries"]["Legendary weapons"][1]["name"]
    legendaryWeapon2Type = data["Legendaries"]["Legendary weapons"][1]["type"].replace("Legendary ","")
    legendaryWeapon2Rating = data["Legendaries"]["Legendary weapons"][1]["itemRating"]
    legendaryWeapon2Icon = data["Legendaries"]["Legendary weapons"][1]["icon"]
    legendaryWeapon2Lore = data["Legendaries"]["Legendary weapons"][1]["lore"].replace('"','&quot').replace("\u2014","</em><br><br>&#8212&nbsp;")
    legendaryWeapon2PerkTable = buildWeaponPerkTable(data["Legendaries"]["Legendary weapons"][1]["weaponPerks"])
    legendaryWeapon2DamageType = data["Legendaries"]["Legendary weapons"][1]["legendWeaponDamageType"]
    legendaryWeapon2DamageElement = data["Legendaries"]["Legendary weapons"][1]["legendWeaponDamageElement"]

    legendaryWeapon3Name = data["Legendaries"]["Legendary weapons"][2]["name"]
    legendaryWeapon3Type = data["Legendaries"]["Legendary weapons"][2]["type"].replace("Legendary ","")
    legendaryWeapon3Rating = data["Legendaries"]["Legendary weapons"][2]["itemRating"]
    legendaryWeapon3Icon = data["Legendaries"]["Legendary weapons"][2]["icon"]
    legendaryWeapon3Lore = data["Legendaries"]["Legendary weapons"][2]["lore"].replace('"','&quot').replace("\u2014","</em><br><br>&#8212&nbsp;")
    legendaryWeapon3PerkTable = buildWeaponPerkTable(data["Legendaries"]["Legendary weapons"][2]["weaponPerks"])
    legendaryWeapon3DamageType = data["Legendaries"]["Legendary weapons"][2]["legendWeaponDamageType"]
    legendaryWeapon3DamageElement = data["Legendaries"]["Legendary weapons"][2]["legendWeaponDamageElement"]

    legendaryWeapon4Name = data["Legendaries"]["Legendary weapons"][3]["name"]
    legendaryWeapon4Type = data["Legendaries"]["Legendary weapons"][3]["type"].replace("Legendary ","")
    legendaryWeapon4Rating = data["Legendaries"]["Legendary weapons"][3]["itemRating"]
    legendaryWeapon4Icon = data["Legendaries"]["Legendary weapons"][3]["icon"]
    legendaryWeapon4Lore = data["Legendaries"]["Legendary weapons"][3]["lore"].replace('"','&quot').replace("\u2014","</em><br><br>&#8212&nbsp;")
    legendaryWeapon4PerkTable = buildWeaponPerkTable(data["Legendaries"]["Legendary weapons"][3]["weaponPerks"])
    legendaryWeapon4DamageType = data["Legendaries"]["Legendary weapons"][3]["legendWeaponDamageType"]
    legendaryWeapon4DamageElement = data["Legendaries"]["Legendary weapons"][3]["legendWeaponDamageElement"]

    legendaryWeapon5Name = data["Legendaries"]["Legendary weapons"][4]["name"]
    legendaryWeapon5Type = data["Legendaries"]["Legendary weapons"][4]["type"].replace("Legendary ","")
    legendaryWeapon5Rating = data["Legendaries"]["Legendary weapons"][4]["itemRating"]
    legendaryWeapon5Icon = data["Legendaries"]["Legendary weapons"][4]["icon"]
    legendaryWeapon5Lore = data["Legendaries"]["Legendary weapons"][4]["lore"].replace('"','&quot').replace("\u2014","</em><br><br>&#8212&nbsp;")
    legendaryWeapon5PerkTable = buildWeaponPerkTable(data["Legendaries"]["Legendary weapons"][4]["weaponPerks"])
    legendaryWeapon5DamageType = data["Legendaries"]["Legendary weapons"][4]["legendWeaponDamageType"]
    legendaryWeapon5DamageElement = data["Legendaries"]["Legendary weapons"][4]["legendWeaponDamageElement"]

    legendaryWeapon6Name = data["Legendaries"]["Legendary weapons"][5]["name"]
    legendaryWeapon6Type = data["Legendaries"]["Legendary weapons"][5]["type"].replace("Legendary ","")
    legendaryWeapon6Rating = data["Legendaries"]["Legendary weapons"][5]["itemRating"]
    legendaryWeapon6Icon = data["Legendaries"]["Legendary weapons"][5]["icon"]
    legendaryWeapon6Lore = data["Legendaries"]["Legendary weapons"][5]["lore"].replace('"','&quot').replace("\u2014","</em><br><br>&#8212&nbsp;")
    legendaryWeapon6PerkTable = buildWeaponPerkTable(data["Legendaries"]["Legendary weapons"][5]["weaponPerks"])
    legendaryWeapon6DamageType = data["Legendaries"]["Legendary weapons"][5]["legendWeaponDamageType"]
    legendaryWeapon6DamageElement = data["Legendaries"]["Legendary weapons"][5]["legendWeaponDamageElement"]

    legendaryWeapon7Name = data["Legendaries"]["Legendary weapons"][6]["name"]
    legendaryWeapon7Type = data["Legendaries"]["Legendary weapons"][6]["type"].replace("Legendary ","")
    legendaryWeapon7Rating = data["Legendaries"]["Legendary weapons"][6]["itemRating"]
    legendaryWeapon7Icon = data["Legendaries"]["Legendary weapons"][6]["icon"]
    legendaryWeapon7Lore = data["Legendaries"]["Legendary weapons"][6]["lore"].replace('"','&quot').replace("\u2014","</em><br><br>&#8212&nbsp;")
    legendaryWeapon7PerkTable = buildWeaponPerkTable(data["Legendaries"]["Legendary weapons"][6]["weaponPerks"])
    legendaryWeapon7DamageType = data["Legendaries"]["Legendary weapons"][6]["legendWeaponDamageType"]
    legendaryWeapon7DamageElement = data["Legendaries"]["Legendary weapons"][6]["legendWeaponDamageElement"]

    #warlock
    WarlockHelmetName = data["Legendaries"]["Warlock"]["Helmet"]["name"]
    WarlockHelmetIcon = data["Legendaries"]["Warlock"]["Helmet"]["icon"]
    WarlockHelmetStatTable = buildLegendArmorStatTable(data["Legendaries"]["Warlock"]["Helmet"])

    WarlockArmsName = data["Legendaries"]["Warlock"]["Arms"]["name"]
    WarlockArmsIcon = data["Legendaries"]["Warlock"]["Arms"]["icon"]
    WarlockArmsStatTable = buildLegendArmorStatTable(data["Legendaries"]["Warlock"]["Arms"])

    WarlockChestName = data["Legendaries"]["Warlock"]["Chest"]["name"]
    WarlockChestIcon = data["Legendaries"]["Warlock"]["Chest"]["icon"]
    WarlockChestStatTable = buildLegendArmorStatTable(data["Legendaries"]["Warlock"]["Chest"])

    WarlockLegsName = data["Legendaries"]["Warlock"]["Legs"]["name"]
    WarlockLegsIcon = data["Legendaries"]["Warlock"]["Legs"]["icon"]
    WarlockLegsStatTable = buildLegendArmorStatTable(data["Legendaries"]["Warlock"]["Legs"])

    WarlockClassItemName = data["Legendaries"]["Warlock"]["Class Item"]["name"]
    WarlockClassItemIcon = data["Legendaries"]["Warlock"]["Class Item"]["icon"]
    WarlockClassItemStatTable = buildLegendArmorStatTable(data["Legendaries"]["Warlock"]["Class Item"])


    #Hunter
    HunterHelmetName = data["Legendaries"]["Hunter"]["Helmet"]["name"]
    HunterHelmetIcon = data["Legendaries"]["Hunter"]["Helmet"]["icon"]
    HunterHelmetStatTable = buildLegendArmorStatTable(data["Legendaries"]["Hunter"]["Helmet"])

    HunterArmsName = data["Legendaries"]["Hunter"]["Arms"]["name"]
    HunterArmsIcon = data["Legendaries"]["Hunter"]["Arms"]["icon"]
    HunterArmsStatTable = buildLegendArmorStatTable(data["Legendaries"]["Hunter"]["Arms"])

    HunterChestName = data["Legendaries"]["Hunter"]["Chest"]["name"]
    HunterChestIcon = data["Legendaries"]["Hunter"]["Chest"]["icon"]
    HunterChestStatTable = buildLegendArmorStatTable(data["Legendaries"]["Hunter"]["Chest"])

    HunterLegsName = data["Legendaries"]["Hunter"]["Legs"]["name"]
    HunterLegsIcon = data["Legendaries"]["Hunter"]["Legs"]["icon"]
    HunterLegsStatTable = buildLegendArmorStatTable(data["Legendaries"]["Hunter"]["Legs"])

    HunterClassItemName = data["Legendaries"]["Hunter"]["Class Item"]["name"]
    HunterClassItemIcon = data["Legendaries"]["Hunter"]["Class Item"]["icon"]
    HunterClassItemStatTable = buildLegendArmorStatTable(data["Legendaries"]["Hunter"]["Class Item"])


    #Titan
    TitanHelmetName = data["Legendaries"]["Titan"]["Helmet"]["name"]
    TitanHelmetIcon = data["Legendaries"]["Titan"]["Helmet"]["icon"]
    TitanHelmetStatTable = buildLegendArmorStatTable(data["Legendaries"]["Titan"]["Helmet"])

    TitanArmsName = data["Legendaries"]["Titan"]["Arms"]["name"]
    TitanArmsIcon = data["Legendaries"]["Titan"]["Arms"]["icon"]
    TitanArmsStatTable = buildLegendArmorStatTable(data["Legendaries"]["Titan"]["Arms"])

    TitanChestName = data["Legendaries"]["Titan"]["Chest"]["name"]
    TitanChestIcon = data["Legendaries"]["Titan"]["Chest"]["icon"]
    TitanChestStatTable = buildLegendArmorStatTable(data["Legendaries"]["Titan"]["Chest"])

    TitanLegsName = data["Legendaries"]["Titan"]["Legs"]["name"]
    TitanLegsIcon = data["Legendaries"]["Titan"]["Legs"]["icon"]
    TitanLegsStatTable = buildLegendArmorStatTable(data["Legendaries"]["Titan"]["Legs"])

    TitanClassItemName = data["Legendaries"]["Titan"]["Class Item"]["name"]
    TitanClassItemIcon = data["Legendaries"]["Titan"]["Class Item"]["icon"]
    TitanClassItemStatTable = buildLegendArmorStatTable(data["Legendaries"]["Titan"]["Class Item"])

    damageElementList = [legendaryWeapon1DamageElement,legendaryWeapon2DamageElement,legendaryWeapon3DamageElement,legendaryWeapon4DamageElement,legendaryWeapon5DamageElement,legendaryWeapon6DamageElement,legendaryWeapon7DamageElement]
    damageTypeList = [legendaryWeapon1DamageType,legendaryWeapon2DamageType,legendaryWeapon3DamageType,legendaryWeapon4DamageType,legendaryWeapon5DamageType,legendaryWeapon6DamageType,legendaryWeapon7DamageType]
    iconList = []
    damageStrList = []

    for i in range(len(damageElementList)):
        iconUrl,damageStr = updateEnergyIcon(damageTypeList[i],damageElementList[i],i+1)
        iconList.append(iconUrl)
        damageStrList.append(damageStr)



    legendaryWeapon1DamageTypeIcon = iconList[0]
    legendaryWeapon2DamageTypeIcon = iconList[1]
    legendaryWeapon3DamageTypeIcon = iconList[2]
    legendaryWeapon4DamageTypeIcon = iconList[3]
    legendaryWeapon5DamageTypeIcon = iconList[4]
    legendaryWeapon6DamageTypeIcon = iconList[5]
    legendaryWeapon7DamageTypeIcon = iconList[6]

    legendaryWeapon1DamageElement = damageStrList[0]
    legendaryWeapon2DamageElement = damageStrList[1]
    legendaryWeapon3DamageElement = damageStrList[2]
    legendaryWeapon4DamageElement = damageStrList[3]
    legendaryWeapon5DamageElement = damageStrList[4]
    legendaryWeapon6DamageElement = damageStrList[5]
    legendaryWeapon7DamageElement = damageStrList[6]

    htmlTemp ="""<!DOCTYPE html>
    <html lang="en">
    <head>
    <link rel="shortcut icon" href="https://pbs.twimg.com/profile_images/1586064167131385857/1mQC0kgE_400x400.png">
    <link rel="apple-touch-icon" sizes="192x192" href="https://pbs.twimg.com/profile_images/1586064167131385857/1mQC0kgE_400x400.png">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.3/font/bootstrap-icons.css">
    <title>X&#251r Tracker // All Items</title>
    <meta charset="utf-8";>
    <meta name="description" content="Tracks Destiny 2's X&#251r location and Inventory.">
    <meta name="keywords" content="xur,Xûr,Xur,xurtracker,wtfix,exotic inventory,destiny,destinythegame,whereisxur,destiny 2,D2,d2,where is xur,xur location,xurtrack,xur inventory">
    <meta name="author" content="Thomas Smith">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!--Bootstrap CDN CSS-->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <!--Bootstrap CDN JS-->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    <!--FA CDN-->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css" integrity="sha512-KfkfwYDsLkIlwQp6LFnl8zNdLGxu9YAA1QvwINks4PhcElQSvqcyVLLD9aMhXd13uQjoXtEKNosOWaZqXgel0g==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <nav class="navbar navbar-expand-lg navbar-light bg-secondary text-white">
        <div class="container-fluid">
            <a class="navbar-brand mb-0 h1" href="https://www.xurtracker.com">X&#251r Tracker</a>
            <button class="navbar-toggler" style="margin-right:5px !important;" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <div class="navbar-nav">
                    <a class="nav-link active" aria-current="page" href="all">All Items</a>
                    <a class="nav-link active" href="exotics">Exotic Items</a>
                    <a class="nav-link active" href="legendary-weapons">Legendary Weapons</a>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle active" href="#" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        Armor
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                        <li><a class="dropdown-item" href="titan">Titan Armor</a></li>
                        <li><a class="dropdown-item" href="hunter">Hunter Armor</a></li>
                        <li><a class="dropdown-item" href="warlock">Warlock Armor</a></li>
                        </ul>
                    </li>   
                </div>
                <nav class="navbar-nav ms-auto">
                    <div>
                        <a class="navbar-brand mb-0" href="#" target="_blank" rel="noopener noreferrer" data-bs-toggle="modal" data-bs-target="#infoModal">
                            <i class="bi bi-question-circle" style="font-size: 2rem;"></i>
                        </a>
                        <a class="navbar-brand mb-0" href="https://github.com/lulamae12/xurtracker.com" target="_blank" rel="noopener noreferrer">
                            <i class="bi bi-github" style="font-size: 2rem;"></i>
                        </a>
                        <a class="navbar-brand mb-0" href="https://twitter.com/XurTrack">
                            <i class="bi bi-twitter" style="font-size: 2rem; color: #0e1010;"></i>
                        </a>
                    </div>
                </nav>
            </div>
        </div>
    </nav> 
    <style>
        body{{
            color: #ffffff;
        }}
        .tooltip-inner {{
            background-color: #0e1010;
            box-shadow: 0px 0px 5px #ffffff;
            opacity: 1 !important;
        }}
        ::-webkit-scrollbar {{
            width: 0;
            background: transparent;
        }} 
    </style>

    <div aria-live="polite" aria-atomic="true" class="position-relative">
        <div class="toast-container position-fixed top-2 end-0 p-3">        
            <div class="toast" id="myToast" data-bs-delay="10000">
                <div class="toast-header text-black">
                    <strong class="me-auto" style="color: #000000;">Thanks for using X&#251r Tracker!</strong>
                    <small><b>Tips</b></small>
                    <button type="button" class="btn-close" data-bs-dismiss="toast"></button>
                </div>
                <div class="toast-body" style="color: #000000;">
                    <h6>&#8226;Hover over an item for more information. <br><br>&#8226;Yellow borders indicate a favorable perk.</h6>
                </div>
            </div>
        </div>
    </div>

    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-Y64WQ82WSS"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){{dataLayer.push(arguments);}}
        gtag('js', new Date());

        gtag('config', 'G-Y64WQ82WSS');
    </script>

    
    </head>
    <body style="background-color:  #000000; overflow: auto;">
        <div class="container">
            <div class="row">
                <div class="col-12">
                    <br>
                    <br>
                    <h1 style="text-align:center;">
                        X&#251r's Inventory for {week}
                    </h1>
                    <br>
                    <br>
                </div>
            </div>
        </div>
        <div class="container">
            <div class="row">
                <div class="col-12d d-flex justify-content-center">
                    <div class="card border" style="max-width: 25rem; color: #ffffff;background-color: #0e1010;;">
                        <div class="card-header border">
                            <h5>X&#251r's Current Location</h5>
                        </div>
                        <div class="card-body">
                            <h2 class="card-title">{landingZone}</h2>
                            <h6 class="card-subtitle">{location}, {planet}</h6>
                            <br>
                            <p>X&#251r will be in the {landingZone} until weekly reset.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <br>
        <div class="container">
        <h2>Exotic Weapons and Armor</h2>
        <hr>
        <br>   
            <div class="row justify-content-around" style="word-break: break-all;">
                <div class="col-lg-2 col-md-6" style="height:fit-content;">
                    <br>
                    <h5>Exotic Weapon</h5>
                    <hr>
                        <img src="{exoticWeaponIcon}" class="img" alt="exotic"  data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="<p>{exoticWeaponLore}</p>"></img>
                        <div class="weaponData">
                            <b>{exoticWeaponName}</b>
                            <p>{exoticWeaponType}</p>
                            <br>
                            <table class="table-sm table-borderless">
                                <thead>
                                    <tr>
                                    <th scope="col" style="white-space: nowrap; max-width: 50px;">Weapon Perks</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {exoticWeaponPerkTable}
                                </tbody>
                            </table>
                        </div>
                </div>
                <div class="col-lg-2 col-md-6" style="height:fit-content;">
                    <br>
                    <h5>Hawkmoon</h5>
                    <hr>
                    <img src="https://www.bungie.net/common/destiny2_content/icons/bc462cdde2fa00c808ff4f15802cb3b4.jpg" class="img" alt="hawkmoon"  data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="<p>Stalk thy prey and let loose thy talons upon the Darkness.</p>">
                    <div class="weaponData">
                        <b>Hawkmoon</b>
                        <p>Hand Cannon</p>
                        <br>
                        <table class="table-sm table-borderless">
                            <thead>
                                <tr>
                                <th scope="col" style="white-space: nowrap; max-width: 50px;">Weapon Perks</th>
                                </tr>
                            </thead>
                            <tbody>
                                {hawkmoonWeaponPerkTable}
                            </tbody>
                        </table>
                    </div>
                </div>
                <div class="col-lg-2 col-md-6" style="height:fit-content;">
                    <br>
                    <h5>Dead Man's Tale</h5>
                    <hr>
                    <img src="https://www.bungie.net/common/destiny2_content/icons/67634d7a01d7dca3aef90b4612d58489.jpg" class="img" alt="DMT" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="<p>&quotLong, short, they all end the same way. &quot<br>\u2014Katabasis</p>">
                    
                    <div class="weaponData">
                        <b>Dead Man's Tale</b>
                        
                        <p>Scout Rifle</p>
                        <br>
                        <table class="table-sm table-borderless">
                            <thead>
                                <tr>
                                <th scope="col" style="white-space: nowrap; max-width: 50px;">Weapon Perks</th>
                                </tr>
                            </thead>
                            <tbody>
                                {deadMansTalePerkTable}
                            </tbody>
                        </table>
                    </div>
                </div>
                <div class="col-lg-2 col-md-6" style="height:fit-content;">
                    <br>
                    <h5>Warlock Exotic</h5>
                    <hr>
                    <img src="{exoticWarlockIcon}" class="img" alt="exotic-warlock"  data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="<p>{exoticWarlockLore}</p>">
                    <div class="armorData">
                        <b>{exoticWarlockName}</b>
                        <p>{exoticWarlockType}</p>
                        <br>
                        <table class="table-sm table-borderless">
                            <thead>
                                <tr>
                                <th scope="col" style="white-space: nowrap; max-width: 50px;">Stat Rolls</th>
                                </tr>
                            </thead>
                            <tbody>
                                {exoticWarlockStatTable}
                            </tbody>
                        </table>
                    </div>
                </div>
                <div class="col-lg-2 col-md-6" style="height:fit-content;">
                    <br>
                    <h5>Hunter Exotic</h5>
                    <hr>
                    <img src="{exoticHunterIcon}" class="img" alt="exotic-hunter"  data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="<p>{exoticHunterLore}</p>">
                    <div class="armorData">
                        <b>{exoticHunterName}</b>
                        <p>{exoticHunterType}</p>
                        <br>
                        <table class="table-sm table-borderless">
                            <thead>
                                <tr>
                                <th scope="col" style="white-space: nowrap; max-width: 50px;">Stat Rolls</th>
                                </tr>
                            </thead>
                            <tbody>
                                {exoticHunterStatTable}
                            </tbody>
                        </table>
                    </div>
                </div>
                <div class="col-lg-2 col-md-6" style="height:fit-content;">
                    <br>
                    <h5>Titan Exotic</h5>
                    <hr>
                    <img src="{exoticTitanIcon}" class="img" alt="exotic-titan"  data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="<p>{exoticTitanLore}</p>">
                    
                    <div class="armorData">
                        <b>{exoticTitanName}</b>
                        <p>{exoticTitanType}</p>
                        <br>
                        <table class="table-sm table-borderless">
                            <thead>
                                <tr>
                                <th scope="col" style="white-space: nowrap; max-width: 50px;">Stat Rolls</th>
                                </tr>
                            </thead>
                            <tbody>
                                {exoticTitanStatTable}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>        
        <div class="container">
        <div class="row justify-content-around" style="font-size: 90%;">
            
            <br>
            <h2>Legendary Weapons</h2>
            <hr>
            <br>
                
            <div class="col-lg-1 col-md-3">
                <br>
                <img src="{legendaryWeapon1Icon}" class="img" alt="legendaryWeapon1"  data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="<p>{legendaryWeapon1Lore}</p>">
                    
                    <div class="weaponData">
                        <b style="white-space: nowrap;">{legendaryWeapon1Name}</b>
                        <p style="white-space: nowrap;"><img src="{legendaryWeapon1DamageTypeIcon}" width="20" height="20"
                                        style="border:solid 0px yellow; border-radius: 40px;" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="<p>This weapon deals {legendaryWeapon1DamageElement} damage.</p>"> {legendaryWeapon1Type}</p>
                        <br>
                        <table class="table-sm table-borderless">
                            <thead>
                                <tr>
                                <th scope="col" style="white-space: nowrap; max-width: 50px;">Weapon Perks</th>
                                </tr>
                            </thead>
                            <tbody>
                                {legendaryWeapon1PerkTable}
                            </tbody>
                        </table>
                    </div>
                </img>
            </div>
            <div class="col-lg-1 col-md-3">
                <br>
                <img src="{legendaryWeapon2Icon}" class="img" alt="legendaryWeapon2"  data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="<p>{legendaryWeapon2Lore}</p>">
                    
                    <div class="weaponData">
                        <b style="white-space: nowrap;">{legendaryWeapon2Name}</b>
                        <p style="white-space: nowrap;"><img src="{legendaryWeapon2DamageTypeIcon}" width="20" height="20"
                                        style="border:solid 0px yellow; border-radius: 40px;" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="<p>This weapon deals {legendaryWeapon2DamageElement} damage.</p>"> {legendaryWeapon2Type}</p>
                        <br>
                        <table class="table-sm table-borderless">
                            <thead>
                                <tr>
                                <th scope="col" style="white-space: nowrap; max-width: 50px;">Weapon Perks</th>
                                </tr>
                            </thead>
                            <tbody>
                                {legendaryWeapon2PerkTable}
                            </tbody>
                        </table>
                    </div>
                </img>
            </div>
            <div class="col-lg-1 col-md-3">
                <br>
                <img src="{legendaryWeapon3Icon}" class="img" alt="legendaryWeapon3"  data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="<p>{legendaryWeapon3Lore}</p>">
                    
                    <div class="weaponData">
                        <b style="white-space: nowrap;">{legendaryWeapon3Name}</b>
                        <p style="white-space: nowrap;"><img src="{legendaryWeapon3DamageTypeIcon}" width="20" height="20"
                                        style="border:solid 0px yellow; border-radius: 40px;" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="<p>This weapon deals {legendaryWeapon3DamageElement} damage.</p>"> {legendaryWeapon3Type}</p>
                        <br>
                        <table class="table-sm table-borderless">
                            <thead>
                                <tr>
                                <th scope="col" style="white-space: nowrap; max-width: 50px;">Weapon Perks</th>
                                </tr>
                            </thead>
                            <tbody>
                                {legendaryWeapon3PerkTable}
                            </tbody>
                        </table>
                    </div>
                </img>
            </div>
            <div class="col-lg-1 col-md-3">
                <br>
                <img src="{legendaryWeapon4Icon}" class="img" alt="legendaryWeapon4"  data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="<p>{legendaryWeapon4Lore}</p>">
                    
                    <div class="weaponData">
                        <b style="white-space: nowrap;">{legendaryWeapon4Name}</b>
                        <p style="white-space: nowrap;"><img src="{legendaryWeapon4DamageTypeIcon}" width="20" height="20"
                                        style="border:solid 0px yellow; border-radius: 40px;" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="<p>This weapon deals {legendaryWeapon4DamageElement} damage.</p>"> {legendaryWeapon4Type}</p>
                        <br>
                        <table class="table-sm table-borderless">
                            <thead>
                                <tr>
                                <th scope="col" style="white-space: nowrap; max-width: 50px;">Weapon Perks</th>
                                </tr>
                            </thead>
                            <tbody>
                                {legendaryWeapon4PerkTable}
                            </tbody>
                        </table>
                    </div>
                </img>
            </div>
            <div class="col-lg-1 col-md-3">
                <br>
                <img src="{legendaryWeapon5Icon}" class="img" alt="legendaryWeapon5"  data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="<p>{legendaryWeapon5Lore}</p>">
                    
                    <div class="weaponData">
                        <b style="white-space: nowrap;">{legendaryWeapon5Name}</b>
                        <p style="white-space: nowrap;"><img src="{legendaryWeapon5DamageTypeIcon}" width="20" height="20"
                                        style="border:solid 0px yellow; border-radius: 40px;" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="<p>This weapon deals {legendaryWeapon5DamageElement} damage.</p>"> {legendaryWeapon5Type}</p>
                        <br>
                        <table class="table-sm table-borderless">
                            <thead>
                                <tr>
                                <th scope="col" style="white-space: nowrap; max-width: 50px;">Weapon Perks</th>
                                </tr>
                            </thead>
                            <tbody>
                                {legendaryWeapon5PerkTable}
                            </tbody>
                        </table>
                    </div>
                </img>
            </div>
            <div class="col-lg-1 col-md-3">
                <br>
                <img src="{legendaryWeapon6Icon}" class="img" alt="legendaryWeapon6"  data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="<p>{legendaryWeapon6Lore}</p>">
                    
                    <div class="weaponData">
                        <b style="white-space: nowrap;">{legendaryWeapon6Name}</b>
                        <p style="white-space: nowrap;"><img src="{legendaryWeapon6DamageTypeIcon}" width="20" height="20"
                                        style="border:solid 0px yellow; border-radius: 40px;" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="<p>This weapon deals {legendaryWeapon6DamageElement} damage.</p>"> {legendaryWeapon6Type}</p>
                        <br>
                        <table class="table-sm table-borderless">
                            <thead>
                                <tr>
                                <th scope="col" style="white-space: nowrap; max-width: 50px;">Weapon Perks</th>
                                </tr>
                            </thead>
                            <tbody>
                                {legendaryWeapon6PerkTable}
                            </tbody>
                        </table>
                    </div>
                </img>
            </div>
            <div class="col-lg-1 col-md-3">
                <br>
                <img src="{legendaryWeapon7Icon}" class="img" alt="legendaryWeapon7"  data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="<p>{legendaryWeapon7Lore}</p>">
                    
                    <div class="weaponData">
                        <b style="white-space: nowrap;">{legendaryWeapon7Name}</b>
                        <p style="white-space: nowrap;"><img src="{legendaryWeapon7DamageTypeIcon}" width="20" height="20"
                                        style="border:solid 0px yellow; border-radius: 40px;" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="<p>This weapon deals {legendaryWeapon7DamageElement} damage.</p>"> {legendaryWeapon7Type}</p>
                        <br>
                        <table class="table-sm table-borderless">
                            <thead>
                                <tr>
                                <th scope="col" style="white-space: nowrap; max-width: 50px;">Weapon Perks</th>
                                </tr>
                            </thead>
                            <tbody>
                                {legendaryWeapon7PerkTable}
                            </tbody>
                        </table>
                    </div>
                </img>
            </div>
        </div>
        <div class="container-fluid">
            <div class="row justify-content-evenly" style="font-size: 100%;">
            
                <br>
                <h2>Legendary Armors</h2>
                <hr>
                <br>
                
                
                <div class="col-lg-4 col-md-7 overflow-auto">
                    <br>
                    <h4 style="text-align: center;">Warlock Armor<hr></h4>
                    <div class="warlockArmor">
                
                        
                        <table class="table" style="color: #ffffff;">
                            <thead scope="col">
                                <tr>
                                    <th scope="col">Armor</th>
                                    <th scope="col"><img src="https://www.bungie.net/common/destiny2_content/icons/e26e0e93a9daf4fdd21bf64eb9246340.png" width="40" height="40" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="top" title="Mobility"></th>
                                    <th scope="col"><img src="https://www.bungie.net/common/destiny2_content/icons/202ecc1c6febeb6b97dafc856e863140.png" width="40" height="40" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="top" title="Resilience"></th>
                                    <th scope="col"><img src="https://www.bungie.net/common/destiny2_content/icons/128eee4ee7fc127851ab32eac6ca91cf.png" width="40" height="40" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="top" title="Recovery"></th>
                                    <th scope="col"><img src="https://www.bungie.net/common/destiny2_content/icons/ca62128071dc254fe75891211b98b237.png" width="40" height="40" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="top" title="Discipline"></th>
                                    <th scope="col"><img src="https://www.bungie.net/common/destiny2_content/icons/59732534ce7060dba681d1ba84c055a6.png" width="40" height="40" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="top" title="Intellect"></th>
                                    <th scope="col"><img src="https://www.bungie.net/common/destiny2_content/icons/c7eefc8abbaa586eeab79e962a79d6ad.png" width="40" height="40" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="top" title="Strength"></th>
                                    
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <th scope="row"><img src="{WarlockHelmetIcon}"  class="img"  width="100%" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="{WarlockHelmetName}"></th>
                                    {WarlockHelmetStatTable}
                                <tr>
                                    <th scope="row"><img src="{WarlockArmsIcon}"  class="img"  width="100%" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="{WarlockArmsName}"></th>
                                    {WarlockArmsStatTable}
                                <tr>
                                    <th scope="row"><img src="{WarlockChestIcon}"  class="img"  width="100%" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="{WarlockChestName}"></th>
                                    {WarlockChestStatTable}
                                <tr>
                                    <th scope="row"><img src="{WarlockLegsIcon}"  class="img"  width="100%" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="{WarlockLegsName}"></th>
                                    {WarlockLegsStatTable}
                                <tr>
                                    <th scope="row"><img src="{WarlockClassItemIcon}"  class="img"  width="100%" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="{WarlockClassItemName}"></th>
                                    {WarlockClassItemStatTable}
                            </tbody>
                        </table>
                    </div>
                </div>
                
                <div class="col-lg-4 col-md-7 overflow-auto">
                    <br>
                    <h4 style="text-align: center;">Hunter Armor<hr></h4>
                    <div class="hunterArmor">
                        <table class="table" style="color: #ffffff;">
                            <thead scope="col">
                                <tr>
                                    <th scope="col">Armor</th>
                                    <th scope="col"><img src="https://www.bungie.net/common/destiny2_content/icons/e26e0e93a9daf4fdd21bf64eb9246340.png" width="40" height="40" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="top" title="Mobility"></th>
                                    <th scope="col"><img src="https://www.bungie.net/common/destiny2_content/icons/202ecc1c6febeb6b97dafc856e863140.png" width="40" height="40" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="top" title="Resilience"></th>
                                    <th scope="col"><img src="https://www.bungie.net/common/destiny2_content/icons/128eee4ee7fc127851ab32eac6ca91cf.png" width="40" height="40" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="top" title="Recovery"></th>
                                    <th scope="col"><img src="https://www.bungie.net/common/destiny2_content/icons/ca62128071dc254fe75891211b98b237.png" width="40" height="40" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="top" title="Discipline"></th>
                                    <th scope="col"><img src="https://www.bungie.net/common/destiny2_content/icons/59732534ce7060dba681d1ba84c055a6.png" width="40" height="40" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="top" title="Intellect"></th>
                                    <th scope="col"><img src="https://www.bungie.net/common/destiny2_content/icons/c7eefc8abbaa586eeab79e962a79d6ad.png" width="40" height="40" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="top" title="Strength"></th>
                                    
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <th scope="row"><img src="{HunterHelmetIcon}"  class="img"  width="100%" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="{HunterHelmetName}"></th>
                                    {HunterHelmetStatTable}
                                <tr>
                                    <th scope="row"><img src="{HunterArmsIcon}"  class="img"  width="100%" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="{HunterArmsName}"></th>
                                    {HunterArmsStatTable}
                                <tr>
                                    <th scope="row"><img src="{HunterChestIcon}"  class="img"  width="100%" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="{HunterChestName}"></th>
                                    {HunterChestStatTable}
                                <tr>
                                    <th scope="row"><img src="{HunterLegsIcon}"  class="img"  width="100%" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="{HunterLegsName}"></th>
                                    {HunterLegsStatTable}
                                <tr>
                                    <th scope="row"><img src="{HunterClassItemIcon}"  class="img"  width="100%" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="{HunterClassItemName}"></th>
                                    {HunterClassItemStatTable}
                            </tbody>
                        </table>
                    </div>
                </div>
                <div class="col-lg-4 col-md-7 overflow-auto">
                    <br>
                    <h4 style="text-align: center;">Titan Armor<hr></h4>
                    <div class="titanArmor">
                        
                        <table class="table" style="color: #ffffff;">
                            <thead scope="col">
                                <tr>
                                    <th scope="col">Armor</th>
                                    <th scope="col"><img src="https://www.bungie.net/common/destiny2_content/icons/e26e0e93a9daf4fdd21bf64eb9246340.png" width="40" height="40" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="top" title="Mobility"></th>
                                    <th scope="col"><img src="https://www.bungie.net/common/destiny2_content/icons/202ecc1c6febeb6b97dafc856e863140.png" width="40" height="40" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="top" title="Resilience"></th>
                                    <th scope="col"><img src="https://www.bungie.net/common/destiny2_content/icons/128eee4ee7fc127851ab32eac6ca91cf.png" width="40" height="40" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="top" title="Recovery"></th>
                                    <th scope="col"><img src="https://www.bungie.net/common/destiny2_content/icons/ca62128071dc254fe75891211b98b237.png" width="40" height="40" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="top" title="Discipline"></th>
                                    <th scope="col"><img src="https://www.bungie.net/common/destiny2_content/icons/59732534ce7060dba681d1ba84c055a6.png" width="40" height="40" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="top" title="Intellect"></th>
                                    <th scope="col"><img src="https://www.bungie.net/common/destiny2_content/icons/c7eefc8abbaa586eeab79e962a79d6ad.png" width="40" height="40" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="top" title="Strength"></th>
                                    
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <th scope="row"><img src="{TitanHelmetIcon}"  class="img"  width="100%" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="{TitanHelmetName}"></th>
                                    {TitanHelmetStatTable}
                                <tr>
                                    <th scope="row"><img src="{TitanArmsIcon}"  class="img"  width="100%" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="{TitanArmsName}"></th>
                                    {TitanArmsStatTable}
                                <tr>
                                    <th scope="row"><img src="{TitanChestIcon}"  class="img"  width="100%" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="{TitanChestName}"></th>
                                    {TitanChestStatTable}
                                <tr>
                                    <th scope="row"><img src="{TitanLegsIcon}"  class="img"  width="100%" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="{TitanLegsName}"></th>
                                    {TitanLegsStatTable}
                                <tr>
                                    <th scope="row"><img src="{TitanClassItemIcon}"  class="img"  width="100%" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="{TitanClassItemName}"></th>
                                    {TitanClassItemStatTable}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
        </div>
        <br>
        <br>
        <footer class="bg-dark text-center text-white">
            <div class="text-center p-3" style="background-color:#6e757d;">
              Created By:
              <a class="text-white" href="https://www.linkedin.com/in/thomas-smith-89a918192/">Thomas Smith</a> // Bungie Net: <a class="text-white" href="https://www.bungie.net/7/en/User/Profile/254/10061778?bgn=Lulamae1">Lulamae1#6072</a>
            </div>
        </footer>
        <!--Help Modal -->
        <div class="modal fade" id="infoModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true" style="color:#000000">
            <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">X&#251r Tracker - Help</h5>
                <button type="button" class="close" data-bs-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">
                        <i class="bi bi-x-lg"></i>
                    </span>
                </button>
                </div>
                <div class="modal-body">
                    <h4>Thanks for using X&#251r Tracker!</h4>
                    <hr>
                    <p>
                        <h6>
                            &#8226;Hover over an item for more information. <br><br>
                            &#8226;Yellow borders indicate a favorable perk.<br><br>
                            &#8226;Pages for each type of item (i.e. Exoitc Items, Legendary Weapons), offer more detailed data.<br><br>
                            <br> Have an issue or suggestion? Please submit it <a href="https://github.com/lulamae12/xurtracker.com/issues">here!</a>
                            
                        </h6>
                    </p>
                </div>
            </div>
            </div>
        </div>
        <!--toast script-->
        <script>
            document.addEventListener("DOMContentLoaded", function(){{
                var btn = document.getElementById("myBtn");
                var element = document.getElementById("myToast");
                //read var from local storage
                let visitedBool = localStorage.getItem("visitedToast");
                if(visitedBool == null || visitedBool == false){{
                    var myToast = new bootstrap.Toast(element);
                    localStorage.setItem("visitedToast", true);

                    //wait for a bit before showing the toast
                    setTimeout(function(){{ myToast.show(); }}, 1000);
                }}
            }});
        </script>
        <script>
            var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
            var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {{
                return new bootstrap.Popover(popoverTriggerEl)
            }})
            
            var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
            var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {{
                return new bootstrap.Tooltip(tooltipTriggerEl)
            }})
        </script>
    </body>
    </html>""".format(week=week,landingZone=landingZone,location=location,planet=planet,exoticWeaponIcon=exoticWeaponIcon,
    exoticWeaponName=exoticWeaponName,exoticWeaponType=exoticWeaponType,exoticWeaponPerkTable=exoticWeaponPerkTable,
    hawkmoonWeaponPerkTable=hawkmoonWeaponPerkTable,hawkmoonRating=hawkmoonRating,deadMansTalePerkTable=deadMansTalePerkTable,
    deadMansTaleRating=deadMansTaleRating,exoticWarlockIcon=exoticWarlockIcon,exoticWarlockName=exoticWarlockName,exoticWarlockType=exoticWarlockType,
    exoticWarlockStatTable=exoticWarlockStatTable,exoticHunterIcon=exoticHunterIcon,exoticHunterName=exoticHunterName,exoticHunterType=exoticHunterType,
    exoticHunterStatTable=exoticHunterStatTable,exoticTitanIcon=exoticTitanIcon,exoticTitanName=exoticTitanName,exoticTitanType=exoticTitanType,
    exoticTitanStatTable=exoticTitanStatTable,legendaryWeapon1Icon=legendaryWeapon1Icon,legendaryWeapon1Name=legendaryWeapon1Name,legendaryWeapon1Type=legendaryWeapon1Type,legendaryWeapon1PerkTable = legendaryWeapon1PerkTable,legendaryWeapon1Rating=legendaryWeapon1Rating,
    legendaryWeapon2Icon=legendaryWeapon2Icon,legendaryWeapon2Name=legendaryWeapon2Name,legendaryWeapon2Type=legendaryWeapon2Type,legendaryWeapon2PerkTable = legendaryWeapon2PerkTable,legendaryWeapon2Rating=legendaryWeapon2Rating,
    legendaryWeapon3Icon=legendaryWeapon3Icon,legendaryWeapon3Name=legendaryWeapon3Name,legendaryWeapon3Type=legendaryWeapon3Type,legendaryWeapon3PerkTable = legendaryWeapon3PerkTable,legendaryWeapon3Rating=legendaryWeapon3Rating,
    legendaryWeapon4Icon=legendaryWeapon4Icon,legendaryWeapon4Name=legendaryWeapon4Name,legendaryWeapon4Type=legendaryWeapon4Type,legendaryWeapon4PerkTable = legendaryWeapon4PerkTable,legendaryWeapon4Rating=legendaryWeapon4Rating,
    legendaryWeapon5Icon=legendaryWeapon5Icon,legendaryWeapon5Name=legendaryWeapon5Name,legendaryWeapon5Type=legendaryWeapon5Type,legendaryWeapon5PerkTable = legendaryWeapon5PerkTable,legendaryWeapon5Rating=legendaryWeapon5Rating,
    legendaryWeapon6Icon=legendaryWeapon6Icon,legendaryWeapon6Name=legendaryWeapon6Name,legendaryWeapon6Type=legendaryWeapon6Type,legendaryWeapon6PerkTable = legendaryWeapon6PerkTable,legendaryWeapon6Rating=legendaryWeapon6Rating,
    legendaryWeapon7Icon=legendaryWeapon7Icon,legendaryWeapon7Name=legendaryWeapon7Name,legendaryWeapon7Type=legendaryWeapon7Type,legendaryWeapon7PerkTable = legendaryWeapon7PerkTable,legendaryWeapon7Rating=legendaryWeapon7Rating,
    WarlockHelmetIcon=WarlockHelmetIcon,WarlockHelmetName=WarlockHelmetName,WarlockHelmetStatTable=WarlockHelmetStatTable,
    WarlockArmsIcon=WarlockArmsIcon,WarlockArmsName=WarlockArmsName,WarlockArmsStatTable=WarlockArmsStatTable,
    WarlockChestIcon=WarlockChestIcon,WarlockChestName=WarlockChestName,WarlockChestStatTable=WarlockChestStatTable,
    WarlockLegsIcon=WarlockLegsIcon,WarlockLegsName=WarlockLegsName,WarlockLegsStatTable=WarlockLegsStatTable,
    WarlockClassItemIcon=WarlockClassItemIcon,WarlockClassItemName=WarlockClassItemName,WarlockClassItemStatTable=WarlockClassItemStatTable,
    HunterHelmetIcon=HunterHelmetIcon,HunterHelmetName=HunterHelmetName,HunterHelmetStatTable=HunterHelmetStatTable,
    HunterArmsIcon=HunterArmsIcon,HunterArmsName=HunterArmsName,HunterArmsStatTable=HunterArmsStatTable,
    HunterChestIcon=HunterChestIcon,HunterChestName=HunterChestName,HunterChestStatTable=HunterChestStatTable,
    HunterLegsIcon=HunterLegsIcon,HunterLegsName=HunterLegsName,HunterLegsStatTable=HunterLegsStatTable,
    HunterClassItemIcon=HunterClassItemIcon,HunterClassItemName=HunterClassItemName,HunterClassItemStatTable=HunterClassItemStatTable,
    TitanHelmetIcon=TitanHelmetIcon,TitanHelmetName=TitanHelmetName,TitanHelmetStatTable=TitanHelmetStatTable,
    TitanArmsIcon=TitanArmsIcon,TitanArmsName=TitanArmsName,TitanArmsStatTable=TitanArmsStatTable,
    TitanChestIcon=TitanChestIcon,TitanChestName=TitanChestName,TitanChestStatTable=TitanChestStatTable,
    TitanLegsIcon=TitanLegsIcon,TitanLegsName=TitanLegsName,TitanLegsStatTable=TitanLegsStatTable,
    TitanClassItemIcon=TitanClassItemIcon,TitanClassItemName=TitanClassItemName,TitanClassItemStatTable=TitanClassItemStatTable,legendaryWeapon1Lore=legendaryWeapon1Lore,legendaryWeapon2Lore=legendaryWeapon2Lore,legendaryWeapon3Lore=legendaryWeapon3Lore,
    legendaryWeapon4Lore=legendaryWeapon4Lore,legendaryWeapon5Lore=legendaryWeapon5Lore,legendaryWeapon6Lore = legendaryWeapon6Lore,legendaryWeapon7Lore=legendaryWeapon7Lore,
    exoticWarlockLore=exoticWarlockLore,exoticHunterLore=exoticHunterLore,exoticTitanLore=exoticTitanLore,exoticWeaponLore=exoticWeaponLore,legendaryWeapon1DamageTypeIcon=legendaryWeapon1DamageTypeIcon,
                legendaryWeapon2DamageTypeIcon=legendaryWeapon2DamageTypeIcon,
                legendaryWeapon3DamageTypeIcon=legendaryWeapon3DamageTypeIcon,
                legendaryWeapon4DamageTypeIcon=legendaryWeapon4DamageTypeIcon,
                legendaryWeapon5DamageTypeIcon=legendaryWeapon5DamageTypeIcon,
                legendaryWeapon6DamageTypeIcon=legendaryWeapon6DamageTypeIcon,
                legendaryWeapon7DamageTypeIcon=legendaryWeapon7DamageTypeIcon,
                legendaryWeapon1DamageType=legendaryWeapon1DamageType,
                legendaryWeapon1DamageElement=legendaryWeapon1DamageElement, 
                legendaryWeapon2DamageType=legendaryWeapon2DamageType,
                legendaryWeapon2DamageElement=legendaryWeapon2DamageElement,
                legendaryWeapon3DamageType=legendaryWeapon3DamageType,
                legendaryWeapon3DamageElement=legendaryWeapon3DamageElement, 
                legendaryWeapon4DamageType=legendaryWeapon4DamageType,
                legendaryWeapon4DamageElement=legendaryWeapon4DamageElement, 
                legendaryWeapon5DamageType=legendaryWeapon5DamageType,
                legendaryWeapon5DamageElement=legendaryWeapon5DamageElement,
                legendaryWeapon6DamageType=legendaryWeapon6DamageType,
                legendaryWeapon6DamageElement=legendaryWeapon6DamageElement,
                legendaryWeapon7DamageType=legendaryWeapon7DamageType,
                legendaryWeapon7DamageElement=legendaryWeapon7DamageElement,) 

    
    htmlTemp = cleanHTML(htmlTemp)
    text_file = open("/home/ubuntu/XurTracker/templates/all_items.html", "w")
    n = text_file.write(htmlTemp)
    text_file.close()



setHtmlVals()