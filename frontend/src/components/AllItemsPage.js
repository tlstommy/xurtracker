import React, { useState } from "react";

import CurrentLocation from "./CurrentLocation";
import SectionHeader from "./SectionHeader";
import ExoticWeapon from "./ExoticWeapon";
import DualPerkHover from "./DualPerkHover";
import ExoticArmor from "./ExoticArmor";
import ArtificeArmor from "./ArtificeArmor";
import ExoticCatalyst from "./ExoticCatalyst";
import LegendaryArmor from "./LegendaryArmor";
import LegendaryWeapon from "./LegendaryWeapon";
import ClassSelect from "./ClassSelect";
import Item from "./Item";
import MiscellaneousItem from "./MiscellaneousItem";

import destinyData from '../destinyData.json';

export default function AllItemsPage() {

    const exoticWeapons = destinyData.Exotics["Exotic Weapons"];
    const hawkmoon = destinyData.Exotics.Hawkmoon;

    const exoticArmors = [destinyData.Exotics["Hunter Exotic"],destinyData.Exotics["Warlock Exotic"],destinyData.Exotics["Titan Exotic"]];
    const legendaryWeapons = destinyData.Legendaries["Legendary weapons"];

    const miscItems = destinyData["Miscellaneous Offers"];

    const artificeBeingSold = destinyData.Artifice;
    const artificeArmors = [destinyData["Artifice Armor"].Hunter,destinyData["Artifice Armor"].Warlock,destinyData["Artifice Armor"].Titan]

    const materialSales = destinyData["Material Offers"];

    const catalysts = [destinyData.Catalysts.Primary,destinyData.Catalysts.Secondary]


    const legendaryArmors  = {
        Hunter:destinyData.Legendaries["Hunter"],
        Warlock:destinyData.Legendaries["Warlock"],
        Titan:destinyData.Legendaries["Titan"]
    };
    //default to warlock
    const [selectedClass, setSelectedClass] = useState("Warlock");

    const handleClassChange = (newClass) => {
        setSelectedClass(newClass);
    };

    function ArtificeArmorCheck({artificeForSale}){
        if(artificeBeingSold){
            return (
                <div>
                    <SectionHeader title="Artifice Armor"/>
                    <div class="grid grid-cols-1 lg:grid-cols-3 justify-evenly gap-2 p-4 items-stretch">
                        {Object.keys(artificeArmors).map((key) => (              
                            <ArtificeArmor classKey={key} data={artificeArmors[key]} />

                        ))}
                    </div>                    
                </div>
            );
        }else{
            return null
        }
    }

    function MiscExoticsCheck(){
        if(miscItems.length !== 0){
            return(
                <div>
                    <SectionHeader title="Miscellaneous Exotic Items"/>    
                </div>
            );
        }
    }


    console.log(selectedClass)

    return (
        <div className="min-h-screen flex flex-col">
            <div className="flex flex-1 flex-col sm:flex-row">
                <nav className="md:w-32 lg:w-36 order-first sm:order-none"></nav>
                <main className="flex-1">
                    <h1 className="page-title text-3xl md:text-4xl text-white text-center mt-24 font-bold mx-12 ">
                        Xûr's Inventory for {destinyData.Week}
                    </h1>
                    
                    <section id="material-offers" className="pt-5">
                        <SectionHeader title="Strange Material Offers"/>
                        
                        <div className="justify-around w-full">
                            <div className="material-sales grid grid-cols-1 md:grid-cols-2 md:grid-rows-2 lg:grid-cols-3 grid-rows-2 gap-6 p-4 justify-evenly">
                                {materialSales.map((item, index) => (
                                <Item key={index} data={item} />
                                ))}
                            </div>
                        </div>
                    </section>
                    
                    
                    <section id="exotic-weapons" className="pt-5">
                        <SectionHeader title="Exotic Weapons"/>
                        <div class="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 justify-evenly gap-1 p-4 items-stretch">
                        
                            {Object.keys(exoticWeapons).map((key) => (              
                                <ExoticWeapon key={exoticWeapons[key].itemHash} data={exoticWeapons[key]} />
                            
                            ))}
                            <ExoticWeapon key={hawkmoon.itemHash} data={hawkmoon} />
                            <ExoticCatalyst data={catalysts[0]}/>
                            <ExoticCatalyst data={catalysts[1]}/>
                        </div>
                    </section>    
                    
                    <section id="exotic-armor" className="pt-5">
                        <SectionHeader title="Exotic Armor"/>    
                        <div class="grid grid-cols-1 lg:grid-cols-3 justify-evenly gap-2 p-4 items-stretch">
                            {Object.keys(exoticArmors).map((key) => (              
                                <ExoticArmor key={exoticArmors[key].itemHash} classKey={key} data={exoticArmors[key]} />
                            ))}
                        </div>
                    </section>
                    
                    <section id="artifice" className="pt-5">
                        <ArtificeArmorCheck artificeForSale={artificeBeingSold}/>
                    </section>

                    <section id="misc-exotics" className="pt-5">
                        <MiscExoticsCheck /> 
                        <div class="grid grid-cols-1 lg:grid-cols-3 justify-evenly gap-2 p-4 items-stretch">
                            {Object.keys(miscItems).map((key) => (              
                                <MiscellaneousItem key={miscItems[key].hash} data={miscItems[key]} />
                            ))}
                        </div>
                    </section>
                    
                    <section id="legendary-weapons" className="pt-5">
                        <SectionHeader title="Legendary Weapons"/>
                        <div class="grid grid-cols-1 lg:grid-cols-3 justify-evenly gap-2 p-4 pt-2 items-stretch">
                            {Object.keys(legendaryWeapons).map((key) => (              
                                <LegendaryWeapon key={legendaryWeapons[key].itemHash} data={legendaryWeapons[key]} />
                            ))}
                        </div>
                    </section>
                    
                

                    <section id="legendary-armor" className="pt-5">
                        <SectionHeader title="Legendary Armor"/>
                        <ClassSelect selectedClass={selectedClass} setSelectedClass={setSelectedClass} />
                        <div class="grid grid-cols-1 md:grid-cols-1 justify-evenly gap-4 p-4 items-stretch">
                            {Object.keys(legendaryArmors[selectedClass]).map((key) => (              
                                
                                <LegendaryArmor data={legendaryArmors[selectedClass][key]} itemType={legendaryArmors[selectedClass][key]} />
                            ))}
                        </div>
                    </section>
                    
                    
                
                </main>
                <aside className="md:w-32 lg:w-36 hidden  sm:block"></aside>
            </div>
            <div className="mb-0 pt-20 pb-0">
                <footer className=" p-4 py-auto text-gray-400 text-center w-full">
                    Created with {`<3`} by Tommy Smith
                    <br/>
                    <i className="text-sm">
                        Xûr & all related media © Bungie
                    </i>
                </footer>
            </div>
                
        </div>
        

    );
}
