
import React, { useState } from "react";
import { motion } from "framer-motion";


export default function ClassSelect(props){

    
    const { selectedClass, setSelectedClass } = props;

    //anim variants
    const variants = {
        hover: { scale: 1.2 },
        tap: { scale: 0.9 }
    };
    
    return (
        <div>
            <div className="row">
                <div className="col-xs-12">
                    <div className="class-select-switch">
                        <input id="class-select-switch-hunter" name="class-select-switch" type="radio" value="Hunter" className="class-select-switch-input" checked={selectedClass === "Hunter"} onChange={() => setSelectedClass("Hunter")}/>
                        <label for="class-select-switch-hunter" className="class-select-switch-label class-select-switch-label-hunter">
                            <motion.div  
                                whileHover={variants.hover}
                                whileTap={variants.tap}>
                            <svg viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">
                                <path d="m11.297 12.239 4.703-.016-4.705 7.078 4.705-.016-5.02 7.551h-4.77l4.764-7.062h-4.764l4.762-7.059h-4.762l5.083-7.534 4.707-.017zm9.406 0-4.703-7.075 4.707.017 5.083 7.534h-4.762l4.762 7.059h-4.764l4.764 7.062h-4.77l-5.02-7.551 4.705.016-4.705-7.078z"/>
                            </svg>
                            </motion.div>
                        </label>
                        
                        <input id="class-select-switch-warlock" name="class-select-switch" type="radio" value="Warlock" className="class-select-switch-input" checked={selectedClass === "Warlock"} onChange={() => setSelectedClass("Warlock")}/>
                        <label for="class-select-switch-warlock" className="class-select-switch-label class-select-switch-label-warlock">
                            <motion.div  
                                whileHover={variants.hover}
                                whileTap={variants.tap}>
                            <svg viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">
                                <path d="m5.442 23.986 7.255-11.65-2.71-4.322-9.987 15.972zm5.986 0 4.28-6.849-2.717-4.333-6.992 11.182zm7.83-11.611 7.316 11.611h5.426l-10.015-15.972zm-7.26 11.611h8.004l-4.008-6.392zm6.991-11.182-2.703 4.324 4.302 6.858h5.413zm-5.707-.459 2.71-4.331 2.71 4.331-2.703 4.326z"/>
                            </svg>
                            </motion.div>
                        </label>
                        
                        <input id="class-select-switch-titan" name="class-select-switch" type="radio" value="Titan" className="class-select-switch-input" checked={selectedClass === "Titan"} onChange={() => setSelectedClass("Titan")}/>
                        <label for="class-select-switch-titan" className="class-select-switch-label class-select-switch-label-titan">
                            <motion.div  
                                whileHover={variants.hover}
                                whileTap={variants.tap}>
                                <svg viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">
                                    <path d="m15.214 15.986-8.925-5.153v10.306zm1.572 0 8.925 5.153v-10.306zm8.109-5.629-8.856-5.193-8.896 5.17 8.896 5.136zm-.023 11.274-8.833-5.101-8.873 5.123 8.873 5.183z"/>
                                </svg>
                            </motion.div>
                        </label>
                        <span className="class-select-switch-selector"></span>
                    </div>
                </div>
            </div>
        </div>
    )
}