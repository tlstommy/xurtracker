import logo from './logo.svg';
import './App.css';

import React from "react";
import { BrowserRouter as Router, Switch, Route, Routes } from 'react-router-dom';


import Navbar from "./components/Navbar";
import NavbarSimp from './components/NavbarSimp';
import AllItemsPage from "./components/AllItemsPage";
import XurGone from './components/XurGone';


//checks if xur is present
function XurPresentCheck(){

  var today = new Date();
  var date = new Date();
  date.setDate(date.getDate() + ((7 - date.getDay()) % 7 + 5) % 7);
  var finalDate = date.getMonth() + '/' + (date.getDate() + 1) + '/' + date.getFullYear();
  var countDownDate = new Date(Date.UTC(date.getFullYear(), date.getMonth(), date.getDate(), 17, 0, 0)).getTime();
  var now = new Date().getTime();
  
  var distance = countDownDate - now;
  console.log("Today: ",today)
  console.log("Date: ",date)
  console.log("Distance: ",distance)
  console.log("Final Date: ",finalDate)
  console.log("CountDown Date: ",countDownDate)
  console.log("computed: ",(new Date(countDownDate)).toLocaleString())
  

  // Determine the next occurrence of Friday after 17:00 UTC
  let nextFriday = new Date(today.getTime());
  nextFriday.setUTCDate(today.getUTCDate() + ((5 - today.getUTCDay() + 7) % 7));
  nextFriday.setUTCHours(17, 0, 0, 0);

  // Determine the end time on Tuesday before 17:00 UTC
  let nextTuesday = new Date(nextFriday.getTime());
  nextTuesday.setUTCDate(nextTuesday.getUTCDate() + 4);
  nextTuesday.setUTCHours(16, 59, 59, 999);

  let fridayBefore = new Date(nextFriday.getTime());
  fridayBefore.setUTCDate(fridayBefore.getUTCDate() - 7);
  fridayBefore.setUTCHours(17, 0, 0, 0);


  let tuesdayBefore = new Date(fridayBefore.getTime());
  tuesdayBefore.setUTCDate(tuesdayBefore.getUTCDate() + 4);
  tuesdayBefore.setUTCHours(16, 59, 59, 999);

  console.log("\n\n\nnow: ",today)
  console.log("friday: ",nextFriday)
  console.log("tuesday:  ",nextTuesday)
  console.log("friday before: ", fridayBefore)
  console.log("tuesday before: ",tuesdayBefore )
  console.log(now >= nextFriday)
  console.log(now <= nextTuesday)



  if (today >= fridayBefore && today <= tuesdayBefore){
    console.log("in between fb and tb")
    console.log("xur present")
    return(
      <Router>
        <Navbar/>
        <Routes>
          <Route exact path="/" Component={AllItemsPage} />
        </Routes>
      </Router>
    );
  } else if (today >= nextFriday && today <= nextTuesday){
    console.log("in between nf and nt")
    console.log("xur present")
    return(
      <Router>
        <Navbar/>
        <Routes>
          <Route exact path="/" Component={AllItemsPage} />
        </Routes>
      </Router>
    );
  } else{
    console.log("Xur gone")
    return(
      <Router>
        <NavbarSimp />
        <Routes>
          <Route exact path="/" Component={XurGone} />
        </Routes>
      </Router>
    );

  }

  
}

function App() {
  return (
    <div className="App flex flex-col min-h-screen">
      <XurPresentCheck />
    </div>
  );
}

export default App;
