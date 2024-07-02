import React, { useState } from 'react';


export default function FramePerk(props) {
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

  const {name,image,description, imageSize} = props;


  return (
    <div className="relative flex items-center">
      <div onMouseEnter={() => setIsHovering(true)} 
        onMouseLeave={() => setIsHovering(false)}
        onMouseMove={handleMouseMove}
      >
        
        <img className={`object-fill z-9 drop-shadow-xl `} alt='perk' src={image} style={{ width: imageSize }}/>
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
              <h3 className="text-lg border-y text-center font-bold">{name}</h3>
            </div>
            <div className='perk-subtitle text-sm font-normal'>
              <p className="text-gray-300 text-center">
                Intrinsic
              </p>
            </div>
            
            <p className="text-sm text-left px-2 text-wrap">{description}</p>
          </div>
        </div>
      )}
    </div>
  );
}
