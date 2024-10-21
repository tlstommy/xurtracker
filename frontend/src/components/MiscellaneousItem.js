import React, { useState } from "react";
//misc items like xurfboard
import MiscellaneousItemDetailed from "./MiscellaneousItemDetailed";


export default function MiscellaneousItem(props) {
    const [isOpen, setOpen] = useState(false);


    const {data} = props;

   

    const modalIndex = {zIndex: 100};

    return (
        <div className="h-full">
            
            <div className="flex justify-center h-full p-4">
                <div className="hover:outline hover:outline-white w-full z-10 max-w-xs sm:max-w-md bg-ui-grey rounded-lg border border-gray-700 shadow-xl cursor-pointer" onClick={() => setOpen(true)}>
                    <div className="bg-yellow-500 p-2 b rounded-t-lg">
                        <h2 className="text-md sm:text-lg font-bold text-center">{data.type}</h2>
                    </div>
                    <div className="mt-1">  
                        <h3 className="text-xl sm:text-2xl font-bold text-gray-100 text-center underline-offset-4">{data.name}</h3>
                    </div>
                    <div className="pt-4">    
                        
                        <div className="flex justify-center">
                            <img className="border-2 mx-auto w-20 my-2" alt="item icon" src={data.icon} />
                        </div>
                        
                        
                    
                    </div>

                    <div className="desc px-4 pt-2 mx-2 my-2 ">

                       
                        <blockquote className="mt-2 p-4 flex text-left h-full italic font-semibold text-gray-300  rounded-md">
                            <p className="whitespace-pre-line">{data.description}</p>
                        </blockquote>

                    </div>

                    
                    
                </div>
            </div>

            {isOpen && (
                <div className="fixed inset-0" style={modalIndex}>
                    <MiscellaneousItemDetailed data={data} isOpen={isOpen} setOpen={setOpen} onClose={() => setOpen(false)}/>
                </div>
            )}
        </div>
    );
}
