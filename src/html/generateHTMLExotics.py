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
                          <th scope="row"><img src="https://www.bungie.net/common/destiny2_content/icons/e26e0e93a9daf4fdd21bf64eb9246340.png" width="40" height="40"> Armor Mobility Rating</th>
                            <td><b>{mob}</b></td>
                          </tr>
                          <tr>
                            <th scope="row"><img src="https://www.bungie.net/common/destiny2_content/icons/202ecc1c6febeb6b97dafc856e863140.png" width="40" height="40"> Armor Resilience Rating</th>
                            <td><b>{res}</b></td>
                          </tr>
                          <tr>
                            <th scope="row"><img src="https://www.bungie.net/common/destiny2_content/icons/128eee4ee7fc127851ab32eac6ca91cf.png" width="40" height="40"> Armor Recovery Rating</th>
                            <td><b>{rec}</b></td>
                          </tr>
                          <tr>
                            <th scope="row"><img src="https://www.bungie.net/common/destiny2_content/icons/ca62128071dc254fe75891211b98b237.png" width="40" height="40"> Armor Discipline Rating</th>
                            <td><b>{dis}</b></td>
                          </tr>
                          <tr>
                            <th scope="row"><img src="https://www.bungie.net/common/destiny2_content/icons/59732534ce7060dba681d1ba84c055a6.png" width="40" height="40"> Armor Intellect Rating</th>
                            <td><b>{inte}</b></td>
                          </tr>
                          <tr>
                            <th scope="row"><img src="https://www.bungie.net/common/destiny2_content/icons/c7eefc8abbaa586eeab79e962a79d6ad.png" width="40" height="40"> Armor Strength Rating</th>
                            <td><b>{stre}</b></td>
                          </tr>
                          <tr>
                            <th scope="row">Armor Total</th>
                            <td><b>{total}</b></td>
                          </tr>""".format(mob = perks["statRolls"][1],res = perks["statRolls"][2],rec = perks["statRolls"][3],dis = perks["statRolls"][4],inte = perks["statRolls"][5],stre = perks["statRolls"][6],total = perks["statRolls"][0])

    return htmlStr


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
    location = data["Location"]
    planet = data["Planet"]
    landingZone = data["Landing Zone"]
    week = data["Week"]
    exoticWeaponName = data["Exotics"]["Exotic Weapon"]["name"]
    exoticWeaponPerkIcon = data["Exotics"]["Exotic Weapon"]["weaponPerks"][0]["perkIcon"]
    exoticWeaponPerkName = data["Exotics"]["Exotic Weapon"]["weaponPerks"][0]["name"]
    exoticWeaponPerkDesc = data["Exotics"]["Exotic Weapon"]["weaponPerks"][0]["description"]
    exoticWeaponType = data["Exotics"]["Exotic Weapon"]["type"].replace("Exotic ","")
    exoticWeaponIcon = data["Exotics"]["Exotic Weapon"]["icon"]
    exoticWeaponLoreExt = data["Exotics"]["Exotic Weapon"]["ExtLore"].replace("\n","<br><br>")
    exoticWarlockLoreExt = data["Exotics"]["Warlock Exotic"]["ExtLore"].replace("\n","<br>")
    exoticHunterLoreExt = data["Exotics"]["Hunter Exotic"]["ExtLore"].replace("\n","<br>")
    exoticTitanLoreExt = data["Exotics"]["Titan Exotic"]["ExtLore"].replace("\n","<br>")
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
   
    exoticWarlockPerkName = data["Exotics"]["Warlock Exotic"]["exoticArmorPerk"][0]["name"]
    exoticWarlockPerkIcon = data["Exotics"]["Warlock Exotic"]["exoticArmorPerk"][0]["icon"]
    exoticWarlockPerkDesc = data["Exotics"]["Warlock Exotic"]["exoticArmorPerk"][0]["desc"]

    exoticHunterPerkName = data["Exotics"]["Hunter Exotic"]["exoticArmorPerk"][0]["name"]
    exoticHunterPerkIcon = data["Exotics"]["Hunter Exotic"]["exoticArmorPerk"][0]["icon"]
    exoticHunterPerkDesc = data["Exotics"]["Hunter Exotic"]["exoticArmorPerk"][0]["desc"]

    exoticTitanPerkName = data["Exotics"]["Titan Exotic"]["exoticArmorPerk"][0]["name"]
    exoticTitanPerkIcon = data["Exotics"]["Titan Exotic"]["exoticArmorPerk"][0]["icon"]
    exoticTitanPerkDesc = data["Exotics"]["Titan Exotic"]["exoticArmorPerk"][0]["desc"]

    exoticWeaponLoreExt = str(exoticWeaponLoreExt).replace("\n","<br>")
    exoticHunterLoreExt = str(exoticHunterLoreExt).replace("\n","<br>")
    exoticWarlockLoreExt = str(exoticWarlockLoreExt).replace("\n","<br>")
    exoticTitanLoreExt = str(exoticTitanLoreExt).replace("\n","<br>")

    
    htmlTemp ="""<!DOCTYPE html>
