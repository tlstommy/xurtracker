import React, { useEffect, useState } from 'react';
import { Link, useLocation } from 'react-router-dom';

import {ReactComponent as GithubIcon} from "../assets/icons/github-logo.svg";
import {ReactComponent as TwitterIcon} from "../assets/icons/twitter-logo.svg";


export default function NavbarSimp() {

  
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  

  //mobile menu
  const toggleMobileMenu = () => {
    setIsMobileMenuOpen(!isMobileMenuOpen);
  };


  return (
    
    <header className="nav bg-navbar top-0 fixed z-20 w-full items-center justify-between shadow-md">
        <div className="bg-gray-600 w-full flex flex-wrap p-3 flex-col lg:flex-row items-center">
          <div className="flex items-center justify-between w-full lg:w-auto pl-2 ">
            <Link to="/" className="flex items-center font-medium text-white lg:mb-0">
              <span className="navbar-name ml-auto text-xl">Xûr Tracker</span>
            </Link>
            <button className="lg:hidden navbar-toggle-button-mobile ml-auto text-white focus:outline-none py-1 px-1 border rounded " onClick={toggleMobileMenu}>
              <svg className="h-6 w-6 fill-current" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                {isMobileMenuOpen ? (<path fillRule="evenodd" clipRule="evenodd"d="M3 5h18v1H3V5zm0 6h18v1H3v-1zm0 6h18v1H3v-1z"/>) : (<path fillRule="evenodd" clipRule="evenodd" d="M4 6h16v1H4V6zm0 4h16v1H4v-1zm0 4h16v1H4v-1z"/>)}
              </svg>
            </button>
          </div>
          <nav className="navbar hidden lg:block lg:mr-auto lg:ml-4  lg:pl-4 lg:border-l lg:border-l-2  lg:border-gray-500 flex flex-wrap items-center text-md font-semibold justify-center">
            &nbsp;

           
            
            
            
          </nav>
          <nav className="navbar hidden lg:block items-right lg:pl-4 lg:border-l lg:border-l-2  lg:border-gray-500 flex flex-wrap items-center text-md font-semibold justify-center">
            <Link to="https://x.com/XurTrack" className="navbar-item mx-3 hover:fill-white ">
              <TwitterIcon style={{ width: "1.25em", height: "1.25em", display: "inline"}}/>
            </Link>
            <Link to="https://github.com/tlstommy/xurtracker" className="navbar-item mx-3 hover:fill-white text-navbar-text">
              <GithubIcon style={{ width: "1.5em", height: "1.5em", display: "inline" }}/>
            </Link>
            
          </nav>
        </div>
          
          {isMobileMenuOpen && (<nav className="lg:hidden bg-gray-700 px-4 py-4 flex flex-col">
            
            <div className="pt-2">
              
              <Link to="https://x.com/XurTrack" className="navbar-item mx-3 fill-white " onClick={() => setIsMobileMenuOpen(false)}>
                <TwitterIcon style={{ width: "1.25em", height: "1.25em", display: "inline"}}/>
              </Link>
              <Link to="https://github.com/tlstommy/xurtracker" className="navbar-item mx-3 fill-white text-navbar-text" onClick={() => setIsMobileMenuOpen(false)}>
                <GithubIcon style={{ width: "1.5em", height: "1.5em", display: "inline" }}/>
              </Link> 
            </div>
            
          </nav>)}
    </header>
  );
}