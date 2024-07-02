import React, { useState } from 'react';

export default function DoublePerk(props) {
  const { perk1, perk2 } = props;
  const [activePerk, setActivePerk] = useState(perk1);

  //swaps perk
  const swapPerk=() => {

    //set the new active perk
    setActivePerk(activePerk === perk1 ? perk2 : perk1);
  };

  
  const setBackground = (perk) => {
    const classText = "w-14 4xl:w-16 object-cover border-2 p-1 rounded-full transition-colors duration-300";
    
    //figure out which perk is active
    if((activePerk === perk1 && perk === perk1) || (activePerk === perk2 && perk === perk2)) {
      return `${classText} bg-blue-500 `;
    }
    return `${classText} hover:outline cursor-pointer`;

  };

  return (
    <div className="flex w-full h-20 items-center justify-between ">
      {/* perk 1 */}
      <div className="flex-shrink-0 pr-2" onClick={swapPerk}>
        <img className={setBackground(perk1)} alt="perk 1 icon" src={perk1.perkIcon} />
      </div>

      {/* perk 2*/}
      <div className="flex-shrink-0 px-2 mx-2" onClick={swapPerk}>
        <img className={setBackground(perk2)} alt="perk 2 icon" src={perk2.perkIcon} />
      </div>

      {/* Perk Details */}
      <div className="flex-grow pl-2 mt-2">
        <p className="text-lg font-semibold text-white">{activePerk.name}</p>
        <p className="text-sm  text-gray-300 tracking-tight">{activePerk.description}</p>
      </div>
    </div>
  );
}
