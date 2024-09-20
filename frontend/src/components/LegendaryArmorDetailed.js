import React, { useState, useRef, useEffect } from "react";
import Sheet from 'react-modal-sheet';

import Accordion from "./Accordion"


import {ReactComponent as MobilityIcon} from "../assets/icons/mobility.svg";
import {ReactComponent as ResilienceIcon} from "../assets/icons/resilience.svg";
import {ReactComponent as RecoveryIcon} from "../assets/icons/recovery.svg";
import {ReactComponent as DisciplineIcon} from "../assets/icons/discipline.svg";
import {ReactComponent as IntellectIcon} from "../assets/icons/intellect.svg";
import {ReactComponent as StrengthIcon} from "../assets/icons/strength.svg";



export default function LegendaryArmorDetailed(props) {
    const { data, classType, closeModal, isOpen, setOpen } = props;

    

    const statNames = ["Mobility", "Resilience", "Recovery", "Discipline", "Intellect", "Strength"]

    const statIcons = {
        "Mobility": <MobilityIcon style={{ width: "2em", height: "2em", fill:"white" }} />,
        "Resilience": <ResilienceIcon style={{ width: "2em", height: "2em", fill:"white"}} />,
        "Recovery": <RecoveryIcon style={{ width: "2em", height: "2em", fill:"white"}} />,
        "Discipline": <DisciplineIcon style={{ width: "2em", height: "2em", fill:"white"}} />,
        "Intellect": <IntellectIcon style={{ width: "2em", height: "2em", fill:"white"}} />,
        "Strength": <StrengthIcon style={{ width: "2em", height: "2em", fill:"white"}} />

    }

    const statTotal = data.statRolls[0]

    const containerRef = useRef(null);

    


    return (
        <div>
            <Sheet isOpen={isOpen} snapPoints={[1.0, 0]}
                initialSnap={0} detent="full-height"
                onClose={() => setOpen(false)} onTap={(e) => e.stopPropagation()} ref={containerRef} isDismissable={true}>
                <Sheet.Container>
                    <Sheet.Header onClose={() => setOpen(false)} onTap={() => setOpen(false)} isDismissable={true} />
                    <Sheet.Content className="relative bg-[rgba(51,52,57,0.9)]" onClose={() => setOpen(false)}  isDismissable={true}>
                        {/* background image */}

                        <img className="absolute inset-0 w-full h-auto object-cover z-0" src={data.backgroundImage} alt="exotic perk" />
                        
                        {/* Hide on small screens */}
                        <div className="hidden lg:grid sm:grid-cols-2 gap-4 overflow-y-auto h-full p-4 z-10" style={{ backgroundImage: `linear-gradient(to right, rgba(0, 0, 0, 0.85) 50%, transparent)` }}>

                            <div className="lg:col-span-1 p-4 space-y-4">

                                <div className="info">
                                    <div className="flex items-center mb-2">
                                        <img className="mr-3 sm:mt-1 w-16 lg:w-20 rounded " alt="weapon icon" src={data.icon} />
                                        <div>
                                            <div className="flex items-center">

                                                <h4 className="lg:text-5xl text-2xl sm:mb-1 font-semibold text-left text-white">{data.name}</h4>
                                            </div>

                                            <div className="border-b  border-gray-400 "></div>
                                            <h5 className="sm:text-xl lg:text-2xl text-lg text-left  text-white">Legendary{" // "}{data.type.replace("Legendary", "")}</h5>
                                        </div>
                                    </div>

                                    <div>
                                        <blockquote className="mt-4 p-4 flex h-auto italic font-semibold text-gray-300  rounded-md">
                                            <p className="whitespace-pre-line">{data.lore}</p>
                                        </blockquote>
                                    </div>
                                </div>

                                {/*Armor perks section*/}
                                <div className="perks">

                                    

                                    <div className="armor-stats flex flex-col py-2 mt-2">
                                        <span className="text-white font-semibold text-md text-nowrap pt-2">{data.name}{' // '}Stats<hr /></span>

                                        <div className="grid grid-cols-2 xl:grid-cols-3 py-2 mt-2">
                                            <div className="col-span-1 sm:col-span-2">
                                                {Object.keys(data.statRolls).splice(1).map((key) => (
                                                    <div className="flex my-2 items-center" key={key}>
                                                        <div className="w-1/4 text-sm md:text-base font-bold text-gray-200 text-white pr-2">
                                                            {statNames[key - 1]}
                                                        </div>
                                                        <div className="flex-1 bg-gray-600 h-6 mr-28 relative">
                                                            <div className="bg-white h-6" style={{ width: `${((data.statRolls[key] / 40) * 100) + 2}%` }}></div>
                                                            <div className="absolute inset-0 flex items-center justify-end pr-2">
                                                                <span className="text-sm md:text-base text-gray-200 font-bold">
                                                                    {data.statRolls[key]}
                                                                </span>
                                                            </div>
                                                        </div>
                                                    </div>
                                                ))}


                                                <div className="flex mt-4">
                                                    <span className="w-1/4 text-white text-2xl font-bold">
                                                        Total:
                                                    </span>
                                                    <span className="text-white text-2xl font-bold pl-">
                                                        {statTotal}
                                                    </span>
                                                </div>
                                            </div>
                                        </div>


                                    </div>



                                </div>
                                <div>

                                </div>


                            </div>

                            <div className="sm:col-span-1 p-8 ">
                                <div className="flex justify-center items-center" >



                                    {data.ExtLore !== null ? <Accordion
                                        className=""
                                        accordionTitle={`${data.name} Lore Entry`}
                                        title={data.name}
                                        content={data.ExtLore}
                                    /> : "" }
                                    



                                    <p className="absolute bottom-0 z-0 font-mono font-semibold lining-nums slashed-zero text-sm right-0 p-4 text-gray-800 hover:text-gray-500">
                                       {data.itemHash}
                                    </p>
                                </div>
                            </div>
                        </div>


                        {/* Hide on non mobile screens */}
                        <div className="lg:hidden grid grid-rows-[auto_1fr] gap-4 p-4 z-10 overflow-y-auto ">

                            <div className="relative w-full " style={{ paddingTop: '56.25%' }}>
                                <div className="absolute inset-0 flex flex-col justify-end pb-5">

                                    <div className="title">
                                        <p className="text-white text-2xl font-semibold text-left">{data.name}</p>
                                        <p className="text-white text-sm font-semibold text-left">Legendary{" // "}{data.type.replace("Legendary", "")}</p>
                                    </div>

                                </div>

                            </div>


                            <div className="z-10">
                                <div>
                                    <blockquote className="p-4 flex h-auto italic font-semibold text-white rounded-md">
                                        <p className="whitespace-pre-line">{data.lore}</p>
                                    </blockquote>
                                </div>
                                

                                <div className="flex flex-col py-2 mt-2">
                                    <span className="text-white font-semibold text-md text-nowrap pt-2">{data.name}{' // '}Stats<hr /></span>
                                    <div className="grid grid-cols-2 py-2  mt-2">
                                        <div className="col-span-2 md:col-span-1">
                                            {Object.keys(data.statRolls).splice(1).map((key) => (
                                                <div className="flex my-2 items-center" key={key}>
                                                    <div className="text-sm md:text-base font-bold text-gray-100 pr-2">
                                                        {statIcons[statNames[key - 1]]}
                                                    </div>
                                                    <div className="flex-1 bg-gray-600 h-6 relative">
                                                        <div className="bg-white h-6 " style={{ width: `${((data.statRolls[key] / 40) * 100)}%` }}></div>
                                                        <div className="absolute inset-0 flex items-center justify-end pr-2">
                                                            <span className="text-sm md:text-base text-gray-200 font-bold">
                                                                {data.statRolls[key]}
                                                            </span>
                                                        </div>
                                                    </div>
                                                </div>
                                            ))}

                                            <div className="flex mt-4">
                                                <span className="w-1/4 text-white text-2xl font-bold">
                                                    Total:
                                                </span>
                                                <span className="text-white text-2xl font-bold pl-">
                                                    {statTotal}
                                                </span>
                                            </div>
                                        </div>
                                        <div className="col-span-1">

                                        </div>

                                    </div>
                                </div>

                                <div className="flex justify-center items-center py-10" >



                                    {data.ExtLore !== null ? <Accordion
                                        className=""
                                        accordionTitle={`${data.name} Lore Entry`}
                                        title={data.name}
                                        content={data.ExtLore}
                                    /> : "" }




                                </div>




                            </div>
                        </div>


                    </Sheet.Content>
                </Sheet.Container>
                <Sheet.Backdrop />
            </Sheet>
        </div>
    );
}