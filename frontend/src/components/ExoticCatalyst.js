import React, { useState } from "react";
import CatalystPerk from "./CatalystPerk";


export default function ExoticCatalyst(props) {
    const {data} = props;

    return (
        <div className="h-full">
            <div className="flex justify-center h-full p-4">
                <div className="w-full z-1 max-w-xs sm:max-w-md bg-ui-grey rounded-lg border border-gray-700 shadow-xl cursor-pointer">
                    <div className="bg-yellow-500 p-2  b rounded-t-lg">
                        <h2 className="text-md pt-2 sm:text-lg font-bold text-center">Exotic Catalyst</h2>
                        
                    </div>
                    <div className="mt-1">  
                        <h3 className="text-xl sm:text-2xl font-bold text-gray-100 text-center underline-offset-4">{data.name}</h3>
                        <p className="text-md sm:text-md text-gray-100 text-center">Exotic Masterwork</p>
                    </div>
                    <div className="p-4">    
                        <img className="object-center mx-auto border-2 w-20 my-2" alt="catalyst icon" src={data.icon} />
                        <h3 className="text-lg sm:text-xl font-bold text-gray-100 text-start underline-offset-4 py-2">Catalyst Effects</h3>
                        <hr/>
                        <div className="exotic-perk pr-2 mx-2 my-2">

                       
                            <div className="flex flex-col gap-4 ">
                                {data["catalyst perks"].map((perk, index) => (
                                    <div className="flex items-start gap-4 " key={index}>
                                        <img className="w-14 h-auto align-middle object-fill sm:border p-1 rounded-full" alt="exotic perk" src={perk.icon} />
                                        <div>
                                            <p className="text-lg  text-left font-semibold text-yellow-300">{perk.name}</p>
                                            <p className="text-sm  text-left text-gray-300 tracking-tight">{perk.description}</p>
                                        </div>
                                    </div>
                                ))}
                            </div>

                    </div>

                    </div>
                </div>
            </div>

            
        </div>
    );
}