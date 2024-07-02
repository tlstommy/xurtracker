import React, { useState } from "react";

import ExoticArmorDetailed from "./ExoticArmorDetailed";

import {ReactComponent as WarlockIcon} from "../assets/icons/warlock.svg";
import {ReactComponent as HunterIcon} from "../assets/icons/hunter.svg";
import {ReactComponent as TitanIcon} from "../assets/icons/titan.svg";

import {ReactComponent as MobilityIcon} from "../assets/icons/mobility.svg";
import {ReactComponent as ResilienceIcon} from "../assets/icons/resilience.svg";
import {ReactComponent as RecoveryIcon} from "../assets/icons/recovery.svg";
import {ReactComponent as DisciplineIcon} from "../assets/icons/discipline.svg";
import {ReactComponent as IntellectIcon} from "../assets/icons/intellect.svg";
import {ReactComponent as StrengthIcon} from "../assets/icons/strength.svg";



export default function ExoticArmor(props) {
    const [isOpen, setOpen] = useState(false);


    const {data,classKey} = props;

    const statNames = ["Mobility","Resilience","Recovery","Discipline","Intellect","Strength"]
    
    
    const classIcons = {
        0: <HunterIcon style={{ width: "2em", height: "2em", display: "block", margin: "auto", fill: "white" }} />,
        1: <WarlockIcon style={{ width: "2em", height: "2em", display: "block", margin: "auto", fill: "white" }} />,
        2: <TitanIcon style={{ width: "2em", height: "2em", display: "block", margin: "auto", fill: "white" }}/>
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
                <div className="hover:outline hover:outline-white w-full z-10 max-w-xs sm:max-w-md bg-ui-grey rounded-lg border border-gray-700 shadow-xl cursor-pointer" onClick={() => setOpen(true)}>
                    <div className="bg-yellow-500 p-2 b rounded-t-lg">
                        <h2 className="text-md sm:text-lg font-bold text-center">{classIcons[classKey]}</h2>
                    </div>
                    <div className="mt-1">  
                        <h3 className="text-xl sm:text-2xl font-bold text-gray-100 text-center underline-offset-4">{data.name}</h3>
                        <p className="text-md sm:text-md text-gray-100 text-center">{data.type.replace("Exotic", "")}</p>
                    </div>
                    <div className="pt-4">    
                        
                        <div className="flex justify-center">
                            <img className="border-2 mx-auto w-20 my-2" alt="armor icon" src={data.icon} />
                            
                        </div>
                        
                        
                        
                        <div className="armor-stats px-4 py-4 rounded-lg m-4 ">
                            {Object.keys(data.statRolls).splice(1).map((key) => (
                                <div className="flex my-2 items-center " key={key}>
                                    <div className=" text-sm md:text-base text-left font-bold text-gray-200 pr-2">
                                        {statIcons[statNames[key - 1]]}
                                    </div>
                                    <div className="flex-1 bg-gray-600 h-6 ml-4 relative">
                                        <div className="bg-white h-6 " style={{ width: `${((data.statRolls[key] / 40) * 100) + 2}%` }}></div>
                                        <div className="absolute inset-0 flex items-center justify-end pr-2">
                                            <span className="text-sm md:text-base text-gray-200 font-bold">
                                                {data.statRolls[key]}
                                            </span>
                                        </div>
                                    </div>
                                </div>
                            ))}

                            {/* statroll total */}
                            {Object.keys(data.statRolls).splice(0,1).map((key) => (
                                <div className="flex items-center mt-4 pt-4 border-t border-gray-600" key={key}>
                                    <div className="w-1/4 pl-2 text-base text-left font-bold text-gray-200">Total</div>
                                    <div className="flex-1 mx-2"></div>
                                    <div className="w-1/4 text-right pr-2 text-lg font-bold text-gray-200">{data.statRolls[key]}</div>
                                </div>
                            ))}
                        </div>
                    </div>

                    <div className="exotic-perk px-4 pt-2 mx-2 my-2 ">

                       
                        <div className="flex py-2 items-start ">
                            {data.exoticArmorPerk.slice(0, 1).map((perk, index) => (
                                <div className="flex items-start gap-4 " key={index}>
                                    <img className="w-16 h-auto align-middle rounded-full" alt="exotic perk" src={perk.icon} />
                                    <div>
                                        <p className=" font-semibold text-lg text-yellow-300">{perk.name}</p>
                                        <p className="text-left  text-white mt-1 tracking-tight">{perk.desc.split('.')[0]+"."}</p>
                                    </div>
                                </div>
                            ))}
                        </div>

                    </div>

                    
                    
                </div>
            </div>

            {isOpen && (
                <div className="fixed inset-0" style={modalIndex}>
                    <ExoticArmorDetailed data={data} classKey={classKey} isOpen={isOpen} setOpen={setOpen} onClose={() => setOpen(false)}/>
                </div>
            )}
        </div>
    );
}
