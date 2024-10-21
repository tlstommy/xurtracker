import React, { useState, useRef } from "react";
import Sheet from 'react-modal-sheet';


import Accordion from "./Accordion"


export default function MiscellaneousItemDetailed(props) {
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
                        <img className="absolute inset-0 w-full h-auto object-cover z-0" src={data.backgroundImage} alt="item background" />

                        {/* Hide on small screens */}
                        <div className="hidden lg:grid sm:grid-cols-2 gap-4 overflow-y-auto h-full pl-4 z-10 " style={{ backgroundImage: `linear-gradient(to right, rgba(0, 0, 0, 0.85) 50%, transparent)` }}>

                            <div className="lg:col-span-1 p-4 space-y-4">
                                
                                <div className="info space-y-4">
                                    <div className="flex items-center mb-2">
                                        <img className="mr-3 sm:mt-1 w-16 lg:w-20 rounded " alt="item icon" src={data.icon} />
                                        <div>
                                            <div className="flex items-center">
                                                <h4 className="lg:text-5xl text-2xl sm:mb-1 font-semibold text-left text-white">{data.name}</h4>
                                            </div>

                                            <div className="border-b  border-gray-400 "></div>
                                            <h5 className="sm:text-xl lg:text-2xl text-lg text-left  text-white">{data.type}</h5>
                                        </div>
                                    </div>

                                    <div>
                                        <blockquote className="p-4 flex h-auto italic font-semibold text-pretty text-gray-500  rounded-md">
                                            <p className="whitespace-pre-line">{data.description}</p>
                                        </blockquote>
                                    </div>
                                    <span className="text-white font-semibold text-md text-nowrap pt-2">{data.name}{' // '}Lore Entry<hr /></span>
                                    <div>
                                        <blockquote className="p-4 flex h-auto font-semibold accordion-scrollbar overflow-y-auto text-pretty text-white rounded-md">
                                            <p className="whitespace-pre-line">{data.lore}</p>
                                        </blockquote>
                                    </div>
                                </div>

        


                            </div>

                            <div className="sm:col-span-1 p-8 ">
                                <div className="flex justify-center items-center" >


                                    <p className="absolute bottom-0 z-0 font-mono font-semibold lining-nums slashed-zero text-sm right-0 p-4 text-gray-800 hover:text-gray-500">
                                       {data.hash}
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
                                    </div>
                                    
                                </div>
                                
                            </div>

                            
                            <div className="z-10">
                                <div>
                                    <blockquote className="p-4 flex h-auto italic font-semibold text-white rounded-md">
                                        <p className="whitespace-pre-line">{data.description}</p>
                                    </blockquote>
                                </div>

                                

                                <div className="flex justify-center items-center py-10" >



                                    <Accordion
                                        className=""
                                        accordionTitle={`${data.name} Lore Entry`}
                                        title={data.name}
                                        content={data.lore}
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
