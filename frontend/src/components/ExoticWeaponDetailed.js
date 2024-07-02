import React, { useState, useRef } from "react";
import Sheet from 'react-modal-sheet';
import SinglePerk from "./SinglePerk"

import Accordion from "./Accordion"

export default function ExoticWeaponDetailed(props) {
    const { data, isOpen, setOpen } = props;
    

    

    const containerRef = useRef(null);

    return (
        <div>
            <Sheet isOpen={isOpen} snapPoints={[1.0, 0]}
                initialSnap={0} detent="full-height"
                onClose={() => setOpen(false)} ref={containerRef}  onTap={(e) => e.stopPropagation()} isDismissable={true}>
                <Sheet.Container>
                    <Sheet.Header onClose={() => setOpen(false)} onTap={() => setOpen(false)} isDismissable={true} />
                    <Sheet.Content className="relative bg-[rgba(51,52,57,0.9)]" onClose={() => setOpen(false)}  isDismissable={true}>
                        {/* background image */}
                        <img className="absolute inset-0 w-full h-auto object-cover" src={data.backgroundImage} alt="exotic perk" />

                        {/* Hide on small screens */}
                        <div className="hidden lg:grid sm:grid-cols-2 gap-4 overflow-y-auto h-full p-4 z-10" style={{ backgroundImage: `linear-gradient(to right, rgba(0, 0, 0, 0.85) 50%, transparent)` }}>

                            <div className="lg:col-span-1 p-4 space-y-4">
                                
                                <div className="info">
                                    <div className="flex items-center mb-2">
                                        <img className="mr-3 sm:mt-1 w-16 lg:w-20 rounded " alt="weapon icon" src={data.icon} />
                                        <div>
                                            <div className="flex items-center">
                                                <img className="mr-1 lg:w-9 w-5 rounded" alt="damage type icon" src={data.damageTypeIcon} />
                                                <h4 className="lg:text-5xl text-2xl sm:mb-1 font-semibold text-left text-white">{data.name}</h4>
                                            </div>

                                            <div className="border-b  border-gray-400 "></div>
                                            <h5 className="sm:text-xl lg:text-2xl text-lg text-left  text-white">{data.legendWeaponDamageType}{" // "}{data.type.replace("Exotic", "")}</h5>
                                        </div>
                                    </div>

                                    <div>
                                        <blockquote className="mt-4 p-4 flex h-auto italic font-semibold text-gray-300 text-pretty rounded-md">
                                            <p className="whitespace-pre-line">{data.lore}</p>
                                        </blockquote>
                                    </div>
                                </div>

                                {/*Weapon perks section*/}
                                <div className="perks">

                                    <div className="exotic-perk ">

                                        <span className="text-white font-semibold text-md text-nowrap pt-4">{data.name}{' // '}Intrinsic<hr /></span>
                                        <div className="flex py-2 items-start">
                                            {data.weaponPerks.slice(0, 1).map((perk, index) => (
                                                <div className="flex items-start gap-3" key={index}>
                                                    <img className="w-14 lg:w-12 2xl:w-20 h-auto pt-1 self.start" alt="exotic perk" src={perk.perkIcon} />
                                                    <div>
                                                        <p className="font-semibold text-md lg:text-lg text-left text-yellow-300">{perk.name}</p>
                                                        <p className="text-sm lg:text-md text-left max-h-32 overflow-y-auto text-white">{perk.description}</p>
                                                    </div>
                                                </div>
                                            ))}
                                        </div>

                                    </div>

                                    <div className="flex flex-col py-2 mt-2">
                                        <span className="text-white font-semibold text-md text-nowrap pt-2">{data.name}{' // '}Basic<hr /></span>
                                        <div className="mt-1 perks grid-background space-y-2">
                                            {data.weaponPerks.slice(1).map((perk) => (
                                                <div>
                                                    <SinglePerk perk={perk} />
                                                </div>
                                                
                                            ))}
                                        </div>
                                            
                                    </div>
                                </div>
                                


                            </div>

                            <div className="sm:col-span-1 p-8 ">
                                <div className="flex justify-center items-center" >



                                    <Accordion
                                        className=""
                                        accordionTitle={`${data.name} Lore Entry`}
                                        title={data.name}
                                        content={data.ExtLore}
                                    />



                                    <p className="absolute mr-1 bottom-0 z-0 font-mono font-semibold lining-nums slashed-zero text-sm right-0 p-4 text-gray-800 hover:text-gray-500">
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
                                        <p className="text-white text-sm font-semibold text-left">{data.legendWeaponDamageType}{" // "}{data.type.replace("Exotic", "")}</p>
                                    </div>
                                    
                                </div>
                                
                            </div>

                            
                            <div className="z-10">
                                <div>
                                    <blockquote className="p-4 flex h-auto italic font-semibold text-white rounded-md">
                                        <p className="whitespace-pre-line">{data.lore}</p>
                                    </blockquote>
                                </div>
                                <div className="exotic-perk py-2">

                                    <span className="text-white font-semibold text-md text-nowrap pt-4">Perks{' // '}Intrinsic<hr /></span>
                                    <div className="flex py-2 items-start">
                                        {data.weaponPerks.slice(0, 1).map((perk, index) => (
                                            <div className="flex items-start gap-3" key={index}>
                                                <img className="w-14 lg:w-12 2xl:w-16 h-auto pt-1 self.start" alt="exotic perk" src={perk.perkIcon} />
                                                <div>
                                                    <p className="font-semibold text-md lg:text-lg text-left text-yellow-300">{perk.name}</p>
                                                    <p className="text-sm lg:text-md text-left max-h-32 overflow-y-auto text-white">{perk.description}</p>
                                                </div>
                                            </div>
                                        ))}
                                    </div>
                                </div>

                                <div className="flex flex-col py-2 mt-2">
                                    <span className="text-white font-semibold text-md text-nowrap pt-2">Perks{' // '}Basic<hr /></span>
                                    <table className="table-auto w-full">
                                        <thead>
                                            <tr className=" text-white">
                                                <th className="px-4"></th>
                                                <th className="px-4"></th>

                                            </tr>
                                        </thead>
                                        <tbody>
                                            {data.weaponPerks.slice(1).map((perk, index) => (
                                                <tr className="border-b border-gray-700" key={index}>
                                                    <td className="p-2">
                                                        <img className="w-14 lg:w-12 2xl:w-16 h-auto align-middle" alt="perk" src={perk.perkIcon} />
                                                    </td>
                                                    <td className="px-1 py-2">
                                                        <p className="font-semibold text-md lg:text-md text-left text-white">{perk.name}</p>
                                                        <div className="text-xs lg:text-sm text-left text-gray-100 max-h-32 overflow-y-auto">
                                                            {perk.description}
                                                        </div>
                                                    </td>

                                                </tr>
                                            ))}
                                        </tbody>
                                    </table>
                                </div>

                                <div className="flex justify-center items-center py-10" >



                                    <Accordion
                                        className=""
                                        accordionTitle={`${data.name} Lore Entry`}
                                        title={data.name}
                                        content={data.ExtLore}
                                    />



                                    
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
