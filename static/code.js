//calculate time difference
var timeZone = new Date().toLocaleDateString(undefined, { day: '2-digit', timeZoneName: 'short' }).substring(4);
var time = -(new Date().getTimezoneOffset() / 60);
var resetTime = 17 + time;
var meridiem = "";
if (resetTime < 12) {
    meridiem = "AM.";
} else {
    if (resetTime != 12) {
        resetTime = resetTime - 12;
    }
    meridiem = "PM.";
}
var resetString = "X&#251r will return on Friday at " + resetTime + ":00 " + meridiem;
document.getElementById("timeZone").innerHTML = resetString;
//find next friday
var today = new Date();
var date = new Date();
date.setDate(date.getDate() + ((7 - date.getDay()) % 7 + 5) % 7);
var finalDate = date.getMonth() + '/' + (date.getDate() + 1) + '/' + date.getFullYear();
var countDownDate = new Date(Date.UTC(date.getFullYear(), date.getMonth(), date.getDate(), 17, 0, 0)).getTime();
var x = setInterval(function () {
    var now = new Date().getTime();
    var distance = countDownDate - now;
    var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);
    if (days == 1) {
        document.getElementById("xurCountdown").innerHTML = days + " Day&nbsp" + ("00" + hours).slice(-2) + ":" + ("00" + minutes).slice(-2) + ":" + ("00" + seconds).slice(-2) + "";
    } else if (days == 0) {
        document.getElementById("xurCountdown").innerHTML = ("00" + hours).slice(-2) + ":" + ("00" + minutes).slice(-2) + ":" + ("00" + seconds).slice(-2) + "";
    } else {
        document.getElementById("xurCountdown").innerHTML = days + " Days&nbsp" + ("00" + hours).slice(-2) + ":" + ("00" + minutes).slice(-2) + ":" + ("00" + seconds).slice(-2) + "";
    }
    if (distance < 0) {
        clearInterval(x);
        document.getElementById("xurCountdown").innerHTML = "00 : 00 : 00";
        window.location.href = "searching";
    }
}, 1000);