<html lang="en">
<head>
    <title>X&#251r Tracker // Exotics</title>
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
                    <a class="nav-link active" aria-current="page" href="exotics">Exotic Items</a>
                    <a class="nav-link active" href="legendary-weapons">Legendary Weapons</a>
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
        <div class="row ">
            <div class="col-12">
                <br>
                <br>
                <h1 style="text-align:center;">
                    X&#251r's Exotic Items for {week}
                </h1>
                <br>
                <br>
            </div>
        </div>
    </div>
    <div class="container">
        <h2>Exotic Weapons</h2>
        <div class="row justify-content-around" style="word-break:normal; width: 100%;">
            <hr>
            <br>
            <div class="col-lg-4 col-md-12">
                <br>
                <table class="table table-borderless" style="color: #ffffff;">
                    <thead>
                        <tr>
                            <th><img src="{exoticWeaponIcon}" class="img" width="100px" alt="exotic-warlock"></th>
                            <th style="vertical-align:middle;"><img src="{exoticWeaponPerkIcon}" class="img"
                                    alt="exotic-warlock-perk" width="75" data-bs-toggle="tooltip" data-bs-offset="100,0"
                                    data-bs-html="true" data-bs-placement="bottom"
                                    title="<p>{exoticWeaponPerkDesc}</p>"></img></th>
                            <th style="vertical-align:middle;">
                                <h4>{exoticWeaponPerkName}</h4>
                            </th>
                        </tr>
                    </thead>
                </table>
                <div class="weaponData">
                    <h4>{exoticWeaponName}</h4>
                    <p>{exoticWeaponType}<br></p>
                    <div class="d-flex p-4 justify-content-start" style="height: 94px;">
                        <i style="height: 50px;">{exoticWeaponLore}</i>
                    </div>
                    <br>
                    <table class="table-sm table-borderless" style="height: 300px;">
                        <thead>
                            <tr>
                                <th scope="col" style="white-space: nowrap; max-width: 50px;">Weapon Perks</th>
                            </tr>
                        </thead>
                        <tbody>
                            {exoticWeaponPerkTable}
                        </tbody>
                    </table>
                    <br>

                    <div class="accordion" id="ExoticWeaponLore" style="margin-top: 2px;">
                        <div class="accordion-item" style="background-color: #0e1010; border-color: #ffffff;">
                            <h2 class="accordion-header" id="headingOne"
                                style="background-color: #0e1010; border-color: #ffffff;">
                                <button class="accordion-button" type="button" data-bs-toggle="collapse"
                                    style="background-color: #0e1010; color: #ffffff;" data-bs-target="#collapseOne"
                                    aria-expanded="true" aria-controls="collapseOne">
                                    Weapon Lore
                                </button>
                            </h2>
                            <div id="collapseOne" class="accordion-collapse collapse" aria-labelledby="headingOne"
                                data-bs-parent="#accordionExample">
                                <div class="accordion-body">
                                    <p>
                                    <h2>{exoticWeaponName}</h2>
                                    <hr>
                                    <p>{exoticWeaponLoreExt}</p>
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="col-lg-4 col-md-6">
                <br>
                <table class="table table-borderless" style="color: #ffffff;">
                    <thead>
                        <tr>
                            <th><img src="https://www.bungie.net/common/destiny2_content/icons/bc462cdde2fa00c808ff4f15802cb3b4.jpg"
                                    class="img" width="100px" alt="exotic-warlock"></th>
                            <th style="vertical-align:middle;"><img
                                    src="https://www.bungie.net/common/destiny2_content/icons/db83b69527ca8373f2803386e3d0a086.png"
                                    class="img" alt="exotic-warlock-perk" width="75" data-bs-toggle="tooltip"
                                    data-bs-offset="100,0" data-bs-html="true" data-bs-placement="bottom"
                                    title="<p>Final blows and precision hits with Hawkmoon grant stacks of Paracausal Charge. The final round in the magazine deals bonus damage based on the number of stacks. Stowing Hawkmoon on the final round removes this bonus.</p>"></img>
                            </th>
                            <th style="vertical-align:middle;">
                                <h4>Paracausal Shot</h4>
                            </th>
                        </tr>
                    </thead>
                </table>
                <div class="weaponData">
                    <h4>Hawkmoon</h4>
                    <p>Hand Cannon<br></p>
                    <div class="d-flex p-4 justify-content-start" style="height: 96px;">
                        <i>Stalk thy prey and let loose thy talons upon the Darkness.<br></i><br>
                    </div>
                    <br>
                    <table class="table-sm table-borderless" style="height: 300px;">
                        <thead>
                            <tr>
                                <th scope="col" style="white-space: nowrap; max-width: 50px;">Weapon Perks</th>
                            </tr>
                        </thead>
                        <tbody>
                            {hawkmoonWeaponPerkTable}
                        </tbody>
                    </table>
                    <br>
                    <div class="accordion" id="HawkmoonLore">
                        <div class="accordion-item" style="background-color: #0e1010; border-color: #ffffff;">
                            <h2 class="accordion-header" id="headingTwo"
                                style="background-color: #0e1010; border-color: #ffffff;">
                                <button class="accordion-button" type="button" data-bs-toggle="collapse"
                                    style="background-color: #0e1010; color: #ffffff;" data-bs-target="#collapseTwo"
                                    aria-expanded="true" aria-controls="collapseTwo">
                                    Weapon Lore
                                </button>
                            </h2>
                            <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo"
                                data-bs-parent="#accordionExample">
                                <div class="accordion-body">
                                    <p>
                                    <h2>Hawkmoon</h2>
                                    <hr>
                                    <p>What is this feeling?<br><br>I did not ask for it. I do not understand it. I do
                                        not want it.<br><br>The Crow is so carefree in his ignorance. The bonfire's glow
                                        lights up his pale features and I am drawn to the hope in his gold eyes. Where
                                        is the despairing child I anticipated?<br><br>He drinks from an open bottle of
                                        wine against the recommendation of his Ghost. The Guardian encourages him and
                                        they are laughing. This celebration is maddening; neither have reason to be so
                                        jubilant. Their world is ending and they thrash like dying creatures in the
                                        final light of collapsing stars. They do not seem to acknowledge the futility of
                                        their existence, the impermanence of it in the face of cosmic
                                        annihilation.<br><br>Now the Guardian is drinking, standing close to the fire.
                                        Their Ghost, too, encourages them not to partake. They poison themselves for the
                                        enjoyment of it.<br><br>I am reminded of my sisters. Of moments spent by lapping
                                        shores, gazing up at infinite stars full of possibilities and wonder. I am left
                                        yearning.<br><br>What is this feeling?<br><br>I do not understand it. I do not
                                        want it.<br><br>They are celebrating their victory over the Taken. The Crow is
                                        making a gun shape with his hand, swinging the nearly empty bottle of wine
                                        around in the other like a Sword. The Guardian looks pensive, sitting on a rock
                                        by the fire, contemplating the secret they are keeping. The Crow notices, but
                                        tries not to show it. He wants the Guardian's spirits to be lifted. He wants to
                                        be supportive, so that they may share in their triumphs together.<br><br>As
                                        equals.<br><br>I am reminded of my home. I am reminded of the warmth of the sun
                                        and the embrace of my family. I am reminded of my father's face. I am reminded
                                        of everyone I betrayed. All the blood
                                        spilled in the name of immortality. The warmth of the sun burns me with its
                                        memory.<br><br>What is this feeling?<br><br>I do not want it.<br><br>The fire
                                        has nearly died. The Crow fell over and cannot stand, though he insists he is
                                        fine. The Guardian is turning the embers with the tip of their Sword. The Ghosts
                                        are talking to one another in quiet conspiracy. The celebration has ended, but I
                                        can sense their emotions are mixed: complex and myriad things, when a simple,
                                        singular focus would suffice.<br><br>There is a growing
                                        kinship here. Against better judgment.<br><br>What is this feeling?</p>
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <br>
            </div>

            <div class="col-lg-4 col-md-6">
                <br>
                <table class="table table-borderless" style="color: #ffffff;">
                    <thead>
                        <tr>
                            <th><img src="https://www.bungie.net/common/destiny2_content/icons/67634d7a01d7dca3aef90b4612d58489.jpg"
                                    class="img" width="100px" alt="exotic-warlock"></th>
                            <th style="vertical-align:middle;"><img
                                    src="https://www.bungie.net/common/destiny2_content/icons/0e171b3269c4796acad0c0b11c7fbc27.png"
                                    class="img" alt="exotic-warlock-perk" width="75" data-bs-toggle="tooltip"
                                    data-bs-offset="100,0" data-bs-html="true" data-bs-placement="bottom"
                                    title="<p>Chaining precision hits grants bonus damage and quickens reload speed.</p>"></img>
                            </th>
                            <th style="vertical-align:middle;">
                                <h4>Cranial Spike</h4>
                            </th>
                        </tr>
                    </thead>
                </table>
                <div class="weaponData">
                    <h4>Dead Man's Tale</h4>
                    <p>Scout Rifle<br></p>
                    <div class="d-flex p-4 justify-content-start" style="height: 96px;">
                        <i>&quotLong, short, they all end the same way. &quot<br>&#8212;Katabasis</i>
                    </div>
                    <br>
                    <table class="table-sm table-borderless" style="height: 300px;">
                        <thead>
                            <tr>
                                <th scope="col" style="white-space: nowrap; max-width: 50px;">Weapon Perks</th>
                            </tr>
                        </thead>
                        <tbody>
                            {deadMansTalePerkTable}
                        </tbody>
                    </table>
                    <br>
                    <div class="accordion" id="DMTLore">
                        <div class="accordion-item" style="background-color: #0e1010; border-color: #ffffff;">
                            <h2 class="accordion-header" id="headingThree"
                                style="background-color: #0e1010; border-color: #ffffff;">
                                <button class="accordion-button" type="button" data-bs-toggle="collapse"
                                    style="background-color: #0e1010; color: #ffffff;" data-bs-target="#collapseThree"
                                    aria-expanded="true" aria-controls="collapseThree">
                                    Weapon Lore
                                </button>
                            </h2>
                            <div id="collapseThree" class="accordion-collapse collapse" aria-labelledby="headingThree"
                                data-bs-parent="#accordionExample">
                                <div class="accordion-body">
                                    <p>
                                    <h2>Dead Man's Tale</h2>
                                    <hr>
                                    <p>Gaelin-4's war beast leads us through balmy Venusian jungle. Our rifles low, our
                                        Ghosts high in the canopy like sentry drones.<br><br>"My vehicle is old. Needs
                                        maintenance. Been running too long without cutting the engine," I
                                        say.<br><br>Gaelin sends me a sideways look. "That shipwright still around? She
                                        used to make cider in the autumn. I swear,
                                        she kept us like a pack of strays."<br><br>I sigh. "No, I mean this thing." I
                                        run my hand over my body. "Besides, you know I can't go back there." I
                                        straighten the leather wrap around my Tex-foundry rifle.<br><br>"You know I
                                        literally tune myself, right?" asks the Exo Hunter.<br><br>"Why? You're
                                        immortal."<br><br>"And you're not?"<br><br>"I know, but I'm&#8230 slower. I feel
                                        slower."<br><br>"Uh huh."<br><br>"Just not like what I used to feel like.
                                        Not&#8230 spry. Not up here either." I tap my helmet.<br><br>"Tragedy. I feel
                                        for you. Have Gilgamesh tune you then."<br><br>I chuckle. "Yeah&#8230 he'd love
                                        that."<br><br>"You two having issues again?"<br><br>I shake my head in a stiff,
                                        narrow lie. "You think we come back the same every time?"<br><br>"I do. Straight
                                        from the manufacturer ," Gaelin-4 says.<br><br>"Sometimes I get the
                                        feeling&#8230 something's different."<br><br>Gaelin stops and squints at
                                        me.<br><br>I dip my head and let my hood fall forward. "Nothing I can put my
                                        finger on, just little things. Adjustments."<br><br>"You think he's changing
                                        you?" Gaelin's voice sounds more serious than surprised.<br><br>I wait too long
                                        to answer. It's not because I don't know my answer, but because I want to feel
                                        like I still doubt it. I raise my head. Gaelin meets my eyes and looks up to the
                                        canopy.<br><br>He leans his shoulder into me and drops his voice to a whisper.
                                        "My Clip's a good one, but you need to realize Ghosts don't know anything.
                                        Nobody does. They're just like us. They get curious. They question. If you think
                                        something's coming unwound, you need to sit down and talk it
                                        out."<br><br>"Wait&#8230 did Clip change yo&#8212"<br><br>"Please," Gaelin
                                        scoffs. "You're paranoid." He turns to keep walking and calls back, "Life
                                        changes you. Same with them. I'm the only one that stays the
                                        same."<br><br>Gaelin raises a fist and we stop. His war beast sniffs the air and
                                        turns us east. We continue walking.<br><br>"What'd you name the
                                        beast?"<br><br>"Castus."<br><br>"You've been reading too many of the Spider's
                                        books ."<br><br>"Some of 'em are good."<br><br>I laugh. "Aren't you the man that
                                        said anything you got tying you down can be made into a noose?"<br><br>"Yeah,
                                        some time ago."<br><br>"You've been taking a lot of jobs with him ? Those
                                        Fallen?"<br><br>"You're one to talk, Emperor's lackey . Some of those Eliksni
                                        aren't so bad."</p>
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <br>
    </div>
    <div class="container">
        <br>
        <h2>Exotic Armors</h2>
        <hr>
        <br>
        <div class="row justify-content-around" style="font-size: 90%;">
            <div class="col-lg-4 col-md-12">
                <br>
                <h3 style="text-align: center;">Warlock Exotic
                    <hr>
                </h3>
                <br>
                <table class="table table-borderless" style="color: #ffffff;padding-left: 20%;">
                    <thead>
                        <tr>
                            <th><img src="{exoticWarlockIcon}" class="img" width="100" alt="exotic-warlock"></th>
                            <th style="vertical-align:middle;"><img src="{exoticWarlockPerkIcon}" class="img"
                                    alt="exotic-warlock-perk" width="75" data-bs-toggle="tooltip" data-bs-offset="100,0"
                                    data-bs-html="true" data-bs-placement="bottom"
                                    title="<p>{exoticWarlockPerkDesc}</p>"></img></th>
                            <th style="vertical-align:middle;">
                                <h4>{exoticWarlockPerkName}</h4>
                            </th>
                        </tr>
                    </thead>
                </table>
                <div class="armorData">
                    <h4>{exoticWarlockName}</h4>
                    <p>{exoticWarlockType}</p>
                    <div class="d-flex p-4">
                        <i style="height: 120px;">{exoticWarlockLore}</i>
                    </div>

                    <table class="table table-bordered" style="color: #ffffff;padding-left: 20%;">
                        <thead>
                            <tr>
                                <th scope="row">Statistic</th>
                                <td><b>Roll</b></td>
                            </tr>
                        </thead>
                        <tbody>
                            {exoticWarlockStatTable}
                        </tbody>
                    </table>
                    <br>
                    <div class="accordion" id="warlockLore">
                        <div class="accordion-item" style="background-color: #0e1010; border-color: #ffffff;">
                            <h2 class="accordion-header" id="headingFour"
                                style="background-color: #0e1010; border-color: #ffffff;">
                                <button class="accordion-button" type="button" data-bs-toggle="collapse"
                                    style="background-color: #0e1010; color: #ffffff;" data-bs-target="#collapseFour"
                                    aria-expanded="true" aria-controls="collapseFour">
                                    Armor Lore
                                </button>
                            </h2>
                            <div id="collapseFour" class="accordion-collapse collapse" aria-labelledby="headingFour"
                                data-bs-parent="#accordionExample">
                                <div class="accordion-body">
                                    <p>
                                    <h2>{exoticWarlockName}</h2>
                                    <hr>
                                    <p>{exoticWarlockLoreExt}</p>
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="col-lg-4 col-md-6">
                <br>
                <h3 style="text-align: center;">Hunter Exotic
                    <hr>
                </h3>
                <br>
                <table class="table table-borderless" style="color: #ffffff;padding-left: 20%;">
                    <thead>
                        <tr>
                            <th><img src="{exoticHunterIcon}" class="img" width="100px" alt="exotic-warlock"></th>
                            <th style="vertical-align:middle;"><img src="{exoticHunterPerkIcon}" class="img"
                                    alt="exotic-warlock-perk" width="75" data-bs-toggle="tooltip" data-bs-offset="100,0"
                                    data-bs-html="true" data-bs-placement="bottom"
                                    title="<p>{exoticHunterPerkDesc}</p>"></img></th>
                            <th style="vertical-align:middle;">
                                <h4>{exoticHunterPerkName}</h4>
                            </th>
                        </tr>
                    </thead>
                </table>
                <div class="armorData">
                    <h4>{exoticHunterName}</h4>
                    <p>{exoticHunterType}</p>
                    <div class="d-inline-flex p-4">
                        <i style="height: 120px;">{exoticHunterLore}</i>
                    </div>

                    <table class="table table-bordered" style="color: #ffffff;padding-left: 20%;">
                        <thead>
                            <tr>
                                <th scope="row">Statistic</th>
                                <td><b>Roll</b></td>
                            </tr>
                        </thead>
                        <tbody>
                            {exoticHunterStatTable}
                        </tbody>
                    </table>
                    <br>
                    <div class="accordion" id="HunterLore">
                        <div class="accordion-item" style="background-color: #0e1010; border-color: #ffffff;">
                            <h2 class="accordion-header" id="headingFive"
                                style="background-color: #0e1010; border-color: #ffffff;">
                                <button class="accordion-button" type="button" data-bs-toggle="collapse"
                                    style="background-color: #0e1010; color: #ffffff;" data-bs-target="#collapseFive"
                                    aria-expanded="true" aria-controls="collapseFive">
                                    Armor Lore
                                </button>
                            </h2>
                            <div id="collapseFive" class="accordion-collapse collapse" aria-labelledby="headingFive"
                                data-bs-parent="#accordionExample">
                                <div class="accordion-body">
                                    <p>
                                    <h2>{exoticHunterName}</h2>
                                    <hr>
                                    <p>{exoticHunterLoreExt}</p>
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="col-lg-4 col-md-6">
                <br>
                <h3 style="text-align: center;">Titan Exotic
                    <hr>
                </h3>
                <br>
                <table class="table table-borderless" style="color: #ffffff;padding-left: 20%;">
                    <thead>
                        <tr>
                            <th><img src="{exoticTitanIcon}" class="img" width="100px" alt="exotic-warlock"></th>
                            <th style="vertical-align:middle;"><img src="{exoticTitanPerkIcon}" class="img"
                                    alt="exotic-warlock-perk" width="75" data-bs-toggle="tooltip" data-bs-offset="100,0"
                                    data-bs-html="true" data-bs-placement="bottom"
                                    title="<p>{exoticTitanPerkDesc}</p>"></img></th>
                            <th style="vertical-align:middle;">
                                <h4>{exoticTitanPerkName}</h4>
                            </th>
                        </tr>
                    </thead>
                </table>
                <div class="armorData">
                    <h4>{exoticTitanName}</h4>
                    <p>{exoticTitanType}</p>
                    <div class="d-inline-flex p-4">
                        <i style="height: 120px;">{exoticTitanLore}</i>
                    </div>

                    <table class="table table-bordered" style="color: #ffffff;padding-left: 20%;">
                        <thead>
                            <tr>
                                <th scope="row">Statistic</th>
                                <td><b>Roll</b></td>
                            </tr>
                        </thead>
                        <tbody>
                            {exoticTitanStatTable}
                        </tbody>
                    </table>
                    <br>
                    <div class="accordion" id="titanLore">
                        <div class="accordion-item" style="background-color: #0e1010; border-color: #ffffff;">
                            <h2 class="accordion-header" id="headingSix"
                                style="background-color: #0e1010; border-color: #ffffff;">
                                <button class="accordion-button" type="button" data-bs-toggle="collapse"
                                    style="background-color: #0e1010; color: #ffffff;" data-bs-target="#collapseSix"
                                    aria-expanded="true" aria-controls="collapseSix">
                                    Armor Lore
                                </button>
                            </h2>
                            <div id="collapseSix" class="accordion-collapse collapse" aria-labelledby="headingSix"
                                data-bs-parent="#accordionExample">
                                <div class="accordion-body">
                                    <p>
                                    <h2>{exoticTitanName}</h2>
                                    <hr>
                                    <p>{exoticTitanLoreExt}</p>
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="container">
        <br>
        <h1>General Exotic Items</h1>
        <hr>
        <br>
        <div class="row justify-content-around gx-5">
            <div class="col-md-6">
                <br>
                <h2 style="text-align: center;">Exotic Cipher
                    <hr>
                </h2>
                <img src="https://www.bungie.net/common/destiny2_content/icons/7f9e6e79bb7a8ce59de9258a7d674af2.jpg"
                    class="img" alt="exotic-engram">
                <div class="armorData">
                    <b>A Question</b>
                    <p>Complete activities in Vanguard, Crucible, or Gambit playlists to earn an Exotic Cipher</p>
                    <em>"The Nine simply wish to learn. I am the instrument, and you are the subject." —X&#251r</em>
                </div>
                <br>
                <br>
                <div class="accordion" id="engramLore">
                    <div class="accordion-item" style="background-color: #0e1010; border-color: #ffffff;">
                        <h2 class="accordion-header" id="headingseven"
                            style="background-color: #0e1010; border-color: #ffffff;">
                            <button class="accordion-button" type="button" data-bs-toggle="collapse"
                                style="background-color: #0e1010; color: #ffffff;" data-bs-target="#collapseseven"
                                aria-expanded="true" aria-controls="collapseseven">
                                Item Lore
                            </button>
                        </h2>
                        <div id="collapseseven" class="accordion-collapse collapse" aria-labelledby="headingseven"
                            data-bs-parent="#accordionExample">
                            <div class="accordion-body">
                                <p>
                                <h2>You Get Used to Him</h2>
                                <hr>
                                <p>There is a strange fellow who&#8230 well, perhaps you've seen him. He doesn't really
                                    come and go as you or I might traditionally think. It's more that you turn around,
                                    and he is either there or he is not. His appearances are steady and predictable, at
                                    least. He's called X&#251r. I'm not sure why one draws the tiny arrow over his name,
                                    but it's important
                                    to try and respect the wishes of those we don't understand.<br><br>The first time I
                                    ever saw X&#251r, I was by myself at my stall in the Tower. The Old Tower, I suppose
                                    you'd call
                                    it now. I hadn't been there long at all. I looked up, and this man had appeared,
                                    seemingly out of nowhere! His back was to me, but even from behind, something seemed
                                    off about
                                    him. Something in his posture. As he started to turn, I noticed his whole face
                                    appeared to be covered in hair. It even seemed to be moving, gently flowing on its
                                    own&#8212but there was no wind.<br><br>When the light hit his face, I screamed and
                                    ducked down behind part of my cabinets. I was sure this abomination had come to
                                    invade us, that more of them were just out of sight, that we were done
                                    for.<br><br>Eventually, I realized no one else was screaming. I heard no sounds of
                                    distress. I peeked out and saw that everyone was
                                    going about their business. No one was panicking but me! Many people saw
                                    him&#8212several were interacting with him.<br><br>Slowly, I stood back up and tried
                                    to go about my business&#8212though I rarely looked away. Tess came over before too
                                    long, and I asked her about the strange figure.<br><br>"Oh, that's X&#251r!" she
                                    said, unconcerned. "He comes through every so often and sells particular,
                                    hard-to-find things." She considered him for a moment, then added, "Could do with a
                                    bit of a wardrobe update, if you ask me, but he's otherwise harmless."<br><br>"What
                                    is he?" I asked. "I've never seen a creature like that before."<br><br>"X&#251r
                                    is&#8230 I believe he's called a Jovian. They're from out beyond even the Reef. I'm
                                    afraid I don't know much else about them."<br><br>"But they're&#8230
                                    friendly?"<br><br>"Well, they don't attack us, if that's what you mean. I don't know
                                    that
                                    I'd call X&#251r friendly, but he's not hostile."<br><br>I felt more at ease after
                                    our conversation, though I still could not shake my fear. For many months, I jumped
                                    every time I
                                    saw him and had to fight back the instinct to hide.<br><br>Eventually, I grew used
                                    to his presence. I even began to appreciate his predictability&#8212it became a
                                    symbol that everything was functioning as it should. The fear evaporated with
                                    time.<br><br>I have often found that my first reaction to new things is fear.
                                    Perhaps it is this way for everyone. However, I have also found that if I accept and
                                    acknowledge my fear, it is easier to push through until I am no longer afraid. The
                                    new thing has almost never been as frightening as I first feared.</p>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
            <div class="col-md-6">
                <br>
                <h2 style="text-align: center;">Exotic Engram
                    <hr>
                </h2>
                <img src="https://www.bungie.net/common/destiny2_content/icons/ee21b5bc72f9e48366c9addff163a187.png"
                    class="img" alt="exotic-engram">
                <div class="armorData">
                    <b>Exotic Engram</b>
                    <p>An engram with a predestined outcome. Contains a new Exotic if any of the possible rewards remain
                        to be collected.</p>
                </div>
                <br>
                <br>

                <div class="accordion" id="engramLore">
                    <div class="accordion-item" style="background-color: #0e1010; border-color: #ffffff;">
                        <h2 class="accordion-header" id="headingeight"
                            style="background-color: #0e1010; border-color: #ffffff;">
                            <button class="accordion-button" type="button" data-bs-toggle="collapse"
                                style="background-color: #0e1010; color: #ffffff;" data-bs-target="#collapseeight"
                                aria-expanded="true" aria-controls="collapseeight">
                                Engram Lore
                            </button>
                        </h2>
                        <div id="collapseeight" class="accordion-collapse collapse" aria-labelledby="headingeight"
                            data-bs-parent="#accordionExample">
                            <div class="accordion-body">
                                <p>
                                <h2>Engrams</h2>
                                <hr>
                                <h6>In ancient times, Earthlings thought there were three states of matter. We now know
                                    there to be four: solid, liquid, gas and engram. Of these, the engram is the purest
                                    state of matter.<br><br>The role of the Cryptarchy is to encrypt and safeguard
                                    civilization's informational infrastructure, not to decrypt anything and everything
                                    for any lowdown scavenger who happens upon an engram.</h6>
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
                        <br> Have an issue or suggestion? Please submit it <a href="https://github.com/lulamae12/xurtracker.com/issues">here!</a>
                        
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

