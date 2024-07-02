import React, { useState } from "react";
import { ReactComponent as ChevronUp } from "../assets/icons/chevron-double-up.svg";
import { ReactComponent as ChevronDown } from "../assets/icons/chevron-double-down.svg";

export default function Item(props) {
    const strangeCoinIcon = "https://www.bungie.net/common/destiny2_content/icons/1fa5806bb6ec16b5f8cdeb4b36d4bb01.jpg";
    const { data } = props;

    const [showTooltip, setShowTooltip] = useState(false);

    return (
        <div className="flex items-center p-2 bg-ui-grey rounded-md">
            <div className="relative mr-4">
                <img className="w-16 border-2 mx-auto" alt="item icon" src={data.icon} />
                <div className="absolute right-0 bottom-0 bg-white px-1 text-sm font-semibold">
                    {data.count}
                </div>
            </div>

            <div className="flex-grow flex flex-col justify-between">
                <h2 className="text-md sm:text-lg font-bold text-white">
                    {data.name}
                </h2>
                <div className="flex justify-between font-semibold items-end mt-1 w-full">
                    <div className="flex items-center">
                        <img className="w-5 h-5" alt="strange coin icon" src={strangeCoinIcon} />
                        <span className="text-white text-sm ml-2">x{data.cost}</span>
                    </div>
                    <div className="relative hover:font-bold">
                        <span onMouseOver={() => setShowTooltip(true)} onMouseOut={() => setShowTooltip(false)} className="text-white text-sm flex items-center">
                            {data["is lowest"] ? (
                                <>
                                    <span className="text-xs font-semibold text-gray-300">Best Price &nbsp;</span> 
                                    <ChevronUp style={{ color: "green", width: "1.5em", height: "1.5em" }} />
                                </>
                            ) : (
                                <>
                                    <span className="text-xs font-semibold text-gray-300">Sold for Less &nbsp;</span> 
                                    <ChevronDown style={{ color: "red", width: "1.5em", height: "1.5em" }} />
                                </>
                                
                            )}
                        </span>
                        {showTooltip && (
                            <div className="absolute w-max right-0 bg-black text-white p-2 text-xs rounded-md shadow-lg">
                                {data["is lowest"] ? "Best price." : `Has sold for lower: ${data["lowest price"]}`}
                            </div>
                        )}
                    </div>
                </div>
            </div>
        </div>
    );
}
