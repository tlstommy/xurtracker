import React, { useState } from "react";
import { motion } from "framer-motion"

import LegendaryWeaponDetailed from "./LegendaryWeaponDetailed";
import Perk from "./Perk"
import FramePerk from "./FramePerk";
import Masterwork from "./Masterwork";

import {ReactComponent as PrimaryAmmoIcon} from "../assets/icons/ammo-primary.svg";
import {ReactComponent as SpecialAmmoIcon} from "../assets/icons/ammo-special.svg";
import {ReactComponent as HeavyAmmoIcon} from "../assets/icons/ammo-heavy.svg";


export default function LegendaryWeapon(props) {
    
    const [isOpen, setOpen] = useState(false);

    const {data} = props;

    const ammoTypeIcon = {

        1: <PrimaryAmmoIcon style={{ width: "2em", height: "2em"}} />,
        2: <SpecialAmmoIcon style={{ width: "2em", height: "2em"}} />,
        3: <HeavyAmmoIcon style={{ width: "2em", height: "2em"}} />

    }
    
    const modalIndex = {zIndex: 100};

    return (
        <div className="h-full">
            <div className="flex justify-center h-full p-4 ">
                <div className="hover:outline hover:outline-white w-full z-1 max-w-xs sm:max-w-md bg-ui-grey rounded-lg border border-gray-700 shadow-xl cursor-pointer" onClick={() => setOpen(true)}>
                    <div className="bg-purple-900 p-2 b rounded-t-lg">
                        <h2 className="text-md sm:text-lg font-bold flex items-center justify-center">
                            {ammoTypeIcon[data.ammoType]}
                            &nbsp;
                            <img className="weapon-damage-icon mr-2" alt="weapon damage type icon" src={data.damageTypeIcon}/>
                            
                        </h2>
                    </div>
                    <div className="mt-1">  
                        <h3 className="text-xl sm:text-2xl font-bold text-gray-100 text-center underline-offset-4">{data.name}</h3>
                        <p className="text-md sm:text-md text-gray-100 text-center">{data.legendWeaponDamageType} {'//'} {data.type.replace("Legendary", "")}</p>
                    </div>
                    <div className="p-4">    
                        <img className="object-center border-2 mx-auto w-20 my-2" alt="weapon icon" src={data.icon} />
                                                 
                        <div className="weapon-perks pt-4 ">
                            <h3 className="text-lg sm:text-xl font-bold text-gray-100 text-start underline-offset-4 py-2 border-b">Perks </h3>
                            
                            <div className="grid grid-cols-5 grid-rows-1 pt-2 gap-1 py-1 grid-background">
                                <div className="perkCol-0">
                                    
                                    
                                    <div className='group relative p-1 sm:p-1'  onClick={(e) => {e.stopPropagation();}}>
                                        <FramePerk name={data.legendWeaponFrame.name} image={data.legendWeaponFrame.icon} description={data.legendWeaponFrame.description} imageSize={"4rem"}/>
                                    </div>
                                    <div className='group relative p-2 sm:p-2 '  onClick={(e) => {e.stopPropagation();}}>
                                        <Masterwork name={data.masterworkData.name} image={data.masterworkData.icon} description={data.masterworkData.description} imageSize={"3.5rem"}/>
                                    </div>
                                    
                                </div>
                                <div className="perkCol-1">
                                    
                                    {data.weaponPerks.slice(0,2).map((perk, index) => (
                                        <div className='group relative p-1 sm:p-1 ' key={perk.hashID} onClick={(e) => {e.stopPropagation();}}>
                                            <Perk image={perk.perkIcon}
                                                
                                                name={perk.name}
                                                type={perk.perkType}
                                                subtype={perk.perkSubType}
                                                description={perk.description}
                                            />
                                            
                                        </div>
                                    ))}
                                </div>
                                <div className="perkCol-2" >
                                    {data.weaponPerks.slice(2,4).map((perk, index) => (
                                        <div className='group relative p-1 sm:p-1' key={perk.hashID} onClick={(e) => {e.stopPropagation();}}>
                                            
                                            <Perk image={perk.perkIcon}
                                                
                                                name={perk.name}
                                                type={perk.perkType}
                                                subtype={perk.perkSubType}
                                                description={perk.description}
                                            />
                                            
                                        </div>
                                    ))}
                                </div>
                                {data.weaponPerks.slice(4,6).map((perk, index) => (
                                    <div className="cols-3-4" >
                                        <div className='group relative p-1 sm:p-1' key={perk.hashID} onClick={(e) => {e.stopPropagation();}}>
                                        <Perk image={perk.perkIcon}
                                                name={perk.name}
                                                
                                                type={perk.perkType}
                                                subtype={perk.perkSubType}
                                                description={perk.description}
                                            />
                                            
                                        </div>
                                    </div>
                                ))}
                                
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            {isOpen && (
                <div className="fixed inset-0" style={modalIndex}>
                    <LegendaryWeaponDetailed data={data} isOpen={isOpen} setOpen={setOpen} onClose={() => setOpen(false)}/>
                </div>
            )}
        </div>
    );
}
