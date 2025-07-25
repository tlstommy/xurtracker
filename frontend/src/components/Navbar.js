import React, { useEffect, useState } from 'react';
import { Link, useLocation } from 'react-router-dom';

import destinyData from '../destinyData.json';
import {ReactComponent as GithubIcon} from "../assets/icons/github-logo.svg";
import {ReactComponent as TwitterIcon} from "../assets/icons/twitter-logo.svg";

export default function Navbar() {

  const { pathname, hash } = useLocation();
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  const artificeBeingSold = destinyData.Artifice;

  useEffect(() => {
    //after render if hash and section exist scroll to it, if not just scroll to top
    if (hash) {
      const sectionId = hash.replace("#","");
      const section = document.getElementById(sectionId);
      if (section) {
        window.scrollTo({
          top: section.offsetTop,
          behavior: "smooth",
        }); 
      }
    } else {
      window.scrollTo({
        top: 0,
        behavior: "smooth",
      });
    }
  }, [pathname, hash]);
  
  //artifice check
  function ArtificeArmorCheck({artificeForSale,mobile}){
    if(artificeBeingSold){
      
        if(mobile){
          return(
            <Link to="#artifice" className="block navbar-item mr-3 text-white py-2 hover:text-white font-semibold" onClick={() => setIsMobileMenuOpen(false)}>
              Artifice
            </Link>
          );
            
          
        }else{
          return(
            
            <Link to="#artifice" className="navbar-item mr-3 hover:text-white text-navbar-text">
              Artifice
            </Link>     
          
          );
        }
    }else{
        return null
    }
  }

  

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
            <Link to="#material-offers" className="navbar-item mr-3 hover:text-white text-navbar-text">
              Materials
            </Link>
            <Link to="#exotic-weapons" className="navbar-item mr-3 hover:text-white text-navbar-text">
              Exotic Weapons
            </Link>
            <Link to="#exotic-armor" className="navbar-item mr-3 hover:text-white text-navbar-text">
              Exotic Armor
            </Link>
           
            <Link to="#legendary-weapons" className="navbar-item mr-3 hover:text-white text-navbar-text">
              Legendary Weapons
            </Link>
            {/* 
            not needed in edge of fate
            <Link to="#legendary-armor" className="navbar-item mr-3 hover:text-white text-navbar-text">
              Legendary Armor
            </Link>
            */}
            <ArtificeArmorCheck artificeForSale={artificeBeingSold} mobile={false}/>

           
            
            
            
          </nav>
          <nav className="navbar hidden lg:block items-right lg:pl-4 lg:border-l lg:border-l-2  lg:border-gray-500 flex flex-wrap items-center text-md font-semibold justify-center">
            <Link to="https://x.com/XurTrack" className="navbar-item mx-3 hover:fill-white " title="Twitter Alerts">
              <TwitterIcon style={{ width: "1.25em", height: "1.25em", display: "inline"}}/>
            </Link>
            <Link to="https://github.com/tlstommy/xurtracker" className="navbar-item mx-3 hover:fill-white text-navbar-text" title="GitHub Repository">
              <GithubIcon style={{ width: "1.5em", height: "1.5em", display: "inline" }}/>
            </Link>
            
          </nav>
        </div>
          
          {isMobileMenuOpen && (<nav className="lg:hidden bg-gray-700 px-4 py-4 flex flex-col">
            <Link to="#material-offers" className="block navbar-item mr-3 text-white py-2 hover:text-white font-semibold hover:text-white" onClick={() => setIsMobileMenuOpen(false)}>
              Materials
            </Link>
            <Link to="#exotic-weapons" className="block navbar-item mr-3 text-white py-2 hover:text-white font-semibold" onClick={() => setIsMobileMenuOpen(false)}>
              Exotic Weapons
            </Link>
            <Link to="#exotic-armor" className="block navbar-item mr-3 text-white py-2 hover:text-white font-semibold" onClick={() => setIsMobileMenuOpen(false)}>
              Exotic Armor
            </Link>
            <Link to="#legendary-weapons" className="block navbar-item mr-3 text-white py-2 hover:text-white font-semibold" onClick={() => setIsMobileMenuOpen(false)}>
              Legendary Weapons
            </Link>
            <Link to="#legendary-armor" className="block navbar-item mr-3 text-white py-2 hover:text-white font-semibold" onClick={() => setIsMobileMenuOpen(false)}>
              Legendary Armor
            </Link>

            <ArtificeArmorCheck artificeForSale={artificeBeingSold} mobile={true}/>

            
            
            <div className="pt-2">
              
              <Link to="https://x.com/XurTrack" className="navbar-item mx-3 fill-white " title="Twitter Alerts" onClick={() => setIsMobileMenuOpen(false)}>
                <TwitterIcon style={{ width: "1.25em", height: "1.25em", display: "inline"}}/>
              </Link>
              <Link to="https://github.com/tlstommy/xurtracker" title="GitHub Repository" className="navbar-item mx-3 fill-white text-navbar-text" onClick={() => setIsMobileMenuOpen(false)}>
                <GithubIcon style={{ width: "1.5em", height: "1.5em", display: "inline" }}/>
              </Link> 
            </div>
            
          </nav>)}
    </header>
  );
}