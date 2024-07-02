import React, { useState } from 'react';


export default function WeaponMasterwork(props) {

    const { name, image, description} = props;

    const [isHovering, setIsHovering] = useState(false);
    const [mousePosition, setMousePosition] = useState({ x: 0, y: 0 });

    function handleMouseMove(e) {
        const tooltipWidth = 256;
        const screenWidth = window.outerWidth;
        let x = e.clientX;
        let y = e.clientY;

        // move tooltip over if its getting off the page on the right
        if (x + tooltipWidth + (tooltipWidth * .10) / 2 > screenWidth) {
            x = x - tooltipWidth;
        }

        //left
        if (x - tooltipWidth - (tooltipWidth * .10) / 2 < 0) {
            x = x / 3 + 20;
        }

        setMousePosition({ x, y });
    };




    return (
        <div className="relative flex items-center">
            <div onMouseEnter={() => setIsHovering(true)}
                onMouseLeave={() => setIsHovering(false)}
                onMouseMove={handleMouseMove}
            >
                
                <img className="object-fill z-9 w-14 drop-shadow-xl"  alt="masterwork" src={image} />
            </div>

            {isHovering && (
                <div className="fixed w-64 p-4 mt-2 bg-gray-700 text-white rounded-md shadow-lg z-10 transform "
                    style={{
                        left: mousePosition.x,
                        top: mousePosition.y,
                        transform: 'translate(10%, 10%)' // Adjust this to position the tooltip as needed
                    }}>
                    <div className="perk-arrow">
                        <div className='perk-name'>
                            <h3 className="text-lg border-y font-bold">{name}</h3>
                        </div>
                        <div className='perk-subtitle font-semibold'>
                            <p className="text-white">
                                Masterwork
                            </p>
                        </div>

                        <p className="text-sm text-left text-wrap">{description}</p>
                    </div>
                </div>
            )}
        </div>
    );
}
