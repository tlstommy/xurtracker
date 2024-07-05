import React, { useState, useEffect } from "react";

function Countdown() {
  const [timeLeft, setTimeLeft] = useState('Calculating...');

  useEffect(() =>{
    const targetDay = new Date();
    targetDay.setDate(targetDay.getDate() + ((7 - targetDay.getDay()) % 7 + 5) % 7);
    const countDownDate = new Date(Date.UTC(targetDay.getFullYear(), targetDay.getMonth(), targetDay.getDate(), 17, 0, 0)).getTime();

    const interval = setInterval(() => {
      const now = new Date().getTime();
      const distance = countDownDate - now;

      if (distance < 0) {
        clearInterval(interval);
        setTimeLeft("00 : 00 : 00");
        
      } else {
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);
        setTimeLeft(`${days} Day${days !== 1 ? 's' : ''} ${("00" + hours).slice(-2)}:${("00" + minutes).slice(-2)}:${("00" + seconds).slice(-2)}`);
      }
    }, 1000);

    return () => clearInterval(interval);
  }, []);

  return <div>{timeLeft}</div>;
}

function ReturnDate(){
    var timeZone = new Date().toLocaleDateString(undefined, { day: '2-digit', timeZoneName: 'short' }).substring(4);
    var time = -(new Date().getTimezoneOffset() / 60);
    var resetTime = 17 + time;
    var meridiem = "";
    if (resetTime < 12) {
        meridiem = "AM.";
    } else {
        if (resetTime !== 12) {
            resetTime = resetTime - 12;
        }
        meridiem = "PM.";
    }
    var resetString = "Xûr will return on Friday at " + resetTime + ":00 " + meridiem;
    
    return <div>{resetString}</div>;
}

export default function XurGone() {
  return (
    <div className="min-h-screen flex flex-col">
      <div className="flex flex-1 flex-col sm:flex-row">
        <nav className="md:w-32 lg:w-36 order-first sm:order-none"></nav>
        <main className="flex-1 flex items-center justify-center">
          <div className="flex justify-center w-full h-auto py-4 px-2">
            <div className="w-full z-10 max-w-xs sm:max-w-xl bg-ui-grey border border-gray-700 shadow-xl cursor-pointer">
              <h2 className="text-4xl text-white mt-4 p-2 font-bold text-center">
                Xûr has left the system...
                <hr className="mx-1 sm:mx-14 mt-2"/>
              </h2>
              <p className="text-white pt-2 text-3xl font-normal">
                Xûr will be back in <Countdown />
              </p>
              <p className="text-white pt-4 pb-4 text-small font-normal">
                <ReturnDate/>
              </p>
            </div>
          </div>
        </main>
        <aside className="md:w-32 lg:w-36 hidden sm:block"></aside>
        
      </div>
      <footer className="mt-auto w-full bg-gray-600 text-white text-center p-4">
          &nbsp;
      </footer>
    </div>
  );
}
