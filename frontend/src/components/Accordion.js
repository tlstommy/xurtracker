import React, { useState } from "react";

export default function Accordion(props) {
    const [isExpanded, setIsExpanded] = useState(false);
    const { accordionTitle, title, subtitle, content } = props;

    const handleAccordionToggle = () => {
        setIsExpanded(!isExpanded);
    };

    return (
        <div className="accordion w-full px-2" onClick={(e) => e.stopPropagation()} onTap={(e) => e.stopPropagation()}>
            <button 
                onClick={handleAccordionToggle} 
                className="w-full text-left xs:h-32 flex items-center justify-between text-white font-medium border px-1 py-8 sm:py-2 border-t-0 border-r-0 border-l-0 hover:border-t hover:border-r hover:border-l border-gray-200 gap-3"
                aria-expanded={isExpanded}
            >
                <span className="font-bold text-xl">{accordionTitle}</span>
                <svg 
                    className={`w-3 h-3 ${isExpanded ? '' : 'rotate-180'} shrink-0`}
                    aria-hidden="true" 
                    xmlns="http://www.w3.org/2000/svg" 
                    fill="none" 
                    viewBox="0 0 10 6"
                >
                    <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 5 5 1 1 5"/>
                </svg>
            </button>
            {isExpanded && (
                <div className="accordion-content whitespace-pre-line text-white accordion-scrollbar bg-[rgba(31,32,37,0.9)] text-gray-300 backdrop-blur-lg p-4 border border-t-0 border-gray-200 max-h-[32rem] overflow-y-auto">
                    <h1 className="text-2xl font-semibold">{title}</h1>
                    <hr/><br/>
                    <blockquote className="text-md font-normal rounded-md">{content}</blockquote>
                </div>
            )}
        </div>
    );
}
