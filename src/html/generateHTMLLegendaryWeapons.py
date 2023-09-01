#generates html data for main.html from the json
import json
import string
from xml.dom.minidom import Element
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



def cleanHTML(html):
    
    html = html.replace("\u2022","<br>&#8226;")
    html = html.replace("\u2014","&nbsp;&#8212&nbsp;")
    html = html.replace("\u201c","&#8220;")
    html = html.replace("\u201d","&#8221;")
    html = html.replace("\u2026","&#8230;")
    html = html.replace("\u00fb","&#251;")
    cleanedHTML = html
    return cleanedHTML

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


def setHtmlVals():
    #read in the json doc
    file = open("/home/ubuntu/XurTracker/data/data.json")
    data = json.load(file)
    file.close()

    #set all vals
    week = data["Week"]
    #legendary weapons
    legendaryWeapon1Name = data["Legendaries"]["Legendary weapons"][0]["name"]
    legendaryWeapon1Type = data["Legendaries"]["Legendary weapons"][0]["type"].replace("Legendary ","")
    legendaryWeapon1Rating = data["Legendaries"]["Legendary weapons"][0]["itemRating"]
    legendaryWeapon1Icon = data["Legendaries"]["Legendary weapons"][0]["icon"]
    legendaryWeapon1Lore = data["Legendaries"]["Legendary weapons"][0]["lore"].replace('"','&quot').replace("\u2014","</em><br><br>&#8212&nbsp;")
    legendaryWeapon1PerkTable = buildWeaponPerkTable(data["Legendaries"]["Legendary weapons"][0]["weaponPerks"])
    legendaryWeapon1FrameName = data["Legendaries"]["Legendary weapons"][0]["legendWeaponFrame"]["name"]
    legendaryWeapon1FrameIcon = data["Legendaries"]["Legendary weapons"][0]["legendWeaponFrame"]["icon"]
    legendaryWeapon1FrameDesc = data["Legendaries"]["Legendary weapons"][0]["legendWeaponFrame"]["description"]
    legendaryWeapon1LoreExt = data["Legendaries"]["Legendary weapons"][0]["ExtLore"]
    legendaryWeapon1DamageType = data["Legendaries"]["Legendary weapons"][0]["legendWeaponDamageType"]
    legendaryWeapon1DamageElement = data["Legendaries"]["Legendary weapons"][0]["legendWeaponDamageElement"]
    legendaryWeapon1MasterWorkName = data["Legendaries"]["Legendary weapons"][0]["masterworkData"]["name"]
    legendaryWeapon1MasterWorkDesc = data["Legendaries"]["Legendary weapons"][0]["masterworkData"]["description"]
    legendaryWeapon1MasterWorkIcon = data["Legendaries"]["Legendary weapons"][0]["masterworkData"]["icon"]
    
    
    

    legendaryWeapon2Name = data["Legendaries"]["Legendary weapons"][1]["name"]
    legendaryWeapon2Type = data["Legendaries"]["Legendary weapons"][1]["type"].replace("Legendary ","")
    legendaryWeapon2Rating = data["Legendaries"]["Legendary weapons"][1]["itemRating"]
    legendaryWeapon2Icon = data["Legendaries"]["Legendary weapons"][1]["icon"]
    legendaryWeapon2Lore = data["Legendaries"]["Legendary weapons"][1]["lore"].replace('"','&quot').replace("\u2014","</em><br><br>&#8212&nbsp;")
    legendaryWeapon2PerkTable = buildWeaponPerkTable(data["Legendaries"]["Legendary weapons"][1]["weaponPerks"])
    legendaryWeapon2FrameName = data["Legendaries"]["Legendary weapons"][1]["legendWeaponFrame"]["name"]
    legendaryWeapon2FrameIcon = data["Legendaries"]["Legendary weapons"][1]["legendWeaponFrame"]["icon"]
    legendaryWeapon2FrameDesc = data["Legendaries"]["Legendary weapons"][1]["legendWeaponFrame"]["description"]
    legendaryWeapon2LoreExt = data["Legendaries"]["Legendary weapons"][1]["ExtLore"]
    legendaryWeapon2DamageType = data["Legendaries"]["Legendary weapons"][1]["legendWeaponDamageType"]
    legendaryWeapon2DamageElement = data["Legendaries"]["Legendary weapons"][1]["legendWeaponDamageElement"]
    legendaryWeapon2MasterWorkName = data["Legendaries"]["Legendary weapons"][1]["masterworkData"]["name"]
    legendaryWeapon2MasterWorkDesc = data["Legendaries"]["Legendary weapons"][1]["masterworkData"]["description"]
    legendaryWeapon2MasterWorkIcon = data["Legendaries"]["Legendary weapons"][1]["masterworkData"]["icon"]

    legendaryWeapon3Name = data["Legendaries"]["Legendary weapons"][2]["name"]
    legendaryWeapon3Type = data["Legendaries"]["Legendary weapons"][2]["type"].replace("Legendary ","")
    legendaryWeapon3Rating = data["Legendaries"]["Legendary weapons"][2]["itemRating"]
    legendaryWeapon3Icon = data["Legendaries"]["Legendary weapons"][2]["icon"]
    legendaryWeapon3Lore = data["Legendaries"]["Legendary weapons"][2]["lore"].replace('"','&quot').replace("\u2014","</em><br><br>&#8212&nbsp;")
    legendaryWeapon3PerkTable = buildWeaponPerkTable(data["Legendaries"]["Legendary weapons"][2]["weaponPerks"])
    legendaryWeapon3FrameName = data["Legendaries"]["Legendary weapons"][2]["legendWeaponFrame"]["name"]
    legendaryWeapon3FrameIcon = data["Legendaries"]["Legendary weapons"][2]["legendWeaponFrame"]["icon"]
    legendaryWeapon3FrameDesc = data["Legendaries"]["Legendary weapons"][2]["legendWeaponFrame"]["description"]
    legendaryWeapon3LoreExt = data["Legendaries"]["Legendary weapons"][2]["ExtLore"]
    legendaryWeapon3DamageType = data["Legendaries"]["Legendary weapons"][2]["legendWeaponDamageType"]
    legendaryWeapon3DamageElement = data["Legendaries"]["Legendary weapons"][2]["legendWeaponDamageElement"]
    legendaryWeapon3MasterWorkName = data["Legendaries"]["Legendary weapons"][2]["masterworkData"]["name"]
    legendaryWeapon3MasterWorkDesc = data["Legendaries"]["Legendary weapons"][2]["masterworkData"]["description"]
    legendaryWeapon3MasterWorkIcon = data["Legendaries"]["Legendary weapons"][2]["masterworkData"]["icon"]

    legendaryWeapon4Name = data["Legendaries"]["Legendary weapons"][3]["name"]
    legendaryWeapon4Type = data["Legendaries"]["Legendary weapons"][3]["type"].replace("Legendary ","")
    legendaryWeapon4Rating = data["Legendaries"]["Legendary weapons"][3]["itemRating"]
    legendaryWeapon4Icon = data["Legendaries"]["Legendary weapons"][3]["icon"]
    legendaryWeapon4Lore = data["Legendaries"]["Legendary weapons"][3]["lore"].replace('"','&quot').replace("\u2014","</em><br><br>&#8212&nbsp;")
    legendaryWeapon4PerkTable = buildWeaponPerkTable(data["Legendaries"]["Legendary weapons"][3]["weaponPerks"])
    legendaryWeapon4FrameName = data["Legendaries"]["Legendary weapons"][3]["legendWeaponFrame"]["name"]
    legendaryWeapon4FrameIcon = data["Legendaries"]["Legendary weapons"][3]["legendWeaponFrame"]["icon"]
    legendaryWeapon4FrameDesc = data["Legendaries"]["Legendary weapons"][3]["legendWeaponFrame"]["description"]
    legendaryWeapon4LoreExt = data["Legendaries"]["Legendary weapons"][3]["ExtLore"]
    legendaryWeapon4DamageType = data["Legendaries"]["Legendary weapons"][3]["legendWeaponDamageType"]
    legendaryWeapon4DamageElement = data["Legendaries"]["Legendary weapons"][3]["legendWeaponDamageElement"]
    legendaryWeapon4MasterWorkName = data["Legendaries"]["Legendary weapons"][3]["masterworkData"]["name"]
    legendaryWeapon4MasterWorkDesc = data["Legendaries"]["Legendary weapons"][3]["masterworkData"]["description"]
    legendaryWeapon4MasterWorkIcon = data["Legendaries"]["Legendary weapons"][3]["masterworkData"]["icon"]

    legendaryWeapon5Name = data["Legendaries"]["Legendary weapons"][4]["name"]
    legendaryWeapon5Type = data["Legendaries"]["Legendary weapons"][4]["type"].replace("Legendary ","")
    legendaryWeapon5Rating = data["Legendaries"]["Legendary weapons"][4]["itemRating"]
    legendaryWeapon5Icon = data["Legendaries"]["Legendary weapons"][4]["icon"]
    legendaryWeapon5Lore = data["Legendaries"]["Legendary weapons"][4]["lore"].replace('"','&quot').replace("\u2014","</em><br><br>&#8212&nbsp;")
    legendaryWeapon5PerkTable = buildWeaponPerkTable(data["Legendaries"]["Legendary weapons"][4]["weaponPerks"])
    legendaryWeapon5FrameName = data["Legendaries"]["Legendary weapons"][4]["legendWeaponFrame"]["name"]
    legendaryWeapon5FrameIcon = data["Legendaries"]["Legendary weapons"][4]["legendWeaponFrame"]["icon"]
    legendaryWeapon5FrameDesc = data["Legendaries"]["Legendary weapons"][4]["legendWeaponFrame"]["description"]
    legendaryWeapon5LoreExt = data["Legendaries"]["Legendary weapons"][4]["ExtLore"]
    legendaryWeapon5DamageType = data["Legendaries"]["Legendary weapons"][4]["legendWeaponDamageType"]
    legendaryWeapon5DamageElement = data["Legendaries"]["Legendary weapons"][4]["legendWeaponDamageElement"]
    legendaryWeapon5MasterWorkName = data["Legendaries"]["Legendary weapons"][4]["masterworkData"]["name"]
    legendaryWeapon5MasterWorkDesc = data["Legendaries"]["Legendary weapons"][4]["masterworkData"]["description"]
    legendaryWeapon5MasterWorkIcon = data["Legendaries"]["Legendary weapons"][4]["masterworkData"]["icon"]

    legendaryWeapon6Name = data["Legendaries"]["Legendary weapons"][5]["name"]
    legendaryWeapon6Type = data["Legendaries"]["Legendary weapons"][5]["type"].replace("Legendary ","").replace("Legendary ","")
    legendaryWeapon6Rating = data["Legendaries"]["Legendary weapons"][5]["itemRating"]
    legendaryWeapon6Icon = data["Legendaries"]["Legendary weapons"][5]["icon"]
    legendaryWeapon6Lore = data["Legendaries"]["Legendary weapons"][5]["lore"].replace('"','&quot').replace("\u2014","</em><br><br>&#8212&nbsp;")
    legendaryWeapon6PerkTable = buildWeaponPerkTable(data["Legendaries"]["Legendary weapons"][5]["weaponPerks"])
    legendaryWeapon6FrameName = data["Legendaries"]["Legendary weapons"][5]["legendWeaponFrame"]["name"]
    legendaryWeapon6FrameIcon = data["Legendaries"]["Legendary weapons"][5]["legendWeaponFrame"]["icon"]
    legendaryWeapon6FrameDesc = data["Legendaries"]["Legendary weapons"][5]["legendWeaponFrame"]["description"]
    legendaryWeapon6LoreExt = data["Legendaries"]["Legendary weapons"][5]["ExtLore"]
    legendaryWeapon6DamageType = data["Legendaries"]["Legendary weapons"][5]["legendWeaponDamageType"]
    legendaryWeapon6DamageElement = data["Legendaries"]["Legendary weapons"][5]["legendWeaponDamageElement"]
    legendaryWeapon6MasterWorkName = data["Legendaries"]["Legendary weapons"][5]["masterworkData"]["name"]
    legendaryWeapon6MasterWorkDesc = data["Legendaries"]["Legendary weapons"][5]["masterworkData"]["description"]
    legendaryWeapon6MasterWorkIcon = data["Legendaries"]["Legendary weapons"][5]["masterworkData"]["icon"]

    legendaryWeapon7Name = data["Legendaries"]["Legendary weapons"][6]["name"]
    legendaryWeapon7Type = data["Legendaries"]["Legendary weapons"][6]["type"].replace("Legendary ","")
    legendaryWeapon7Rating = data["Legendaries"]["Legendary weapons"][6]["itemRating"]
    legendaryWeapon7Icon = data["Legendaries"]["Legendary weapons"][6]["icon"]
    legendaryWeapon7Lore = data["Legendaries"]["Legendary weapons"][6]["lore"].replace('"','&quot').replace("\u2014","</em><br><br>&#8212&nbsp;")
    legendaryWeapon7PerkTable = buildWeaponPerkTable(data["Legendaries"]["Legendary weapons"][6]["weaponPerks"])
    legendaryWeapon7FrameName = data["Legendaries"]["Legendary weapons"][6]["legendWeaponFrame"]["name"]
    legendaryWeapon7FrameIcon = data["Legendaries"]["Legendary weapons"][6]["legendWeaponFrame"]["icon"]
    legendaryWeapon7FrameDesc = data["Legendaries"]["Legendary weapons"][6]["legendWeaponFrame"]["description"]
    legendaryWeapon7LoreExt = data["Legendaries"]["Legendary weapons"][6]["ExtLore"]
    legendaryWeapon7DamageType = data["Legendaries"]["Legendary weapons"][6]["legendWeaponDamageType"]
    legendaryWeapon7DamageElement = data["Legendaries"]["Legendary weapons"][6]["legendWeaponDamageElement"]
    legendaryWeapon7MasterWorkName = data["Legendaries"]["Legendary weapons"][6]["masterworkData"]["name"]
    legendaryWeapon7MasterWorkDesc = data["Legendaries"]["Legendary weapons"][6]["masterworkData"]["description"]
    legendaryWeapon7MasterWorkIcon = data["Legendaries"]["Legendary weapons"][6]["masterworkData"]["icon"]

    legendaryWeapon1LoreExt = str(legendaryWeapon1LoreExt).replace("\n","<br>")
    legendaryWeapon2LoreExt = str(legendaryWeapon2LoreExt).replace("\n","<br>")
    legendaryWeapon3LoreExt = str(legendaryWeapon3LoreExt).replace("\n","<br>")
    legendaryWeapon4LoreExt = str(legendaryWeapon4LoreExt).replace("\n","<br>")
    legendaryWeapon5LoreExt = str(legendaryWeapon5LoreExt).replace("\n","<br>")
    legendaryWeapon6LoreExt = str(legendaryWeapon6LoreExt).replace("\n","<br>")
    legendaryWeapon7LoreExt = str(legendaryWeapon7LoreExt).replace("\n","<br>")
    
    loreList = [legendaryWeapon1LoreExt,legendaryWeapon2LoreExt,legendaryWeapon3LoreExt,legendaryWeapon4LoreExt,legendaryWeapon5LoreExt,legendaryWeapon6LoreExt,legendaryWeapon7LoreExt]
    damageElementList = [legendaryWeapon1DamageElement,legendaryWeapon2DamageElement,legendaryWeapon3DamageElement,legendaryWeapon4DamageElement,legendaryWeapon5DamageElement,legendaryWeapon6DamageElement,legendaryWeapon7DamageElement]
    damageTypeList = [legendaryWeapon1DamageType,legendaryWeapon2DamageType,legendaryWeapon3DamageType,legendaryWeapon4DamageType,legendaryWeapon5DamageType,legendaryWeapon6DamageType,legendaryWeapon7DamageType]
    iconList = []
    damageStrList = []

    for i in range(len(loreList)):
        if(loreList[i] == "None"):
            loreList[i] = "This weapon has no known lore. Perhaps it was lost long ago?"

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


    
    legendaryWeapon1LoreExt = loreList[0]
    legendaryWeapon2LoreExt = loreList[1]
    legendaryWeapon3LoreExt = loreList[2]
    legendaryWeapon4LoreExt = loreList[3]
    legendaryWeapon5LoreExt = loreList[4]
    legendaryWeapon6LoreExt = loreList[5]
    legendaryWeapon7LoreExt = loreList[6]


    htmlTemp ="""
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <title>X&#251r Tracker // Weapons</title>
    <link rel="shortcut icon" href="../static/favicon.ico">
    <link rel="apple-touch-icon" sizes="192x192" href="../static/favicon.ico">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.3/font/bootstrap-icons.css">
    <link rel="canonical" href="https://www.xurtracker.com/legendary-weapons"/>
    <meta charset="utf-8" ;>
    <meta name="description" content="Tracks Destiny 2's X&#251r location and inventory.">
    <meta name="keywords" content="xur,Xûr,Xur,xurtracker,wtfix,exotic inventory,destiny,destinythegame,whereisxur,destiny 2,D2,d2,where is xur,xur location,xurtrack,xur inventory">
    <meta name="author" content="Thomas Smith">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!--Bootstrap CDN CSS-->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <!--Bootstrap CDN JS-->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    <!--FA CDN-->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css"
        integrity="sha512-KfkfwYDsLkIlwQp6LFnl8zNdLGxu9YAA1QvwINks4PhcElQSvqcyVLLD9aMhXd13uQjoXtEKNosOWaZqXgel0g=="
        crossorigin="anonymous" referrerpolicy="no-referrer" />
    <nav class="navbar navbar-expand-lg navbar-light bg-secondary text-white">
        <div class="container-fluid">
            <a class="navbar-brand mb-0 h1" href="https://www.xurtracker.com">X&#251r Tracker</a>
            <button class="navbar-toggler" style="margin-right:5px !important;" type="button" data-bs-toggle="collapse"
                data-bs-target="#navbarSupportedContent">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <div class="navbar-nav">
                    <a class="nav-link active" href="all">All Items</a>
                    <a class="nav-link active" href="exotics">Exotic Items</a>
                    <a class="nav-link active" aria-current="page" href="legendary-weapons">Legendary Weapons</a>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle active" href="#" id="navbarDropdownMenuLink" role="button"
                            data-bs-toggle="dropdown" aria-expanded="false">
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
                        <a class="navbar-brand mb-0" href="https://github.com/tlstommy/xurtracker.com" target="_blank" rel="noopener noreferrer">
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
        body {{
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
</head>

<body style="background-color:  #000000; overflow: auto;"></body>
<div class="container">
    <div class="row ">
        <div class="col-12">
            <br>
            <br>
            <h1 style="text-align:center;">
                X&#251r's Legendary Weapons for {week}
                <hr>
            </h1>
            <br>
            <br>
        </div>
    </div>
</div>
<div class="container">
    <div class="row justify-content-around" style="word-break:normal; width: 100%;">
        <div class="col-lg-3 col-md-6">
            <br>
            <img src="{legendaryWeapon1Icon}" class="img" alt="legendaryWeapon">

            <div class="weaponData">
                <b>{legendaryWeapon1Name}</b>
                <p>{legendaryWeapon1Type}</p>
                <div class="d-flex p-3">
                    <i style="height: 125px;">{legendaryWeapon1Lore}</i>
                </div>
                <br>
                <table class="table-dark table-borderless">
                    <thead style="border-bottom:solid 1px white;">

                        <tr>
                            <th scope="col" style="white-space: nowrap; max-width: 50px;">Weapon Data</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td style="word-break:normal;">
                                <img src="{legendaryWeapon1DamageTypeIcon}" width="40" height="40"
                                    style="border:solid 0px yellow; border-radius: 40px;" data-bs-toggle="tooltip"
                                    data-bs-html="true" data-bs-placement="left"
                                    title="<p>This weapon deals {legendaryWeapon1DamageElement} damage.</p>">
                            </td>
                            <td style="word-break:normal;">
                                {legendaryWeapon1DamageType} Archetype
                            </td>
                        </tr>
                        <tr>
                            <td style="word-break:normal;">
                                <img src="{legendaryWeapon1FrameIcon}" width="40" height="40"
                                    style="border:solid 0px yellow; border-radius: 40px;" data-bs-toggle="tooltip"
                                    data-bs-html="true" data-bs-placement="left"
                                    title="<p>{legendaryWeapon1FrameDesc}</p>">
                            </td>
                            <td style="word-break:normal;">
                                {legendaryWeapon1FrameName}
                            </td>
                        </tr>
                        <tr>
                            <td style="word-break:normal;">
                                <img src="{legendaryWeapon1MasterWorkIcon}" width="40" height="40"
                                    style="border:solid 0px yellow;" data-bs-toggle="tooltip" data-bs-html="true"
                                    data-bs-placement="left" title="<p>{legendaryWeapon1MasterWorkDesc}</p>">
                            </td>
                            <td style="word-break:normal;">
                                {legendaryWeapon1MasterWorkName} Masterwork
                            </td>
                        </tr>

                    </tbody>
                </table>
                <br>

                <table class="table-sm table-borderless">
                    <thead style="border-bottom:solid 1px white;">
                        <tr>
                            <th scope="col" style="white-space: nowrap; max-width: 50px;">Weapon Perks</th>
                        </tr>
                    </thead>
                    <tbody style="height: 250px;">
                        {legendaryWeapon1PerkTable}
                    </tbody>
                </table>
                </img>
                <br>
                <div class="accordion" id="legendWeaponlore1" style="margin-top: -2px;">
                    <div class="accordion-item" style="background-color: #0e1010; border-color: #ffffff;">
                        <h2 class="accordion-header" id="headingOne"
                            style="background-color: #0e1010; border-color: #ffffff;">
                            <button class="accordion-button" type="button" data-bs-toggle="collapse"
                                style="background-color: #0e1010; color: #ffffff;" data-bs-target="#collapseOne"
                                aria-expanded="true" aria-controls="collapseOne">
                                {legendaryWeapon1Name} Lore
                            </button>
                        </h2>
                        <div id="collapseOne" class="accordion-collapse collapse" aria-labelledby="headingOne"
                            data-bs-parent="#accordionExample">
                            <div class="accordion-body" style="word-wrap: break-word;">
                                <p>
                                <h2>{legendaryWeapon1Name}</h2>
                                <hr>
                                <h6>{legendaryWeapon1LoreExt}</h6>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="col-lg-3 col-md-6">
            <br>
            <img src="{legendaryWeapon2Icon}" class="img" alt="legendaryWeapon">

            <div class="weaponData">
                <b>{legendaryWeapon2Name}</b>
                <p>{legendaryWeapon2Type}</p>
                <div class="d-flex p-3">
                    <i style="height: 125px;">{legendaryWeapon2Lore}</i>
                </div>
                <br>
                <table class="table-dark table-borderless">
                    <thead style="border-bottom:solid 1px white;">

                        <tr>
                            <th scope="col" style="white-space: nowrap; max-width: 50px;">Weapon Data</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td style="word-break:normal;">
                                <img src="{legendaryWeapon2DamageTypeIcon}" width="40" height="40"
                                    style="border:solid 0px yellow; border-radius: 40px;" data-bs-toggle="tooltip"
                                    data-bs-html="true" data-bs-placement="left"
                                    title="<p>This weapon deals {legendaryWeapon2DamageElement} damage.</p>">
                            </td>
                            <td style="word-break:normal;">
                                {legendaryWeapon2DamageType} Archetype
                            </td>
                        </tr>
                        <tr>
                            <td style="word-break:normal;">
                                <img src="{legendaryWeapon2FrameIcon}" width="40" height="40"
                                    style="border:solid 0px yellow; border-radius: 40px;" data-bs-toggle="tooltip"
                                    data-bs-html="true" data-bs-placement="left"
                                    title="<p>{legendaryWeapon2FrameDesc}</p>">
                            </td>
                            <td style="word-break:normal;">
                                {legendaryWeapon2FrameName}
                            </td>
                        </tr>
                        <tr>
                            <td style="word-break:normal;">
                                <img src="{legendaryWeapon2MasterWorkIcon}" width="40" height="40"
                                    style="border:solid 0px yellow;" data-bs-toggle="tooltip" data-bs-html="true"
                                    data-bs-placement="left" title="<p>{legendaryWeapon2MasterWorkDesc}</p>">
                            </td>
                            <td style="word-break:normal;">
                                {legendaryWeapon2MasterWorkName} Masterwork
                            </td>
                        </tr>

                    </tbody>
                </table>
                <br>

                <table class="table-sm table-borderless">
                    <thead style="border-bottom:solid 1px white;">
                        <tr>
                            <th scope="col" style="white-space: nowrap; max-width: 50px;">Weapon Perks</th>
                        </tr>
                    </thead>
                    <tbody style="height: 250px;">
                        {legendaryWeapon2PerkTable}
                    </tbody>
                </table>
                </img>
                <br>
                <div class="accordion" id="legendWeaponlore2" style="margin-top: -2px;">
                    <div class="accordion-item" style="background-color: #0e1010; border-color: #ffffff;">
                        <h2 class="accordion-header" id="heading2"
                            style="background-color: #0e1010; border-color: #ffffff;">
                            <button class="accordion-button" type="button" data-bs-toggle="collapse"
                                style="background-color: #0e1010; color: #ffffff;" data-bs-target="#collapse2"
                                aria-expanded="true" aria-controls="collapse2">
                                {legendaryWeapon2Name} Lore
                            </button>
                        </h2>
                        <div id="collapse2" class="accordion-collapse collapse" aria-labelledby="heading2"
                            data-bs-parent="#accordionExample">
                            <div class="accordion-body" style="word-wrap: break-word;">
                                <p>
                                <h2>{legendaryWeapon2Name}</h2>
                                <hr>
                                <h6>{legendaryWeapon2LoreExt}</h6>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="col-lg-3 col-md-6">
            <br>
            <img src="{legendaryWeapon3Icon}" class="img" alt="legendaryWeapon">

            <div class="weaponData">
                <b>{legendaryWeapon3Name}</b>
                <p>{legendaryWeapon3Type}</p>
                <div class="d-flex p-3">
                    <i style="height: 125px;">{legendaryWeapon3Lore}</i>
                </div>
                <br>
                <table class="table-dark table-borderless">
                    <thead style="border-bottom:solid 1px white;">

                        <tr>
                            <th scope="col" style="white-space: nowrap; max-width: 50px;">Weapon Data</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td style="word-break:normal;">
                                <img src="{legendaryWeapon3DamageTypeIcon}" width="40" height="40"
                                    style="border:solid 0px yellow; border-radius: 40px;" data-bs-toggle="tooltip"
                                    data-bs-html="true" data-bs-placement="left"
                                    title="<p>This weapon deals {legendaryWeapon3DamageElement} damage.</p>">
                            </td>
                            <td style="word-break:normal;">
                                {legendaryWeapon3DamageType} Archetype
                            </td>
                        </tr>
                        <tr>
                            <td style="word-break:normal;">
                                <img src="{legendaryWeapon3FrameIcon}" width="40" height="40"
                                    style="border:solid 0px yellow; border-radius: 40px;" data-bs-toggle="tooltip"
                                    data-bs-html="true" data-bs-placement="left"
                                    title="<p>{legendaryWeapon3FrameDesc}</p>">
                            </td>
                            <td style="word-break:normal;">
                                {legendaryWeapon3FrameName}
                            </td>
                        </tr>
                        <tr>
                            <td style="word-break:normal;">
                                <img src="{legendaryWeapon3MasterWorkIcon}" width="40" height="40"
                                    style="border:solid 0px yellow;" data-bs-toggle="tooltip" data-bs-html="true"
                                    data-bs-placement="left" title="<p>{legendaryWeapon3MasterWorkDesc}</p>">
                            </td>
                            <td style="word-break:normal;">
                                {legendaryWeapon3MasterWorkName} Masterwork
                            </td>
                        </tr>

                    </tbody>
                </table>
                <br>

                <table class="table-sm table-borderless">
                    <thead style="border-bottom:solid 1px white;">
                        <tr>
                            <th scope="col" style="white-space: nowrap; max-width: 50px;">Weapon Perks</th>
                        </tr>
                    </thead>
                    <tbody style="height: 250px;">
                        {legendaryWeapon3PerkTable}
                    </tbody>
                </table>
                </img>
                <br>
                <div class="accordion" id="legendWeaponlore3" style="margin-top: -2px;">
                    <div class="accordion-item" style="background-color: #0e1010; border-color: #ffffff;">
                        <h2 class="accordion-header" id="heading3"
                            style="background-color: #0e1010; border-color: #ffffff;">
                            <button class="accordion-button" type="button" data-bs-toggle="collapse"
                                style="background-color: #0e1010; color: #ffffff;" data-bs-target="#collapse3"
                                aria-expanded="true" aria-controls="collapse3">
                                {legendaryWeapon3Name} Lore
                            </button>
                        </h2>
                        <div id="collapse3" class="accordion-collapse collapse" aria-labelledby="heading3"
                            data-bs-parent="#accordionExample">
                            <div class="accordion-body" style="word-wrap: break-word;">
                                <p>
                                <h2>{legendaryWeapon3Name}</h2>
                                <hr>
                                <h6>{legendaryWeapon3LoreExt}</h6>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="col-lg-3 col-md-6">
            <br>
            <img src="{legendaryWeapon4Icon}" class="img" alt="legendaryWeapon">

            <div class="WeaponData">
                <b>{legendaryWeapon4Name}</b>
                <p>{legendaryWeapon4Type}</p>
                <div class="d-flex p-3">
                    <i style="height: 125px;">{legendaryWeapon4Lore}</i>
                </div>
                <br>
                <table class="table-dark table-borderless">
                    <thead style="border-bottom:solid 1px white;">

                        <tr>
                            <th scope="col" style="white-space: nowrap; max-width: 50px;">Weapon Data</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td style="word-break:normal;">
                                <img src="{legendaryWeapon4DamageTypeIcon}" width="40" height="40"
                                    style="border:solid 0px yellow; border-radius: 40px;" data-bs-toggle="tooltip"
                                    data-bs-html="true" data-bs-placement="left"
                                    title="<p>This Weapon deals {legendaryWeapon4DamageElement} damage.</p>">
                            </td>
                            <td style="word-break:normal;">
                                {legendaryWeapon4DamageType} Archetype
                            </td>
                        </tr>
                        <tr>
                            <td style="word-break:normal;">
                                <img src="{legendaryWeapon4FrameIcon}" width="40" height="40"
                                    style="border:solid 0px yellow; border-radius: 40px;" data-bs-toggle="tooltip"
                                    data-bs-html="true" data-bs-placement="left"
                                    title="<p>{legendaryWeapon4FrameDesc}</p>">
                            </td>
                            <td style="word-break:normal;">
                                {legendaryWeapon4FrameName}
                            </td>
                        </tr>
                        <tr>
                            <td style="word-break:normal;">
                                <img src="{legendaryWeapon4MasterWorkIcon}" width="40" height="40"
                                    style="border:solid 0px yellow;" data-bs-toggle="tooltip" data-bs-html="true"
                                    data-bs-placement="left" title="<p>{legendaryWeapon4MasterWorkDesc}</p>">
                            </td>
                            <td style="word-break:normal;">
                                {legendaryWeapon4MasterWorkName} Masterwork
                            </td>
                        </tr>

                    </tbody>
                </table>
                <br>

                <table class="table-sm table-borderless">
                    <thead style="border-bottom:solid 1px white;">
                        <tr>
                            <th scope="col" style="white-space: nowrap; max-width: 50px;">Weapon Perks</th>
                        </tr>
                    </thead>
                    <tbody style="height: 250px;">
                        {legendaryWeapon4PerkTable}
                    </tbody>
                </table>
                </img>
                <br>
                <div class="accordion" id="legendWeaponlore4" style="margin-top: -2px;">
                    <div class="accordion-item" style="background-color: #0e1010; border-color: #ffffff;">
                        <h2 class="accordion-header" id="heading4"
                            style="background-color: #0e1010; border-color: #ffffff;">
                            <button class="accordion-button" type="button" data-bs-toggle="collapse"
                                style="background-color: #0e1010; color: #ffffff;" data-bs-target="#collapse4"
                                aria-expanded="true" aria-controls="collapse4">
                                {legendaryWeapon4Name} Lore
                            </button>
                        </h2>
                        <div id="collapse4" class="accordion-collapse collapse" aria-labelledby="heading4"
                            data-bs-parent="#accordionExample">
                            <div class="accordion-body" style="word-wrap: break-word;">
                                <p>
                                <h2>{legendaryWeapon4Name}</h2>
                                <hr>
                                <h6>{legendaryWeapon4LoreExt}</h6>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <br>
    <br>
    <br>
    <div class="d-flex justify-content-evenly">
        <div class="row" style="word-break:normal; width: 100%;">

            <div class="col-lg-4 col-md-6 justify-content-start">
                <br>
                <img src="{legendaryWeapon5Icon}" class="img" alt="legendaryWeapon">

                <div class="weaponData">
                    <b>{legendaryWeapon5Name}</b>
                    <p>{legendaryWeapon5Type}</p>
                    <div class="d-flex p-3">
                        <i style="height: 125px;">{legendaryWeapon5Lore}</i>
                    </div>
                    <br>
                    <table class="table-dark table-borderless">
                        <thead style="border-bottom:solid 1px white;">

                            <tr>
                                <th scope="col" style="white-space: nowrap; max-width: 50px;">Weapon Data</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td style="word-break:normal;">
                                    <img src="{legendaryWeapon5DamageTypeIcon}" width="40" height="40"
                                        style="border:solid 0px yellow; border-radius: 40px;" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="<p>This weapon deals {legendaryWeapon5DamageElement} damage.</p>">
                                </td>
                                <td style="word-break:normal;">
                                    {legendaryWeapon5DamageType} Archetype
                                </td>
                            </tr>
                            <tr>
                                <td style="word-break:normal;">
                                    <img src="{legendaryWeapon5FrameIcon}" width="40" height="40"
                                        style="border:solid 0px yellow; border-radius: 40px;" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="<p>{legendaryWeapon5FrameDesc}</p>">
                                </td>
                                <td style="word-break:normal;">
                                    {legendaryWeapon5FrameName}
                                </td>
                            </tr>
                            <tr>
                                <td style="word-break:normal;">
                                    <img src="{legendaryWeapon5MasterWorkIcon}" width="40" height="40"
                                        style="border:solid 0px yellow;" data-bs-toggle="tooltip" data-bs-html="true"
                                        data-bs-placement="left" title="<p>{legendaryWeapon5MasterWorkDesc}</p>">
                                </td>
                                <td style="word-break:normal;">
                                    {legendaryWeapon5MasterWorkName} Masterwork
                                </td>
                            </tr>

                        </tbody>
                    </table>
                    <br>

                    <table class="table-sm table-borderless">
                        <thead style="border-bottom:solid 1px white;">
                            <tr>
                                <th scope="col" style="white-space: nowrap; max-width: 50px;">Weapon Perks</th>
                            </tr>
                        </thead>
                        <tbody style="height: 250px;">
                            {legendaryWeapon5PerkTable}
                        </tbody>
                    </table>
                    </img>
                    <br>
                    <div class="accordion" id="legendWeaponlore5" style="margin-top: -2px;">
                        <div class="accordion-item" style="background-color: #0e1010; border-color: #ffffff;">
                            <h2 class="accordion-header" id="heading5"
                                style="background-color: #0e1010; border-color: #ffffff;">
                                <button class="accordion-button" type="button" data-bs-toggle="collapse"
                                    style="background-color: #0e1010; color: #ffffff;" data-bs-target="#collapse5"
                                    aria-expanded="true" aria-controls="collapse5">
                                    {legendaryWeapon5Name} Lore
                                </button>
                            </h2>
                            <div id="collapse5" class="accordion-collapse collapse" aria-labelledby="heading5"
                                data-bs-parent="#accordionExample">
                                <div class="accordion-body" style="word-wrap: break-word;">
                                    <p>
                                    <h2>{legendaryWeapon5Name}</h2>
                                    <hr>
                                    <h6>{legendaryWeapon5LoreExt}</h6>
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="col-lg-4 col-md-6">
                <br>
                <img src="{legendaryWeapon6Icon}" class="img" alt="legendaryWeapon">

                <div class="weaponData">
                    <b>{legendaryWeapon6Name}</b>
                    <p>{legendaryWeapon6Type}</p>
                    <div class="d-flex p-3">
                        <i style="height: 125px;">{legendaryWeapon6Lore}</i>
                    </div>
                    <br>
                    <table class="table-dark table-borderless">
                        <thead style="border-bottom:solid 1px white;">

                            <tr>
                                <th scope="col" style="white-space: nowrap; max-width: 50px;">Weapon Data</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td style="word-break:normal;">
                                    <img src="{legendaryWeapon6DamageTypeIcon}" width="40" height="40"
                                        style="border:solid 0px yellow; border-radius: 40px;" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="<p>This weapon deals {legendaryWeapon6DamageElement} damage.</p>">
                                </td>
                                <td style="word-break:normal;">
                                    {legendaryWeapon6DamageType} Archetype
                                </td>
                            </tr>
                            <tr>
                                <td style="word-break:normal;">
                                    <img src="{legendaryWeapon6FrameIcon}" width="40" height="40"
                                        style="border:solid 0px yellow; border-radius: 40px;" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="<p>{legendaryWeapon6FrameDesc}</p>">
                                </td>
                                <td style="word-break:normal;">
                                    {legendaryWeapon6FrameName}
                                </td>
                            </tr>
                            <tr>
                                <td style="word-break:normal;">
                                    <img src="{legendaryWeapon6MasterWorkIcon}" width="40" height="40"
                                        style="border:solid 0px yellow;" data-bs-toggle="tooltip" data-bs-html="true"
                                        data-bs-placement="left" title="<p>{legendaryWeapon6MasterWorkDesc}</p>">
                                </td>
                                <td style="word-break:normal;">
                                    {legendaryWeapon6MasterWorkName} Masterwork
                                </td>
                            </tr>

                        </tbody>
                    </table>
                    <br>

                    <table class="table-sm table-borderless">
                        <thead style="border-bottom:solid 1px white;">
                            <tr>
                                <th scope="col" style="white-space: nowrap; max-width: 50px;">Weapon Perks</th>
                            </tr>
                        </thead>
                        <tbody style="height: 250px;">
                            {legendaryWeapon6PerkTable}
                        </tbody>
                    </table>
                    </img>
                    <br>
                    <div class="accordion" id="legendWeaponlore6" style="margin-top: -2px;">
                        <div class="accordion-item" style="background-color: #0e1010; border-color: #ffffff;">
                            <h2 class="accordion-header" id="heading6"
                                style="background-color: #0e1010; border-color: #ffffff;">
                                <button class="accordion-button" type="button" data-bs-toggle="collapse"
                                    style="background-color: #0e1010; color: #ffffff;" data-bs-target="#collapse6"
                                    aria-expanded="true" aria-controls="collapse6">
                                    {legendaryWeapon6Name} Lore
                                </button>
                            </h2>
                            <div id="collapse6" class="accordion-collapse collapse" aria-labelledby="heading6"
                                data-bs-parent="#accordionExample">
                                <div class="accordion-body" style="word-wrap: break-word;">
                                    <p>
                                    <h2>{legendaryWeapon6Name}</h2>
                                    <hr>
                                    <h6>{legendaryWeapon6LoreExt}</h6>
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="col-lg-4 col-md-6">
                <br>
                <img src="{legendaryWeapon7Icon}" class="img" alt="legendaryWeapon">

                <div class="weaponData">
                    <b>{legendaryWeapon7Name}</b>
                    <p>{legendaryWeapon7Type}</p>
                    <div class="d-flex p-3">
                        <i style="height: 125px;">{legendaryWeapon7Lore}</i>
                    </div>
                    <br>
                    <table class="table-dark table-borderless">
                        <thead style="border-bottom:solid 1px white;">

                            <tr>
                                <th scope="col" style="white-space: nowrap; max-width: 50px;">Weapon Data</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td style="word-break:normal;">
                                    <img src="{legendaryWeapon7DamageTypeIcon}" width="40" height="40"
                                        style="border:solid 0px yellow; border-radius: 40px;" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="<p>This weapon deals {legendaryWeapon7DamageElement} damage.</p>">
                                </td>
                                <td style="word-break:normal;">
                                    {legendaryWeapon7DamageType} Archetype
                                </td>
                            </tr>
                            <tr>
                                <td style="word-break:normal;">
                                    <img src="{legendaryWeapon7FrameIcon}" width="40" height="40"
                                        style="border:solid 0px yellow; border-radius: 40px;" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="<p>{legendaryWeapon7FrameDesc}</p>">
                                </td>
                                <td style="word-break:normal;">
                                    {legendaryWeapon7FrameName}
                                </td>
                            </tr>
                            <tr>
                                <td style="word-break:normal;">
                                    <img src="{legendaryWeapon7MasterWorkIcon}" width="40" height="40"
                                        style="border:solid 0px yellow;" data-bs-toggle="tooltip" data-bs-html="true"
                                        data-bs-placement="left" title="<p>{legendaryWeapon7MasterWorkDesc}</p>">
                                </td>
                                <td style="word-break:normal;">
                                    {legendaryWeapon7MasterWorkName} Masterwork
                                </td>
                            </tr>

                        </tbody>
                    </table>
                    <br>

                    <table class="table-sm table-borderless">
                        <thead style="border-bottom:solid 1px white;">
                            <tr>
                                <th scope="col" style="white-space: nowrap; max-width: 50px;">Weapon Perks</th>
                            </tr>
                        </thead>
                        <tbody style="height: 250px;">
                            {legendaryWeapon7PerkTable}
                        </tbody>
                    </table>
                    </img>
                    <br>
                    <div class="accordion" id="legendWeaponlore7" style="margin-top: -2px;">
                        <div class="accordion-item" style="background-color: #0e1010; border-color: #ffffff;">
                            <h2 class="accordion-header" id="heading7"
                                style="background-color: #0e1010; border-color: #ffffff;">
                                <button class="accordion-button" type="button" data-bs-toggle="collapse"
                                    style="background-color: #0e1010; color: #ffffff;" data-bs-target="#collapse7"
                                    aria-expanded="true" aria-controls="collapse7">
                                    {legendaryWeapon7Name} Lore
                                </button>
                            </h2>
                            <div id="collapse7" class="accordion-collapse collapse" aria-labelledby="heading7"
                                data-bs-parent="#accordionExample">
                                <div class="accordion-body" style="word-wrap: break-word;">
                                    <p>
                                    <h2>{legendaryWeapon7Name}</h2>
                                    <hr>
                                    <h6>{legendaryWeapon7LoreExt}</h6>
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
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
        <a class="text-white" href="https://www.linkedin.com/in/thomas-smith-89a918192/">Thomas Smith</a> // Bungie Net:
        <a class="text-white" href="https://www.bungie.net/7/en/User/Profile/254/10061778?bgn=Lulamae1">Lulamae1#6072</a>
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
                    <br> Have an issue or suggestion? Please submit it <a href="https://github.com/tlstommy/xurtracker.com/issues">here!</a>
                    
                </h6>
            </p>
        </div>
    </div>
    </div>
</div>
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
</html>
    """.format(week=week,legendaryWeapon1Name=legendaryWeapon1Name,
                legendaryWeapon1Type=legendaryWeapon1Type,
                legendaryWeapon1Rating=legendaryWeapon1Rating,
                legendaryWeapon1Icon=legendaryWeapon1Icon,
                legendaryWeapon1Lore=legendaryWeapon1Lore,
                legendaryWeapon1PerkTable=legendaryWeapon1PerkTable,
                legendaryWeapon1FrameName=legendaryWeapon1FrameName,
                legendaryWeapon1FrameIcon=legendaryWeapon1FrameIcon, 
                legendaryWeapon1FrameDesc=legendaryWeapon1FrameDesc,
                legendaryWeapon1LoreExt=legendaryWeapon1LoreExt,
                legendaryWeapon1DamageType=legendaryWeapon1DamageType,
                legendaryWeapon1DamageElement=legendaryWeapon1DamageElement, 
                legendaryWeapon1MasterWorkName=legendaryWeapon1MasterWorkName,
                legendaryWeapon1MasterWorkDesc=legendaryWeapon1MasterWorkDesc,
                legendaryWeapon1MasterWorkIcon=legendaryWeapon1MasterWorkIcon,
                legendaryWeapon2Name=legendaryWeapon2Name,
                legendaryWeapon2Type=legendaryWeapon2Type,
                legendaryWeapon2Rating=legendaryWeapon2Rating,
                legendaryWeapon2Icon=legendaryWeapon2Icon,
                legendaryWeapon2Lore=legendaryWeapon2Lore,
                legendaryWeapon2PerkTable=legendaryWeapon2PerkTable,
                legendaryWeapon2FrameName=legendaryWeapon2FrameName,
                legendaryWeapon2FrameIcon=legendaryWeapon2FrameIcon, 
                legendaryWeapon2FrameDesc=legendaryWeapon2FrameDesc,
                legendaryWeapon2LoreExt=legendaryWeapon2LoreExt,
                legendaryWeapon2DamageType=legendaryWeapon2DamageType,
                legendaryWeapon2DamageElement=legendaryWeapon2DamageElement, 
                legendaryWeapon2MasterWorkName=legendaryWeapon2MasterWorkName,
                legendaryWeapon2MasterWorkDesc=legendaryWeapon2MasterWorkDesc,
                legendaryWeapon2MasterWorkIcon=legendaryWeapon2MasterWorkIcon,
                legendaryWeapon3Name=legendaryWeapon3Name,
                legendaryWeapon3Type=legendaryWeapon3Type,
                legendaryWeapon3Rating=legendaryWeapon3Rating,
                legendaryWeapon3Icon=legendaryWeapon3Icon,
                legendaryWeapon3Lore=legendaryWeapon3Lore,
                legendaryWeapon3PerkTable=legendaryWeapon3PerkTable,
                legendaryWeapon3FrameName=legendaryWeapon3FrameName,
                legendaryWeapon3FrameIcon=legendaryWeapon3FrameIcon, 
                legendaryWeapon3FrameDesc=legendaryWeapon3FrameDesc,
                legendaryWeapon3LoreExt=legendaryWeapon3LoreExt,
                legendaryWeapon3DamageType=legendaryWeapon3DamageType,
                legendaryWeapon3DamageElement=legendaryWeapon3DamageElement, 
                legendaryWeapon3MasterWorkName=legendaryWeapon3MasterWorkName,
                legendaryWeapon3MasterWorkDesc=legendaryWeapon3MasterWorkDesc,
                legendaryWeapon3MasterWorkIcon=legendaryWeapon3MasterWorkIcon,
                legendaryWeapon4Name=legendaryWeapon4Name,
                legendaryWeapon4Type=legendaryWeapon4Type,
                legendaryWeapon4Rating=legendaryWeapon4Rating,
                legendaryWeapon4Icon=legendaryWeapon4Icon,
                legendaryWeapon4Lore=legendaryWeapon4Lore,
                legendaryWeapon4PerkTable=legendaryWeapon4PerkTable,
                legendaryWeapon4FrameName=legendaryWeapon4FrameName,
                legendaryWeapon4FrameIcon=legendaryWeapon4FrameIcon, 
                legendaryWeapon4FrameDesc=legendaryWeapon4FrameDesc,
                legendaryWeapon4LoreExt=legendaryWeapon4LoreExt,
                legendaryWeapon4DamageType=legendaryWeapon4DamageType,
                legendaryWeapon4DamageElement=legendaryWeapon4DamageElement, 
                legendaryWeapon4MasterWorkName=legendaryWeapon4MasterWorkName,
                legendaryWeapon4MasterWorkDesc=legendaryWeapon4MasterWorkDesc,
                legendaryWeapon4MasterWorkIcon=legendaryWeapon4MasterWorkIcon,
                legendaryWeapon5Name=legendaryWeapon5Name,
                legendaryWeapon5Type=legendaryWeapon5Type,
                legendaryWeapon5Rating=legendaryWeapon5Rating,
                legendaryWeapon5Icon=legendaryWeapon5Icon,
                legendaryWeapon5Lore=legendaryWeapon5Lore,
                legendaryWeapon5PerkTable=legendaryWeapon5PerkTable,
                legendaryWeapon5FrameName=legendaryWeapon5FrameName,
                legendaryWeapon5FrameIcon=legendaryWeapon5FrameIcon, 
                legendaryWeapon5FrameDesc=legendaryWeapon5FrameDesc,
                legendaryWeapon5LoreExt=legendaryWeapon5LoreExt,
                legendaryWeapon5DamageType=legendaryWeapon5DamageType,
                legendaryWeapon5DamageElement=legendaryWeapon5DamageElement, 
                legendaryWeapon5MasterWorkName=legendaryWeapon5MasterWorkName,
                legendaryWeapon5MasterWorkDesc=legendaryWeapon5MasterWorkDesc,
                legendaryWeapon5MasterWorkIcon=legendaryWeapon5MasterWorkIcon,
                legendaryWeapon6Name=legendaryWeapon6Name,
                legendaryWeapon6Type=legendaryWeapon6Type,
                legendaryWeapon6Rating=legendaryWeapon6Rating,
                legendaryWeapon6Icon=legendaryWeapon6Icon,
                legendaryWeapon6Lore=legendaryWeapon6Lore,
                legendaryWeapon6PerkTable=legendaryWeapon6PerkTable,
                legendaryWeapon6FrameName=legendaryWeapon6FrameName,
                legendaryWeapon6FrameIcon=legendaryWeapon6FrameIcon, 
                legendaryWeapon6FrameDesc=legendaryWeapon6FrameDesc,
                legendaryWeapon6LoreExt=legendaryWeapon6LoreExt,
                legendaryWeapon6DamageType=legendaryWeapon6DamageType,
                legendaryWeapon6DamageElement=legendaryWeapon6DamageElement, 
                legendaryWeapon6MasterWorkName=legendaryWeapon6MasterWorkName,
                legendaryWeapon6MasterWorkDesc=legendaryWeapon6MasterWorkDesc,
                legendaryWeapon6MasterWorkIcon=legendaryWeapon6MasterWorkIcon,
                legendaryWeapon7Name=legendaryWeapon7Name,
                legendaryWeapon7Type=legendaryWeapon7Type,
                legendaryWeapon7Rating=legendaryWeapon7Rating,
                legendaryWeapon7Icon=legendaryWeapon7Icon,
                legendaryWeapon7Lore=legendaryWeapon7Lore,
                legendaryWeapon7PerkTable=legendaryWeapon7PerkTable,
                legendaryWeapon7FrameName=legendaryWeapon7FrameName,
                legendaryWeapon7FrameIcon=legendaryWeapon7FrameIcon, 
                legendaryWeapon7FrameDesc=legendaryWeapon7FrameDesc,
                legendaryWeapon7LoreExt=legendaryWeapon7LoreExt,
                legendaryWeapon7DamageType=legendaryWeapon7DamageType,
                legendaryWeapon7DamageElement=legendaryWeapon7DamageElement, 
                legendaryWeapon7MasterWorkName=legendaryWeapon7MasterWorkName,
                legendaryWeapon7MasterWorkDesc=legendaryWeapon7MasterWorkDesc,
                legendaryWeapon7MasterWorkIcon=legendaryWeapon7MasterWorkIcon,
                legendaryWeapon1DamageTypeIcon=legendaryWeapon1DamageTypeIcon,
                legendaryWeapon2DamageTypeIcon=legendaryWeapon2DamageTypeIcon,
                legendaryWeapon3DamageTypeIcon=legendaryWeapon3DamageTypeIcon,
                legendaryWeapon4DamageTypeIcon=legendaryWeapon4DamageTypeIcon,
                legendaryWeapon5DamageTypeIcon=legendaryWeapon5DamageTypeIcon,
                legendaryWeapon6DamageTypeIcon=legendaryWeapon6DamageTypeIcon,
                legendaryWeapon7DamageTypeIcon=legendaryWeapon7DamageTypeIcon)

    
    htmlTemp = cleanHTML(htmlTemp)
    text_file = open("/home/ubuntu/XurTracker/templates/legendary_weapons.html", "w")
    text_file.write(htmlTemp)
    text_file.close()



setHtmlVals()