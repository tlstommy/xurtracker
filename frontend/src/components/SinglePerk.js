import React, { useState } from 'react';

export default function SinglePerk(props) {
  const {perk,isOrigin} = props;
  
  return (
    <div className="flex w-full max-h-20 items-center justify-between  ">
      {/* perk 1 */}
      <div className="flex-shrink-0  pr-4 py-2">
        <img className="w-14 4xl:w-16 object-cover border-2 p-1 rounded-full transition-colors duration-300 bg-blue-500" alt="perk icon" src={perk.perkIcon} />
      </div>

      

      {/* Perk Details */}
      <div className="flex-grow pl-3">
        <p className="text-lg  font-semibold text-white">{perk.name}{isOrigin ? <small className="origin-perk-label text-sm text-gray-300">  - Origin Trait</small>: ""}</p>
        <p className="text-sm  text-gray-300 tracking-tight">{perk.description}</p>
      </div>
    </div>
  );
}