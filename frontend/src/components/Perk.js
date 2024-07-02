import React, { useState } from 'react';


export default function Perk(props) {
  const [isHovering, setIsHovering] = useState(false);
  const [mousePosition, setMousePosition] = useState({ x: 0, y: 0 });

  const handleMouseMove = (e) => {
    const tooltipWidth = 256;
    const screenWidth = window.outerWidth;
    let x = e.clientX;
    let y = e.clientY;

    // move tooltip over if its getting off the page on the right
    if(x + tooltipWidth + (tooltipWidth * .10) / 2 > screenWidth) {
      x =  x - tooltipWidth;
    }

    //left
    if(x - tooltipWidth - (tooltipWidth * .10) / 2 < 0) {
      x =  x/3 +20;
    }

    setMousePosition({x,y});
  };

  const {name,type,subtype,image,description,index} = props;


  return (
    <div className="relative flex items-center">
      <div onMouseEnter={() => setIsHovering(true)} 
        onMouseLeave={() => setIsHovering(false)}
        onMouseMove={handleMouseMove}
      >
        {/* for exotic perks ternary*/}
        <img className={index !== 0 ? "object-fill z-9 sm:p-1 w-16 lg:w-16 xl:w-24  lg drop-shadow-xl hover:ring sm:border rounded-full ring-white" : "object-cover z-9 w-16 lg:w-16 xl:w-16 drop-shadow-2xl rounded-full hover:ring ring-yellow-400"} alt='perk' src={image} />
      </div>

      {isHovering && (
        <div className="fixed shadow-xl w-64 mx-4 pb-4 mt-2 bg-gray-700 text-white rounded-md border-2 border-white shadow-lg z-10 transform"
        style={{ 
          left: mousePosition.x,
          top: mousePosition.y,
          transform: 'translate(10%, 10%)'
        }}>
          <div className="perk-arrow">
            <div className='perk-name'>
              <h3 className="text-lg border-b font-bold">{name}</h3>
            </div>
            <div className='perk-subtitle text-sm font-normal'>
              <p className={index !== 0 ? "text-gray-300" : "text-yellow-400"}>
                {index !== 0 ? ` ${type}` : "Exotic Intrinsic"}
              </p>
            </div>
            
            <p className="text-sm text-left px-2 text-wrap">{description}</p>
          </div>
        </div>
      )}
    </div>
  );
}
