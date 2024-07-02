import React, { useState } from "react";
import ExoticWeaponDetailed from "./ExoticWeaponDetailed";
import Perk from "./Perk";

import {ReactComponent as PrimaryAmmoIcon} from "../assets/icons/ammo-primary.svg";
import {ReactComponent as SpecialAmmoIcon} from "../assets/icons/ammo-special.svg";
import {ReactComponent as HeavyAmmoIcon} from "../assets/icons/ammo-heavy.svg";


export default function ExoticWeapon(props) {
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [isOpen, setOpen] = useState(false);

    const {data} = props;

    const ammoTypeIcon = {

        1: <PrimaryAmmoIcon style={{ width: "2em", height: "2em"}} />,
        2: <SpecialAmmoIcon style={{ width: "2em", height: "2em"}} />,
        3: <HeavyAmmoIcon style={{ width: "2em", height: "2em"}} />

    }

    

    const openModal = () => setIsModalOpen(true);
    const closeModal = () => setIsModalOpen(false);

    const modalIndex = {zIndex: 100};

    return (
        <div className="h-full">
            <div className="flex justify-center h-full p-4">
                <div className="hover:outline hover:outline-white w-full z-1 max-w-xs sm:max-w-md bg-ui-grey rounded-lg border border-gray-700 shadow-xl cursor-pointer" onClick={() => setOpen(true)}>
                    <div className="bg-yellow-500 p-2 rounded-t-lg">
                        <h2 className="text-md sm:text-lg font-bold flex items-center justify-center">
                            {ammoTypeIcon[data.ammoType]}
                            &nbsp;
                            <img className="weapon-damage-icon mr-2" alt="weapon damage type icon" src={data.damageTypeIcon}/>
                        </h2>
                    </div>

                    <div className="mt-1">  
                        <h3 className="text-xl sm:text-2xl font-bold text-gray-100 text-center underline-offset-4">{data.name}</h3>
                        <p className="text-md sm:text-md text-gray-100 text-center">{data.legendWeaponDamageType} {'//'} {data.type.replace("Exotic", "")}</p>
                    </div>
                    <div className="p-4">    
                        <img className="object-center w-20 border-2 mx-auto my-2" alt="weapon icon" src={data.icon} />
                        
                        
                        <h3 className="text-lg sm:text-xl font-bold text-gray-100 text-start underline-offset-4 py-2">Weapon Perks</h3>
                        <hr/>
                        <div class="grid grid-cols-5 gap-1 py-1 grid-background">
                            {data.weaponPerks.map((perk,index) => (
                                <div className='group relative p-0 sm:p-1' key={perk.hashID}>
                                    <Perk 
                                        image={perk.perkIcon}
                                        name={perk.name}
                                        type={perk.perkType}
                                        subtype={perk.perkSubType}
                                        description={perk.description}
                                        index={index}
                                    />
                                </div>
                            ))}

                        </div>
                    </div>
                </div>
            </div>

            {isOpen && (
                <div className="fixed inset-0" style={modalIndex}>
                    <ExoticWeaponDetailed data={data} isOpen={isOpen} setOpen={setOpen} onClose={() => setOpen(false)}/>
                </div>
            )}
        </div>
    );
}
