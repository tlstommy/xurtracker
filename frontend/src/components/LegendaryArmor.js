import React, { useState } from "react";

import LegendaryArmorDetailed from "./LegendaryArmorDetailed";


import {ReactComponent as HelmetIcon} from "../assets/icons/helmet.svg";
import {ReactComponent as ArmIcon} from "../assets/icons/gloves.svg";
import {ReactComponent as ChestIcon} from "../assets/icons/chest.svg";
import {ReactComponent as BootsIcon} from "../assets/icons/boots.svg";
import {ReactComponent as ClassItemIcon} from "../assets/icons/classitem.svg";

import {ReactComponent as MobilityIcon} from "../assets/icons/mobility.svg";
import {ReactComponent as ResilienceIcon} from "../assets/icons/resilience.svg";
import {ReactComponent as RecoveryIcon} from "../assets/icons/recovery.svg";
import {ReactComponent as DisciplineIcon} from "../assets/icons/discipline.svg";
import {ReactComponent as IntellectIcon} from "../assets/icons/intellect.svg";
import {ReactComponent as StrengthIcon} from "../assets/icons/strength.svg";



export default function LegendaryArmor(props) {
    const [isOpen, setOpen] = useState(false);


    const {data,itemType} = props;

    const statNames = ["Mobility","Resilience","Recovery","Discipline","Intellect","Strength"]
    
    const armorIcons = {
        "Legendary Helmet": <HelmetIcon style={{ width: "2em", height: "2em", display: "block", fill:"white"  }} />,
        "Legendary Gauntlets": <ArmIcon style={{ width: "2em", height: "2em", display: "block", fill:"white"  }} />,
        "Legendary Chest Armor": <ChestIcon style={{ width: "2em", height: "2em", display: "block", fill:"white"}}/>,
        "Legendary Leg Armor": <BootsIcon style={{ width: "2em", height: "2em", display: "block", fill:"white"}} />,
        "Legendary Hunter Cloak": <ClassItemIcon style={{ width: "2em", height: "2em", display: "block", fill:"white"}}/>,
        "Legendary Warlock Bond": <ClassItemIcon style={{ width: "2em", height: "2em", display: "block", fill:"white"}}/>,
        "Legendary Titan Mark": <ClassItemIcon style={{ width: "2em", height: "2em", display: "block", fill:"white"}}/>,
    };

    const statIcons = {
        "Mobility": <MobilityIcon style={{ width: "2em", height: "2em", fill:"white" }} />,
        "Resilience": <ResilienceIcon style={{ width: "2em", height: "2em", fill:"white"}} />,
        "Recovery": <RecoveryIcon style={{ width: "2em", height: "2em", fill:"white"}} />,
        "Discipline": <DisciplineIcon style={{ width: "2em", height: "2em", fill:"white"}} />,
        "Intellect": <IntellectIcon style={{ width: "2em", height: "2em", fill:"white"}} />,
        "Strength": <StrengthIcon style={{ width: "2em", height: "2em", fill:"white"}} />

    }
    
    
    

    
    

    const modalIndex = {zIndex: 100};

    return (
        <div className="h-full">
            <div className="flex justify-center h-full p-4">
                <div className="hover:outline hover:outline-white w-full max-w-4xl bg-ui-grey rounded-lg border border-gray-700 shadow-xl cursor-pointer" onClick={() => setOpen(true)}>
                    <div className="flex">
                        {/* Left Panel */}
                        <div className="flex-1 text-center p-4 border-r border-gray-700">
                            <div className=" border-b p-2 rounded-tl-lg">
                                <h2 className="text-md sm:text-lg font-bold text-white flex items-center">
                                    {armorIcons[data.type]} 
                                    <span className="ml-2">{data.type.replace("Legendary", "")}</span>
                                </h2>
                            </div>
                            <img className="mx-auto border-2 w-20 my-4" alt="armor icon" src={data.icon} />
                            <h3 className="text-xl sm:text-2xl font-bold text-gray-100 underline-offset-4">{data.name}</h3>
                            <blockquote className="mt-2 p-4 flex text-left h-full italic font-semibold text-gray-300  rounded-md">
                                <p className="whitespace-pre-line">{data.lore}</p>
                            </blockquote>
                        </div>

                        {/* Right Panel */}
                        <div className="flex-1 p-4 ">
                            {Object.keys(data.statRolls).splice(1).map((key, index) => (
                                <div className="flex my-2 items-center" key={index}>
                                    <div className=" text-sm md:text-base text-left font-bold text-gray-200">
                                        {statIcons[statNames[index]]}
                                    </div>
                                    <div className="flex-1 bg-gray-600 h-6 ml-4 relative">
                                        <div className="bg-white h-6" style={{ width: `${((data.statRolls[key] / 40) * 100) + 2}%` }}></div>
                                        <div className="absolute inset-0 flex items-center justify-end pr-2">
                                            <span className="text-sm md:text-base text-gray-200 font-bold">
                                                {data.statRolls[key]}
                                            </span>
                                        </div>
                                    </div>
                                </div>
                            ))}
                            <div className="flex items-center mt-4 pt-4 border-t border-gray-600">
                                <div className="w-1/3 pl-2 text-base text-left font-bold text-gray-200">Total</div>
                                <div className="flex-1 mx-2"></div>
                                <div className="w-1/3 text-right pr-2 text-lg font-bold text-gray-200">{data.statRolls[0]}</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            {isOpen && (
                <div className="fixed inset-0" style={modalIndex}>
                    <LegendaryArmorDetailed data={data} isOpen={isOpen} setOpen={setOpen} onClose={() => setOpen(false)} />
                </div>
            )}
        </div>
                
    );
}
        