import React from "react";

export default function ItemInfoModal({itemDetails, closeModal }) {
    // Function to stop propagation to avoid closing modal when clicking inside it
    const handleClickInside = e => e.stopPropagation();

    return (
        <div className="fixed inset-0 bg-black bg-opacity-60 overflow-y-auto h-full w-full flex justify-center items-center" onClick={closeModal}>
            <div className="relative bg-white rounded-lg shadow-xl w-full max-w-2xl mx-4" onClick={handleClickInside}>
                <div className="flex justify-between items-center border-b border-gray-200 p-5 rounded-t-lg bg-gray-800 text-white">
                    <h3 className="text-xl font-semibold">Exotic Weapon Details</h3>
                    <button onClick={closeModal} className="text-gray-400 bg-transparent hover:bg-gray-700 hover:text-white rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" aria-label="Close">
                        <svg xmlns="http://www.w3.org/2000/svg" className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M6 18L18 6M6 6l12 12" />
                        </svg>
                    </button>
                </div>
                <div className="p-6">
                    <p className="text-gray-700 text-sm leading-relaxed">More detailed information about the weapon...</p>
                    {/* Place additional content here */}
                </div>
                <div className="flex justify-end p-6 border-t border-gray-200 rounded-b-lg">
                    <button onClick={closeModal} className="px-6 py-2.5 bg-yellow-500 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-yellow-600 hover:shadow-lg focus:bg-yellow-600 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-yellow-700 active:shadow-lg transition duration-150 ease-in-out">
                        Close
                    </button>
                </div>
            </div>
        </div>
    );
}
