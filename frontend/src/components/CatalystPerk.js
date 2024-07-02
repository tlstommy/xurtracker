import React, { useState } from 'react';

export default function CatalystPerk(props) {
  const {perk,isOrigin} = props;
  
  return (
    <div className="grid grid-cols-[auto_1fr] gap-3 relative flex items-start">
      {/* perk 1 */}
      <div className="">
        <img className="w-14 4xl:w-16 object-fill sm:border p-1 rounded-full" alt="perk icon" src={perk.icon} />
      </div>

      

      {/* Perk Details */}
      <div className="flex-grow pl-3 mt-2">
        <p className="text-lg  font-semibold text-white">{perk.name}</p>
        <p className="text-sm  text-left text-gray-300 tracking-tight">{perk.description}</p>
      </div>
    </div>
  );
}