#generates html data for main.html from the json
import json

def cleanHTML(html):
    
    html = html.replace("\u2022","<br>&#8226;")
    html = html.replace("\u2014","&nbsp;&#8212&nbsp;")
    html = html.replace("\u2013","&#8211;")
    html = html.replace("\u201c","&#34;")
    html = html.replace("\u201c","&#8220;")
    html = html.replace("\u201d","&#8221;")
    html = html.replace("\u2026","...")
    
    cleanedHTML = html
    return cleanedHTML




def setHtmlVals():
    #read in the json doc
    file = open("/home/ubuntu/XurTracker/data/data.json")
    data = json.load(file)
    file.close()

    #set all vals
    week = data["Week"]
    exoticHunterLoreExt = data["Exotics"]["Hunter Exotic"]["ExtLore"].replace("\n","<br>")
    exoticHunterName = data["Exotics"]["Hunter Exotic"]["name"]
    exoticHunterIcon = data["Exotics"]["Hunter Exotic"]["icon"]
    exoticHunterLore = data["Exotics"]["Hunter Exotic"]["lore"].replace('"','&quot').replace("\u2014","</em><br><br>&#8212&nbsp;")
    exoticHunterStatsList = data["Exotics"]["Hunter Exotic"]["statRolls"]
    exoticHunterLoreExt = str(exoticHunterLoreExt).replace("\n","<br>")
    exoticHunterPerkIcon = data["Exotics"]["Hunter Exotic"]["exoticArmorPerk"][0]["icon"]
    exoticHunterPerkName = data["Exotics"]["Hunter Exotic"]["exoticArmorPerk"][0]["name"]
    exoticHunterPerkDesc = data["Exotics"]["Hunter Exotic"]["exoticArmorPerk"][0]["desc"]


    hunterHelmetName = data["Legendaries"]["Hunter"]["Helmet"]["name"]
    hunterHelmetLore = data["Legendaries"]["Hunter"]["Helmet"]["lore"].replace('"','&quot').replace("\u2014","</em><br><br>&#8212&nbsp;")
    try:
        hunterHelmetLoreExt = data["Legendaries"]["Hunter"]["Helmet"]["ExtLore"].replace("\n","<br>")
    except:
        hunterHelmetLoreExt = data["Legendaries"]["Hunter"]["Helmet"]["ExtLore"]
    hunterHelmetIcon = data["Legendaries"]["Hunter"]["Helmet"]["icon"]
    hunterHelmetStatsList = data["Legendaries"]["Hunter"]["Helmet"]["statRolls"]

    hunterArmsName = data["Legendaries"]["Hunter"]["Arms"]["name"]
    hunterArmsLore = data["Legendaries"]["Hunter"]["Arms"]["lore"].replace('"','&quot').replace("\u2014","</em><br><br>&#8212&nbsp;")
    try:
        hunterArmsLoreExt = data["Legendaries"]["Hunter"]["Arms"]["ExtLore"].replace("\n","<br>")
    except:
        hunterArmsLoreExt = data["Legendaries"]["Hunter"]["Arms"]["ExtLore"]
    hunterArmsIcon = data["Legendaries"]["Hunter"]["Arms"]["icon"]
    hunterArmsStatsList = data["Legendaries"]["Hunter"]["Arms"]["statRolls"]

    hunterChestName = data["Legendaries"]["Hunter"]["Chest"]["name"]
    hunterChestLore = data["Legendaries"]["Hunter"]["Chest"]["lore"].replace('"','&quot').replace("\u2014","</em><br><br>&#8212&nbsp;")
    try:
        hunterChestLoreExt = data["Legendaries"]["Hunter"]["Chest"]["ExtLore"].replace("\n","<br>")
    except:
        hunterChestLoreExt = data["Legendaries"]["Hunter"]["Chest"]["ExtLore"]
    
    hunterChestIcon = data["Legendaries"]["Hunter"]["Chest"]["icon"]
    hunterChestStatsList = data["Legendaries"]["Hunter"]["Chest"]["statRolls"]

    hunterLegsName = data["Legendaries"]["Hunter"]["Legs"]["name"]
    hunterLegsLore = data["Legendaries"]["Hunter"]["Legs"]["lore"].replace('"','&quot').replace("\u2014","</em><br><br>&#8212&nbsp;")
    try:
        hunterLegsLoreExt = data["Legendaries"]["Hunter"]["Legs"]["ExtLore"].replace("\n","<br>")
    except:
        hunterLegsLoreExt = data["Legendaries"]["Hunter"]["Legs"]["ExtLore"]

    hunterLegsIcon = data["Legendaries"]["Hunter"]["Legs"]["icon"]
    hunterLegsStatsList = data["Legendaries"]["Hunter"]["Legs"]["statRolls"]

    hunterMarkName = data["Legendaries"]["Hunter"]["Class Item"]["name"]
    hunterMarkLore = data["Legendaries"]["Hunter"]["Class Item"]["lore"].replace('"','&quot').replace("\u2014","</em><br><br>&#8212&nbsp;")
    try:
        hunterMarkLoreExt = data["Legendaries"]["Hunter"]["Class Item"]["ExtLore"].replace("\n","<br>")
    except:
         hunterMarkLoreExt = data["Legendaries"]["Hunter"]["Class Item"]["ExtLore"]
    
    hunterMarkIcon = data["Legendaries"]["Hunter"]["Class Item"]["icon"]
    hunterMarkStatsList = [0,0,0,0,0,0,0]

    loreList = [exoticHunterLoreExt,hunterHelmetLoreExt,hunterArmsLoreExt,hunterChestLoreExt,hunterLegsLoreExt,hunterMarkLoreExt]

    for i in range(len(loreList)):
      if(str(loreList[i]) == "None"):
        
        if(i == 0):
            exoticHunterLoreExt = "This weapon has no known lore. Perhaps it was lost long ago?"
        if(i == 1):
            hunterHelmetLoreExt = "This weapon has no known lore. Perhaps it was lost long ago?"
        if(i == 2):
            hunterArmsLoreExt = "This weapon has no known lore. Perhaps it was lost long ago?"
        if(i == 3):
            hunterChestLoreExt = "This weapon has no known lore. Perhaps it was lost long ago?"
        if(i == 4):
            hunterLegsLoreExt = "This weapon has no known lore. Perhaps it was lost long ago?"
        if(i == 5):
            hunterMarkLoreExt = "This weapon has no known lore. Perhaps it was lost long ago?"
    
    htmlTemp ="""
    <!DOCTYPE html>
<html lang="en">
<head>
    <title>X&#251r Tracker // Hunter</title>
    <link rel="shortcut icon" href="https://pbs.twimg.com/profile_images/1586064167131385857/1mQC0kgE_400x400.png">
    <link rel="apple-touch-icon" sizes="192x192" href="https://pbs.twimg.com/profile_images/1586064167131385857/1mQC0kgE_400x400.png">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.3/font/bootstrap-icons.css">
    <link rel="canonical" href="https://www.xurtracker.com/">
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
                    <a class="nav-link active" href="legendary-weapons">Legendary Weapons</a>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle active" href="#" id="navbarDropdownMenuLink" role="button"
                            data-bs-toggle="dropdown" aria-expanded="false">
                            Armor
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                            <li><a class="dropdown-item" href="titan">Titan Armor</a></li>
                            <li><a class="dropdown-item" aria-current="page" href="hunter">Hunter Armor</a></li>
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

        progress {{
            border: solid #636363 3px;
            background: #ffffff;
        }}

        progress {{
            color: #ffffff;
        }}

        progress::-moz-progress-bar {{
            background: #000000;
        }}

        progress::-webkit-progress-value {{
            background: #ffffff;
        }}

        progress::-webkit-progress-bar {{
            background: #000000;
        }}

        ::-webkit-scrollbar {{
            width: 0;
            background: transparent;
        }}
    </style>
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-Y64WQ82WSS"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag() {{ dataLayer.push(arguments); }}
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
                    X&#251r's Hunter Armor for {week}
                    <hr>
                </h1>
                <br>
                <br>
            </div>
        </div>
    </div>
    <br>
    <br>
    <div class="container">
        <div class="row">
            <div class="col-md-6 border">
                <br>
                <table class="table" style="color: #ffffff;padding-left: 4.5%;">
                    <thead>
                        <tr>
                            <th><img src="https://bungie.net/common/destiny2_content/icons/2ffa90c58bdadcca8226f553315212e7.png"
                                    class="img" width="70px" alt="exotic-warlock"></th>
                            <th>
                                <h2 style="padding-bottom: 10px;">Exotic Armorpeice</h2>
                            </th>
                        </tr>
                    </thead>
                </table>
                <br>
                <table class="table table-borderless" style="color: #ffffff;padding-left: 4.5%;">
                    <h3 style="text-align: center; border-bottom: #ffffff; border: #ffffff;">{exoticHunterName}
                        <hr>
                    </h3>
                    <thead>
                        <tr>
                            <th><img src="{exoticHunterIcon}" class="img" alt="exotic-warlock"></th>
                            <th>
                                <em>{exoticHunterLore}</em>
                            </th>
                        </tr>
                    </thead>
                </table>

                <table class="table table-borderless" style="color: #ffffff;padding-left: 4.5%;">
                    <thead>
                        <tr>
                            <h4 style="padding-left: 1%;"><u>Exotic Perk</u></h4>
                            <th>
                                <img src="{exoticHunterPerkIcon}" style="padding-bottom: 12.5px;" class="img"
                                    alt="exotic-warlock-perk" width="75"></img>
                            </th>
                            </th>
                            <th>
                                <h5>{exoticHunterPerkName}</h5>
                                <p>{exoticHunterPerkDesc}</p>
                            </th>
                        </tr>
                    </thead>
                </table>
                <div style="padding-left: 2%;">
                    <table class="table table-borderless" style="color: #ffffff;max-width: 200px;">
                        <caption>
                            <h4 style="color: #ffffff;">Stat Total : {exoticHunterStatsList[0]}</h5>
                        </caption>
                        <thead>
                            <tr>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <th scope="row" style="vertical-align: middle;border: so #ffffff;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/e26e0e93a9daf4fdd21bf64eb9246340.png"
                                        class="img" alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="Mobility <br>Increases movement speed and maximum jump height."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{exoticHunterStatsList[1]}</h5>
                                </td>
                                <td style="vertical-align: middle;">

                                    <progress id="mob" value="{exoticHunterStatsList[1]}" max="40"
                                        style="height: 30px; width: 200px;"> 32% </progress>

                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/202ecc1c6febeb6b97dafc856e863140.png"
                                        class="img" alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="Resilience <br>&#8226Decreases cooldown of Class abilities.<br>&#8226;Increases Shield capacity.<br>&#8226;Reduces incoming damage."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{exoticHunterStatsList[2]}</h5>
                                </td>
                                <td style="vertical-align: middle;">

                                    <progress id="res" value="{exoticHunterStatsList[2]}" max="40"
                                        style="height: 30px; width: 200px;"> 32% </progress>

                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/128eee4ee7fc127851ab32eac6ca91cf.png"
                                        class="img" alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="Recovery<br>Increases health regeneration rate."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{exoticHunterStatsList[3]}</h5>
                                </td>
                                <td style="vertical-align: middle;">

                                    <progress id="rec" value="{exoticHunterStatsList[3]}" max="40"
                                        style="height: 30px; width: 200px;"> 32% </progress>

                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/79be2d4adef6a19203f7385e5c63b45b.png"
                                        class="img" alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="Discipline<br>Decreases cooldown of grenade abilities."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{exoticHunterStatsList[4]}</h5>
                                </td>
                                <td style="vertical-align: middle;">

                                    <progress id="dis" value="{exoticHunterStatsList[4]}" max="40"
                                        style="height: 30px; width: 200px;"> 32% </progress>

                                </td>
                            </tr>

                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/d1c154469670e9a592c9d4cbdcae5764.png"
                                        class="img" alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="Intellect<br>Decreases cooldown of Super abilities."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{exoticHunterStatsList[5]}</h5>
                                </td>
                                <td style="vertical-align: middle;">

                                    <progress id="inte" value="{exoticHunterStatsList[5]}" max="40"
                                        style="height: 30px; width: 200px;"> 32% </progress>

                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/ea5af04ccd6a3470a44fd7bb0f66e2f7.png"
                                        class="img" alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="Strength<br>Decreases cooldown of melee abilities."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{exoticHunterStatsList[6]}</h5>
                                </td>
                                <td style="vertical-align: middle;">

                                    <progress id="stre" value="{exoticHunterStatsList[6]}" max="40"
                                        style="height: 30px; width: 200px;"> 32% </progress>

                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <br>
                <div class="accordion" id="hunter1">
                    <div class="accordion-item" style="background-color: #0e1010; border-color: #ffffff;">
                        <h2 class="accordion-header" id="heading1"
                            style="background-color: #0e1010; border-color: #ffffff;">
                            <button class="accordion-button" type="button" data-bs-toggle="collapse"
                                style="background-color: #0e1010; color: #ffffff;" data-bs-target="#collapse1"
                                aria-expanded="true" aria-controls="collapse1">
                                {exoticHunterName} Lore
                            </button>
                        </h2>
                        <div id="collapse1" class="accordion-collapse collapse" aria-labelledby="heading1"
                            data-bs-parent="#accordionExample">
                            <div class="accordion-body">
                                <p>
                                <h3>{exoticHunterName}</h3>
                                <hr>
                                <p>{exoticHunterLoreExt}</p>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                <br>

            </div>

            <div class="col-md-6 border">
                <br>
                <table class="table" style="color: #ffffff;padding-left: 4.5%;">
                    <thead>
                        <tr>
                            <th>
                                <div
                                    style="background-image:url('https://www.bungie.net/common/destiny2_content/icons/d89699e6307ac5d2a306cf054978e251.png'); width:70px; height:70px; background-position:center; border-radius: 100%;">
                                    &nbsp;</div>
                            </th>
                            <th>
                                <h2 style="padding-bottom: 10px;">Helmet</h2>
                            </th>
                        </tr>
                    </thead>
                </table>
                <br>
                <table class="table table-borderless" style="color: #ffffff;padding-left: 4.5%;">
                    <h3 style="text-align: center; border-bottom: #ffffff; border: #ffffff;">{hunterHelmetName}
                        <hr>
                    </h3>
                    <thead>
                        <tr>
                            <th><img src={hunterHelmetIcon} class="img" alt="exotic-warlock"></th>
                            <th>
                                <em>{hunterHelmetLore}</em>
                            </th>
                        </tr>
                    </thead>
                </table>
                <table class="table table-borderless" style="color: #ffffff;padding-left: 4.5%;visibility:hidden;">
                    <thead>
                        <tr>
                            <h4 style="padding-left: 1%;visibility:hidden;"><u>Exotic Perk</u></h4>
                            <th>
                                <img src="{exoticHunterPerkIcon}" style="padding-bottom: 12.5px;" class="img"
                                    alt="exotic-warlock-perk" width="75"></img>
                            </th>
                            </th>
                            <th>
                                <h5>{exoticHunterPerkName}</h5>
                                <p>{exoticHunterPerkDesc}</p>
                            </th>
                        </tr>
                    </thead>
                </table>
                <div style="padding-left: 2%;">
                    <table class="table table-borderless" style="color: #ffffff;max-width: 200px;">
                        <caption>
                            <h4 style="color: #ffffff;">Stat Total : {hunterHelmetStatsList[0]}</h5>
                        </caption>
                        <thead>
                            <tr>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <th scope="row" style="vertical-align: middle;border: so #ffffff;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/e26e0e93a9daf4fdd21bf64eb9246340.png"
                                        class="img" alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="Mobility <br>Increases movement speed and maximum jump height."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{hunterHelmetStatsList[1]}</h5>
                                </td>
                                <td style="vertical-align: middle;">

                                    <progress id="mob" value="{hunterHelmetStatsList[1]}" max="40"
                                        style="height: 30px; width: 200px;"> 32% </progress>

                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/202ecc1c6febeb6b97dafc856e863140.png"
                                        class="img" alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="Resilience <br>&#8226Decreases cooldown of Class abilities.<br>&#8226;Increases Shield capacity.<br>&#8226;Reduces incoming damage."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{hunterHelmetStatsList[2]}</h5>
                                </td>
                                <td style="vertical-align: middle;">

                                    <progress id="res" value="{hunterHelmetStatsList[2]}" max="40"
                                        style="height: 30px; width: 200px;"> 32% </progress>

                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/128eee4ee7fc127851ab32eac6ca91cf.png"
                                        class="img" alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="Recovery<br>Increases health regeneration rate."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{hunterHelmetStatsList[3]}</h5>
                                </td>
                                <td style="vertical-align: middle;">

                                    <progress id="rec" value="{hunterHelmetStatsList[3]}" max="40"
                                        style="height: 30px; width: 200px;"> 32% </progress>

                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/79be2d4adef6a19203f7385e5c63b45b.png"
                                        class="img" alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="Discipline<br>Decreases cooldown of grenade abilities."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{hunterHelmetStatsList[4]}</h5>
                                </td>
                                <td style="vertical-align: middle;">

                                    <progress id="dis" value="{hunterHelmetStatsList[4]}" max="40"
                                        style="height: 30px; width: 200px;"> 32% </progress>

                                </td>
                            </tr>

                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/d1c154469670e9a592c9d4cbdcae5764.png"
                                        class="img" alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="Intellect<br>Decreases cooldown of Super abilities."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{hunterHelmetStatsList[5]}</h5>
                                </td>
                                <td style="vertical-align: middle;">

                                    <progress id="inte" value="{hunterHelmetStatsList[5]}" max="40"
                                        style="height: 30px; width: 200px;"> 32% </progress>

                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/ea5af04ccd6a3470a44fd7bb0f66e2f7.png"
                                        class="img" alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="Strength<br>Decreases cooldown of melee abilities."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{hunterHelmetStatsList[6]}</h5>
                                </td>
                                <td style="vertical-align: middle;">

                                    <progress id="stre" value="{hunterHelmetStatsList[6]}" max="40"
                                        style="height: 30px; width: 200px;"> 32% </progress>

                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <br>
                <div class="accordion" id="hunter2">
                    <div class="accordion-item" style="background-color: #0e1010; border-color: #ffffff;">
                        <h2 class="accordion-header" id="heading2"
                            style="background-color: #0e1010; border-color: #ffffff;">
                            <button class="accordion-button" type="button" data-bs-toggle="collapse"
                                style="background-color: #0e1010; color: #ffffff;" data-bs-target="#collapse2"
                                aria-expanded="true" aria-controls="collapse2">
                                {hunterHelmetName} Lore
                            </button>
                        </h2>
                        <div id="collapse2" class="accordion-collapse collapse" aria-labelledby="heading2"
                            data-bs-parent="#accordionExample">
                            <div class="accordion-body">
                                <p>
                                <h3>{hunterHelmetName}</h3>
                                <hr>
                                <p>{hunterHelmetLoreExt}</p>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                <br>
            </div>
        </div>
    </div>
    <div class="container">
        <div class="row ">
            <div class="col-md-6 border">
                <br>
                <table class="table" style="color: #ffffff;padding-left: 4.5%;">
                    <thead>
                        <tr>
                            <th>
                                <div
                                    style="background-image:url('https://www.bungie.net/common/destiny2_content/icons/18bb744532b78a20164f150c770c5f89.png'); width:70px; height:70px; background-position:center; border-radius: 100%;">
                                    &nbsp;</div>
                            </th>
                            <th>
                                <h2 style="padding-bottom: 10px;">Arms</h2>
                            </th>
                        </tr>
                    </thead>
                </table>
                <br>
                <table class="table table-borderless" style="color: #ffffff;padding-left: 4.5%;height: 100px;">
                    <h3 style="text-align: center; border-bottom: #ffffff; border: #ffffff;">{hunterArmsName}
                        <hr>
                    </h3>
                    <thead>
                        <tr>
                            <th><img src={hunterArmsIcon} class="img" alt="exotic-warlock"></th>
                            <th style="height: 100px;">
                                <em>{hunterArmsLore}</em>
                            </th>
                        </tr>
                    </thead>
                </table>
                <div style="padding-left: 2%">
                    <table class="table table-borderless" style="color: #ffffff;max-width: 200px;">
                        <caption>
                            <h4 style="color: #ffffff;">Stat Total : {hunterArmsStatsList[0]}</h5>
                        </caption>
                        <thead>
                            <tr>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <th scope="row" style="vertical-align: middle;border: so #ffffff;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/e26e0e93a9daf4fdd21bf64eb9246340.png"
                                        class="img" alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="Mobility <br>Increases movement speed and maximum jump height."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{hunterArmsStatsList[1]}</h5>
                                </td>
                                <td style="vertical-align: middle;">

                                    <progress id="mob" value="{hunterArmsStatsList[1]}" max="40"
                                        style="height: 30px; width: 200px;"> 32% </progress>

                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/202ecc1c6febeb6b97dafc856e863140.png"
                                        class="img" alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="Resilience <br>&#8226Decreases cooldown of Class abilities.<br>&#8226;Increases Shield capacity.<br>&#8226;Reduces incoming damage."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{hunterArmsStatsList[2]}</h5>
                                </td>
                                <td style="vertical-align: middle;">

                                    <progress id="res" value="{hunterArmsStatsList[2]}" max="40"
                                        style="height: 30px; width: 200px;"> 32% </progress>

                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/128eee4ee7fc127851ab32eac6ca91cf.png"
                                        class="img" alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="Recovery<br>Increases health regeneration rate."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{hunterArmsStatsList[3]}</h5>
                                </td>
                                <td style="vertical-align: middle;">

                                    <progress id="rec" value="{hunterArmsStatsList[3]}" max="40"
                                        style="height: 30px; width: 200px;"> 32% </progress>

                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/79be2d4adef6a19203f7385e5c63b45b.png"
                                        class="img" alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="Discipline<br>Decreases cooldown of grenade abilities."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{hunterArmsStatsList[4]}</h5>
                                </td>
                                <td style="vertical-align: middle;">

                                    <progress id="dis" value="{hunterArmsStatsList[4]}" max="40"
                                        style="height: 30px; width: 200px;"> 32% </progress>

                                </td>
                            </tr>

                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/d1c154469670e9a592c9d4cbdcae5764.png"
                                        class="img" alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="Intellect<br>Decreases cooldown of Super abilities."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{hunterArmsStatsList[5]}</h5>
                                </td>
                                <td style="vertical-align: middle;">

                                    <progress id="inte" value="{hunterArmsStatsList[5]}" max="40"
                                        style="height: 30px; width: 200px;"> 32% </progress>

                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/ea5af04ccd6a3470a44fd7bb0f66e2f7.png"
                                        class="img" alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="Strength<br>Decreases cooldown of melee abilities."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{hunterArmsStatsList[6]}</h5>
                                </td>
                                <td style="vertical-align: middle;">

                                    <progress id="stre" value="{hunterArmsStatsList[6]}" max="40"
                                        style="height: 30px; width: 200px;"> 32% </progress>

                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <br>
                <div class="accordion" id="hunter3">
                    <div class="accordion-item" style="background-color: #0e1010; border-color: #ffffff;">
                        <h2 class="accordion-header" id="heading3"
                            style="background-color: #0e1010; border-color: #ffffff;">
                            <button class="accordion-button" type="button" data-bs-toggle="collapse"
                                style="background-color: #0e1010; color: #ffffff;" data-bs-target="#collapse3"
                                aria-expanded="true" aria-controls="collapse3">
                                {hunterArmsName} Lore
                            </button>
                        </h2>
                        <div id="collapse3" class="accordion-collapse collapse" aria-labelledby="heading3"
                            data-bs-parent="#accordionExample">
                            <div class="accordion-body">
                                <p>
                                <h3>{hunterArmsName}</h3>
                                <hr>
                                <p>{hunterArmsLoreExt}</p>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                <br>

            </div>

            <div class="col-md-6 border">
                <br>
                <table class="table" style="color: #ffffff;padding-left: 4.5%;">
                    <thead>
                        <tr>
                            <th>
                                <div
                                    style="background-image:url('https://www.bungie.net/common/destiny2_content/icons/6bf61607ffa8198cdabdf0fa3b5feab1.png'); width:70px; height:70px; background-position:center; border-radius: 100%;">
                                    &nbsp;</div>
                            </th>
                            <th>
                                <h2 style="padding-bottom: 10px;">Chest</h2>
                            </th>
                        </tr>
                    </thead>
                </table>
                <br>
                <table class="table table-borderless" style="color: #ffffff;padding-left: 4.5%;height: 100px;">
                    <h3 style="text-align: center; border-bottom: #ffffff; border: #ffffff;">{hunterChestName}
                        <hr>
                    </h3>
                    <thead>
                        <tr>
                            <th><img src="{hunterChestIcon}" class="img" alt="exotic-warlock"></th>
                            <th style="height: 100px;">
                                <em>{hunterChestLore}</em>
                            </th>
                        </tr>
                    </thead>
                </table>
                <div style="padding-left: 2%">
                    <table class="table table-borderless" style="color: #ffffff;max-width: 200px;">
                        <caption>
                            <h4 style="color: #ffffff;">Stat Total : {hunterChestStatsList[0]}</h5>
                        </caption>
                        <thead>
                            <tr>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <th scope="row" style="vertical-align: middle;border: so #ffffff;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/e26e0e93a9daf4fdd21bf64eb9246340.png"
                                        class="img" alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="Mobility <br>Increases movement speed and maximum jump height."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{hunterChestStatsList[1]}</h5>
                                </td>
                                <td style="vertical-align: middle;">

                                    <progress id="mob" value="{hunterChestStatsList[1]}" max="40"
                                        style="height: 30px; width: 200px;"> 32% </progress>

                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/202ecc1c6febeb6b97dafc856e863140.png"
                                        class="img" alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="Resilience <br>&#8226Decreases cooldown of Class abilities.<br>&#8226;Increases Shield capacity.<br>&#8226;Reduces incoming damage."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{hunterChestStatsList[2]}</h5>
                                </td>
                                <td style="vertical-align: middle;">

                                    <progress id="res" value="{hunterChestStatsList[2]}" max="40"
                                        style="height: 30px; width: 200px;"> 32% </progress>

                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/128eee4ee7fc127851ab32eac6ca91cf.png"
                                        class="img" alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="Recovery<br>Increases health regeneration rate."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{hunterChestStatsList[3]}</h5>
                                </td>
                                <td style="vertical-align: middle;">

                                    <progress id="rec" value="{hunterChestStatsList[3]}" max="40"
                                        style="height: 30px; width: 200px;"> 32% </progress>

                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/79be2d4adef6a19203f7385e5c63b45b.png"
                                        class="img" alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="Discipline<br>Decreases cooldown of grenade abilities."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{hunterChestStatsList[4]}</h5>
                                </td>
                                <td style="vertical-align: middle;">

                                    <progress id="dis" value="{hunterChestStatsList[4]}" max="40"
                                        style="height: 30px; width: 200px;"> 32% </progress>

                                </td>
                            </tr>

                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/d1c154469670e9a592c9d4cbdcae5764.png"
                                        class="img" alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="Intellect<br>Decreases cooldown of Super abilities."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{hunterChestStatsList[5]}</h5>
                                </td>
                                <td style="vertical-align: middle;">

                                    <progress id="inte" value="{hunterChestStatsList[5]}" max="40"
                                        style="height: 30px; width: 200px;"> 32% </progress>

                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/ea5af04ccd6a3470a44fd7bb0f66e2f7.png"
                                        class="img" alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="Strength<br>Decreases cooldown of melee abilities."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{hunterChestStatsList[6]}</h5>
                                </td>
                                <td style="vertical-align: middle;">

                                    <progress id="stre" value="{hunterChestStatsList[6]}" max="40"
                                        style="height: 30px; width: 200px;"> 32% </progress>

                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <br>
                <div class="accordion" id="hunter4">
                    <div class="accordion-item" style="background-color: #0e1010; border-color: #ffffff;">
                        <h2 class="accordion-header" id="heading4"
                            style="background-color: #0e1010; border-color: #ffffff;">
                            <button class="accordion-button" type="button" data-bs-toggle="collapse"
                                style="background-color: #0e1010; color: #ffffff;" data-bs-target="#collapse4"
                                aria-expanded="true" aria-controls="collapse4">
                                {hunterChestName} Lore
                            </button>
                        </h2>
                        <div id="collapse4" class="accordion-collapse collapse" aria-labelledby="heading4"
                            data-bs-parent="#accordionExample">
                            <div class="accordion-body">
                                <p>
                                <h3>{hunterChestName}</h3>
                                <hr>
                                <p>{hunterChestLoreExt}</p>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                <br>
            </div>
        </div>
    </div>
    <div class="container">
        <div class="row ">
            <div class="col-md-6 border">
                <br>
                <table class="table" style="color: #ffffff;padding-left: 4.5%;">
                    <thead>
                        <tr>
                            <th>
                                <div
                                    style="background-image:url('https://www.bungie.net/common/destiny2_content/icons/c4b573f9dd4892f6eb3bfb9b194170d0.png'); width:70px; height:70px; background-position:center; border-radius: 100%;">
                                    &nbsp;</div>
                            </th>
                            <th>
                                <h2 style="padding-bottom: 10px;">Legs</h2>
                            </th>
                        </tr>
                    </thead>
                </table>
                <br>
                <table class="table table-borderless" style="color: #ffffff;padding-left: 4.5%;height: 100px;">
                    <h3 style="text-align: center; border-bottom: #ffffff; border: #ffffff;">{hunterLegsName}
                        <hr>
                    </h3>
                    <thead>
                        <tr>
                            <th><img src="{hunterLegsIcon}" class="img" alt="exotic-warlock"></th>
                            <th style="height: 100px;">
                                <em>{hunterLegsLore}</em>
                            </th>
                        </tr>
                    </thead>
                </table>
                <div style="padding-left: 2%">
                    <table class="table table-borderless" style="color: #ffffff;max-width: 200px;">
                        <caption>
                            <h4 style="color: #ffffff;">Stat Total : {hunterLegsStatsList[0]}</h5>
                        </caption>
                        <thead>
                            <tr>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <th scope="row" style="vertical-align: middle;border: so #ffffff;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/e26e0e93a9daf4fdd21bf64eb9246340.png"
                                        class="img" alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="Mobility <br>Increases movement speed and maximum jump height."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{hunterLegsStatsList[1]}</h5>
                                </td>
                                <td style="vertical-align: middle;">

                                    <progress id="mob" value="{hunterLegsStatsList[1]}" max="40"
                                        style="height: 30px; width: 200px;"> 32% </progress>

                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/202ecc1c6febeb6b97dafc856e863140.png"
                                        class="img" alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="Resilience <br>&#8226Decreases cooldown of Class abilities.<br>&#8226;Increases Shield capacity.<br>&#8226;Reduces incoming damage."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{hunterLegsStatsList[2]}</h5>
                                </td>
                                <td style="vertical-align: middle;">

                                    <progress id="res" value="{hunterLegsStatsList[2]}" max="40"
                                        style="height: 30px; width: 200px;"> 32% </progress>

                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/128eee4ee7fc127851ab32eac6ca91cf.png"
                                        class="img" alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="Recovery<br>Increases health regeneration rate."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{hunterLegsStatsList[3]}</h5>
                                </td>
                                <td style="vertical-align: middle;">

                                    <progress id="rec" value="{hunterLegsStatsList[3]}" max="40"
                                        style="height: 30px; width: 200px;"> 32% </progress>

                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/79be2d4adef6a19203f7385e5c63b45b.png"
                                        class="img" alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="Discipline<br>Decreases cooldown of grenade abilities."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{hunterLegsStatsList[4]}</h5>
                                </td>
                                <td style="vertical-align: middle;">

                                    <progress id="dis" value="{hunterLegsStatsList[4]}" max="40"
                                        style="height: 30px; width: 200px;"> 32% </progress>

                                </td>
                            </tr>

                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/d1c154469670e9a592c9d4cbdcae5764.png"
                                        class="img" alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="Intellect<br>Decreases cooldown of Super abilities."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{hunterLegsStatsList[5]}</h5>
                                </td>
                                <td style="vertical-align: middle;">

                                    <progress id="inte" value="{hunterLegsStatsList[5]}" max="40"
                                        style="height: 30px; width: 200px;"> 32% </progress>

                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/ea5af04ccd6a3470a44fd7bb0f66e2f7.png"
                                        class="img" alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="Strength<br>Decreases cooldown of melee abilities."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{hunterLegsStatsList[6]}</h5>
                                </td>
                                <td style="vertical-align: middle;">

                                    <progress id="stre" value="{hunterLegsStatsList[6]}" max="40"
                                        style="height: 30px; width: 200px;"> 32% </progress>

                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <br>
                <div class="accordion" id="hunter5">
                    <div class="accordion-item" style="background-color: #0e1010; border-color: #ffffff;">
                        <h2 class="accordion-header" id="heading5"
                            style="background-color: #0e1010; border-color: #ffffff;">
                            <button class="accordion-button" type="button" data-bs-toggle="collapse"
                                style="background-color: #0e1010; color: #ffffff;" data-bs-target="#collapse5"
                                aria-expanded="true" aria-controls="collapse5">
                                {hunterLegsName} Lore
                            </button>
                        </h2>
                        <div id="collapse5" class="accordion-collapse collapse" aria-labelledby="heading5"
                            data-bs-parent="#accordionExample">
                            <div class="accordion-body">
                                <p>
                                <h3>{hunterLegsName}</h3>
                                <hr>
                                <p>{hunterLegsLoreExt}</p>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                <br>

            </div>

            <div class="col-md-6 border">
                <br>
                <table class="table" style="color: #ffffff;padding-left: 4.5%;">
                    <thead>
                        <tr>
                            <th>
                                <div
                                    style="background-image:url('https://www.bungie.net/common/destiny2_content/icons/3cfff0f2aa68784762f553eb7997e909.png'); width:70px; height:70px; background-position:center; border-radius: 100%;">
                                    &nbsp;</div>
                            </th>
                            <th>
                                <h2 style="padding-bottom: 10px;">Hunter Cloak</h2>
                            </th>
                        </tr>
                    </thead>
                </table>
                <br>
                <table class="table table-borderless" style="color: #ffffff;padding-left: 4.5%;height: 100px;">
                    <h3 style="text-align: center; border-bottom: #ffffff; border: #ffffff;">{hunterMarkName}
                        <hr>
                    </h3>
                    <thead>
                        <tr>
                            <th><img src="{hunterMarkIcon}" class="img" alt="exotic-warlock"></th>
                            <th style="height: 100px;">
                                <em>{hunterMarkLore}</em>
                            </th>
                        </tr>
                    </thead>
                </table>
                <div style="padding-left: 2%">
                    <table class="table table-borderless" style="color: #ffffff;max-width: 200px;">
                        <caption style="height: 53px;">Hunter Cloaks do not have randomized stats.<br></caption>
                        <thead>
                            <tr>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <th scope="row" style="vertical-align: middle;border: so #ffffff;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/e26e0e93a9daf4fdd21bf64eb9246340.png"
                                        class="img" alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="Mobility <br>Increases movement speed and maximum jump height."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{hunterMarkStatsList[1]}</h5>
                                </td>
                                <td style="vertical-align: middle;">

                                    <progress id="mob" value="{hunterMarkStatsList[1]}" max="40"
                                        style="height: 30px; width: 200px;"> 32% </progress>

                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/202ecc1c6febeb6b97dafc856e863140.png"
                                        class="img" alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="Resilience <br>&#8226Decreases cooldown of Class abilities.<br>&#8226;Increases Shield capacity.<br>&#8226;Reduces incoming damage."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{hunterMarkStatsList[2]}</h5>
                                </td>
                                <td style="vertical-align: middle;">

                                    <progress id="res" value="{hunterMarkStatsList[2]}" max="40"
                                        style="height: 30px; width: 200px;"> 32% </progress>

                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/128eee4ee7fc127851ab32eac6ca91cf.png"
                                        class="img" alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="Recovery<br>Increases health regeneration rate."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{hunterMarkStatsList[3]}</h5>
                                </td>
                                <td style="vertical-align: middle;">

                                    <progress id="rec" value="{hunterMarkStatsList[3]}" max="40"
                                        style="height: 30px; width: 200px;"> 32% </progress>

                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/79be2d4adef6a19203f7385e5c63b45b.png"
                                        class="img" alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="Discipline<br>Decreases cooldown of grenade abilities."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{hunterMarkStatsList[4]}</h5>
                                </td>
                                <td style="vertical-align: middle;">

                                    <progress id="dis" value="{hunterMarkStatsList[4]}" max="40"
                                        style="height: 30px; width: 200px;"> 32% </progress>

                                </td>
                            </tr>

                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/d1c154469670e9a592c9d4cbdcae5764.png"
                                        class="img" alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="Intellect<br>Decreases cooldown of Super abilities."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{hunterMarkStatsList[5]}</h5>
                                </td>
                                <td style="vertical-align: middle;">

                                    <progress id="inte" value="{hunterMarkStatsList[5]}" max="40"
                                        style="height: 30px; width: 200px;"> 32% </progress>

                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/ea5af04ccd6a3470a44fd7bb0f66e2f7.png"
                                        class="img" alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip"
                                        data-bs-html="true" data-bs-placement="left"
                                        title="Strength<br>Decreases cooldown of melee abilities."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{hunterMarkStatsList[6]}</h5>
                                </td>
                                <td style="vertical-align: middle;">

                                    <progress id="stre" value="{hunterMarkStatsList[6]}" max="40"
                                        style="height: 30px; width: 200px;"> 32% </progress>

                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <br>
                <div class="accordion" id="hunter6">
                    <div class="accordion-item" style="background-color: #0e1010; border-color: #ffffff;">
                        <h2 class="accordion-header" id="heading6"
                            style="background-color: #0e1010; border-color: #ffffff;">
                            <button class="accordion-button" type="button" data-bs-toggle="collapse"
                                style="background-color: #0e1010; color: #ffffff;" data-bs-target="#collapse6"
                                aria-expanded="true" aria-controls="collapse6">
                                {hunterMarkName} Lore
                            </button>
                        </h2>
                        <div id="collapse6" class="accordion-collapse collapse" aria-labelledby="heading6"
                            data-bs-parent="#accordionExample">
                            <div class="accordion-body">
                                <p>
                                <h3>{hunterMarkName}</h3>
                                <hr>
                                <p>{hunterMarkLoreExt}</p>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                <br>
            </div>
        </div>
    </div>
    <br>
    <br>
    <footer class="bg-dark text-center text-white">
        <div class="text-center p-3" style="background-color:#6e757d;">
            Created By:
            <a class="text-white" href="https://www.linkedin.com/in/thomas-smith-89a918192/">Thomas Smith</a> // Bungie
            Net: <a class="text-white"
                href="https://www.bungie.net/7/en/User/Profile/254/10061778?bgn=Lulamae1">Lulamae1#6072</a>
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
    """.format(week=week,exoticHunterLoreExt=exoticHunterLoreExt,exoticHunterName=exoticHunterName,exoticHunterIcon=exoticHunterIcon,exoticHunterLore=exoticHunterLore,exoticHunterStatsList=exoticHunterStatsList,
    hunterHelmetLoreExt=hunterHelmetLoreExt,hunterHelmetName=hunterHelmetName,hunterHelmetIcon=hunterHelmetIcon,hunterHelmetLore=hunterHelmetLore,hunterHelmetStatsList=hunterHelmetStatsList,
    hunterArmsLoreExt=hunterArmsLoreExt,hunterArmsName=hunterArmsName,hunterArmsIcon=hunterArmsIcon,hunterArmsLore=hunterArmsLore,hunterArmsStatsList=hunterArmsStatsList,
    hunterChestLoreExt=hunterChestLoreExt,hunterChestName=hunterChestName,hunterChestIcon=hunterChestIcon,hunterChestLore=hunterChestLore,hunterChestStatsList=hunterChestStatsList,
    hunterLegsLoreExt=hunterLegsLoreExt,hunterLegsName=hunterLegsName,hunterLegsIcon=hunterLegsIcon,hunterLegsLore=hunterLegsLore,hunterLegsStatsList=hunterLegsStatsList,
    hunterMarkLoreExt=hunterMarkLoreExt,hunterMarkName=hunterMarkName,hunterMarkIcon=hunterMarkIcon,hunterMarkLore=hunterMarkLore,hunterMarkStatsList=hunterMarkStatsList,exoticHunterPerkIcon=exoticHunterPerkIcon,exoticHunterPerkName=exoticHunterPerkName,exoticHunterPerkDesc=exoticHunterPerkDesc)

    
    htmlTemp = cleanHTML(htmlTemp)
    text_file = open("/home/ubuntu/XurTracker/templates/hunter_armor.html", "w")
    text_file.write(htmlTemp)
    text_file.close()



setHtmlVals()