</html>""".format(week=week,landingZone=landingZone,location=location,planet=planet,exoticWeaponIcon=exoticWeaponIcon,
    exoticWeaponName=exoticWeaponName,exoticWeaponType=exoticWeaponType,exoticWeaponPerkTable=exoticWeaponPerkTable,
    hawkmoonWeaponPerkTable=hawkmoonWeaponPerkTable,hawkmoonRating=hawkmoonRating,deadMansTalePerkTable=deadMansTalePerkTable,
    deadMansTaleRating=deadMansTaleRating,exoticWarlockIcon=exoticWarlockIcon,exoticWarlockName=exoticWarlockName,exoticWarlockType=exoticWarlockType,
    exoticWarlockStatTable=exoticWarlockStatTable,exoticHunterIcon=exoticHunterIcon,exoticHunterName=exoticHunterName,exoticHunterType=exoticHunterType,
    exoticHunterStatTable=exoticHunterStatTable,exoticTitanIcon=exoticTitanIcon,exoticTitanName=exoticTitanName,exoticTitanType=exoticTitanType,
    exoticTitanStatTable=exoticTitanStatTable,exoticWarlockLore=exoticWarlockLore,exoticHunterLore=exoticHunterLore,exoticTitanLore=exoticTitanLore,exoticWeaponLore=exoticWeaponLore,
    exoticWeaponLoreExt=exoticWeaponLoreExt,exoticWarlockLoreExt=exoticWarlockLoreExt,exoticHunterLoreExt=exoticHunterLoreExt,exoticTitanLoreExt=exoticTitanLoreExt,
    exoticWarlockPerkName=exoticWarlockPerkName,exoticWarlockPerkIcon=exoticWarlockPerkIcon,exoticWarlockPerkDesc=exoticWarlockPerkDesc,exoticHunterPerkName=exoticHunterPerkName,exoticHunterPerkIcon=exoticHunterPerkIcon,exoticHunterPerkDesc=exoticHunterPerkDesc,exoticTitanPerkName=exoticTitanPerkName,exoticTitanPerkIcon=exoticTitanPerkIcon,exoticTitanPerkDesc=exoticTitanPerkDesc,
    exoticWeaponPerkIcon=exoticWeaponPerkIcon,exoticWeaponPerkName=exoticWeaponPerkName,exoticWeaponPerkDesc=exoticWeaponPerkDesc)

    
    htmlTemp = cleanHTML(htmlTemp)
    text_file = open("/home/ubuntu/XurTracker/templates/exotic_items.html", "w")
    text_file.write(htmlTemp)
    text_file.close()



setHtmlVals()