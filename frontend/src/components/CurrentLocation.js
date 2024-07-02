import React from "react";

export default function CurrentLocation(){
    return(
        
      <div class="relative flex flex-col mt-6 text-gray-700 bg-white shadow-md bg-clip-border rounded-xl w-96">
        <div class="border-b p-4">
          <h5 class="text-lg font-semibold">Xûr's Current Location</h5>
        </div>
        <div class="p-6">
          <h2 class="text-2xl font-bold">Winding Cove</h2>
          <h6 class="text-base font-medium">European Dead Zone, Earth</h6>
          
          <p>Xûr will be in the Winding Cove until weekly reset.</p>
        </div>
        <div class="p-6 pt-0">
          <button
            class="align-middle select-none font-sans font-bold text-center uppercase transition-all disabled:opacity-50 disabled:shadow-none disabled:pointer-events-none text-xs py-3 px-6 rounded-lg bg-gray-900 text-white shadow-md shadow-gray-900/10 hover:shadow-lg hover:shadow-gray-900/20 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none"
            type="button">
            button
          </button>
        </div>
      </div>
        
    );
}