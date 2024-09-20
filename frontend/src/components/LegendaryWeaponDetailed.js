import React, { useState, useRef } from "react";
import Sheet from 'react-modal-sheet';

import DoublePerk from "./DoublePerk";
import SinglePerk from "./SinglePerk"
import FramePerk from "./FramePerk";
import Masterwork from "./Masterwork";

import Accordion from "./Accordion"

export default function LegendaryWeaponDetailed(props) {
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
                        <img className="absolute inset-0 w-full h-auto object-cover z-0" src={data.backgroundImage} alt="weapon" />

                        {/* Hide on small screens */}
                        <div className="hidden lg:grid sm:grid-cols-2 gap-4 overflow-y-auto h-full pl-4 z-10 " style={{ backgroundImage: `linear-gradient(to right, rgba(0, 0, 0, 0.85) 50%, transparent)` }}>

                            <div className="lg:col-span-1 p-4 space-y-4">
                                
                                <div className="info space-y-4">
                                    <div className="flex items-center mb-2">
                                        <img className="mr-3 sm:mt-1 w-16 lg:w-20 rounded " alt="weapon icon" src={data.icon} />
                                        <div>
                                            <div className="flex items-center">
                                                <img className="mr-1 lg:w-9 w-5 rounded" alt="damage type icon" src={data.damageTypeIcon} />
                                                <h4 className="lg:text-5xl text-2xl sm:mb-1 font-semibold text-left text-white">{data.name}</h4>
                                            </div>

                                            <div className="border-b  border-gray-400 "></div>
                                            <h5 className="sm:text-xl lg:text-2xl text-lg text-left  text-white">{data.legendWeaponDamageType}{" // "}{data.type.replace("Legendary", "")}</h5>
                                        </div>
                                    </div>

                                    <div>
                                        <blockquote className="p-4 flex h-auto italic font-semibold text-pretty text-gray-300  rounded-md">
                                            <p className="whitespace-pre-line">{data.lore}</p>
                                        </blockquote>
                                    </div>
                                </div>

                                <div class="weapon-frame flex flex-col flex-grow space-y-4 mt-2 text-white pl-4">
                                    <div class="flex flex-col sm:flex-row justify-evenly space-y-4 sm:space-y-0 sm:space-x-4">
                                        
                                        <div class="flex items-center space-x-2">
                                            <FramePerk name={data.legendWeaponFrame.name} image={data.legendWeaponFrame.icon} description={data.legendWeaponFrame.description} imageSize={"4rem"}/>
                                            <h4 class="text-lg font-semibold text-left text-white">
                                                {data.legendWeaponFrame.name}
                                            </h4>
                                        </div>
                                        
                                        <div class="flex items-center space-x-2">
                                            <Masterwork name={data.masterworkData.name} image={data.masterworkData.icon} description={data.masterworkData.description} imageSize={"3.5rem"}/>
                                            <h4 class="text-lg font-semibold text-left text-white">
                                                {data.masterworkData.name}
                                            </h4>
                                        </div>
                                    </div>
                                </div>



                                {/*Weapon perks section*/}

                                <div className="perks-sect mb-10">

                                    <div className="weapon-perks flex flex-col space-y mt-2 text-white">
                                        <h3 className="font-semibold text-xl text-white py-2">{data.name}{' // '}Perks</h3>
                                        <hr />
                                        
                                        <div className="mt-1 perks grid-background flex flex-col space-y-2">
                                            <div>
                                                <DoublePerk perk1={data.weaponPerks[0]} perk2={data.weaponPerks[1]} />
                                            </div>
                                            <div>
                                                <DoublePerk perk1={data.weaponPerks[2]} perk2={data.weaponPerks[3]} />
                                            </div>
                                            {data.weaponPerks.slice(4).map((perk, index) => (
                                                <div className="mt-2">
                                                    <SinglePerk perk={perk} />
                                                </div>
                                                
                                            ))}
                                            {data.originTrait ? (
                                                <div className="mt-2">
                                                    <SinglePerk perk={data.originTrait} isOrigin={true} />
                                                </div>
                                            ) : null}
                                    
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

                                <div class="weapon-frame flex flex-col flex-grow space-y-4 mt-2 text-white pl-4">
                                    <div class="space-y-4 ">
                                        
                                        <div class="flex flex-col">
                                                
                                                <FramePerk name={data.legendWeaponFrame.name} image={data.legendWeaponFrame.icon} description={data.legendWeaponFrame.description} imageSize={"4rem"}/>
                                            
                                                <h4 class="text-lg font-semibold text-left text-white">
                                                    {data.legendWeaponFrame.name}
                                                </h4>
                                                
                                           
                                        </div>
                                        
                                        <div class="">
                                            <Masterwork name={data.masterworkData.name} image={data.masterworkData.icon} description={data.masterworkData.description} imageSize={"3.5rem"}/>
                                            <h4 class="text-lg font-semibold text-left text-white">
                                                {data.masterworkData.name}
                                            </h4>
                                        </div>
                                    </div>
                                </div>
                               

                                <div className="weapon-perks flex flex-col mt-2 text-white">
                                    <span className="text-white font-semibold text-md text-nowrap pt-2">Perks{' // '}Basic<hr /></span>
                                    <div className="mt-1 perks grid-background flex flex-col space-y-4">
                                        <div>
                                            <DoublePerk perk1={data.weaponPerks[0]} perk2={data.weaponPerks[1]} />
                                        </div>
                                        <div>
                                            <DoublePerk perk1={data.weaponPerks[2]} perk2={data.weaponPerks[3]} />
                                        </div>
                                        {data.weaponPerks.slice(4).map((perk, index) => (
                                            <div className="mt-2">
                                                <SinglePerk perk={perk} />
                                            </div>
                                            
                                        ))}
                                        {data.originTrait ? (
                                            <div className="mt-2">
                                                <SinglePerk perk={data.originTrait} isOrigin={true} />
                                            </div>
                                        ) : null}
                                    
                                    </div>
                                    
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