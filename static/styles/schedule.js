var months = {
    "January":31,
    "February":28,
    "March":31,
    "April":30,
    "May":31,
    "June":30,
    "July":31,
    "August":31,
    "September":30,
    "October":31,
    "November":30,
    "December":31
};

var monthsList = [ "January", "February", "March", "April", "May", "June", 
           "July", "August", "September", "October", "November", "December" ];

let curYear = new Date().getFullYear(); 
let days = document.getElementsByClassName("col-sm-1");
let curMonth = new Date().getMonth();
document.getElementById("month").innerHTML = monthsList[curMonth];
curMonth = document.getElementById("month").innerHTML;
let startMonth = document.getElementById("month").innerHTML;
let monthLength = months[curMonth];
let curDay = new Date().getDate();

function setMonth(){
    curMonth = document.getElementById("month").innerHTML;
    monthLength = months[curMonth];
}

function getNextMonth(month){
    let keys = Object.keys(months);
    let nextIndex = keys.indexOf(month) + 1;
    if(nextIndex == 12){
        nextIndex = 0;
        curYear += 1;
    }
    let nextMonth = keys[nextIndex];
    return nextMonth;
}

function getPrevMonth(month){
    let keys = Object.keys(months);
    let prevIndex = keys.indexOf(month) - 1;
    if(prevIndex == -1){
        prevIndex = 11;
        curYear -= 1;
    }
    let prevMonth = keys[prevIndex];
    return prevMonth;
}

let highlightedDay = false;

function fillDays() {
    for (const day of days) {
        if(day.id <= monthLength){
            day.innerHTML = day.id;
        } else{
            day.innerHTML = day.id - monthLength;
        }

        if (day.innerHTML == curDay && curMonth == startMonth && highlightedDay == false){
            console.log(startMonth);
            day.classList.add("curDay");
            highlightedDay = true;
        } else {
            if(day.classList.contains("curDay")){
                console.log("hi");
                day.classList.remove("curDay");
            }
        }
    }

    if(curMonth != startMonth){
        highlightedDay = false;
    }
    
}

document.getElementById("prev").addEventListener("click", e=>{
    document.getElementById("month").innerHTML = getPrevMonth(document.getElementById("month").innerHTML);
    setMonth();
    fillDays();
})

document.getElementById("next").addEventListener("click", e=>{
    document.getElementById("month").innerHTML = getNextMonth(document.getElementById("month").innerHTML);
    setMonth();
    fillDays();
})

function getMonthFromString(mon){

    var d = Date.parse(mon + "1, 2012");
    if(!isNaN(d)){
       let goodDate = new Date(d).getMonth() + 1;
       if(String(goodDate).length == 1){
        goodDate = 0 + String(goodDate);
       }
       return goodDate;
    }
    return -1;
}

function goToWindow(day){
    if(day.id < 10){
        window.location.href="info/" + curYear + "-" + getMonthFromString(curMonth) + "-" + "0" + day.id;
    } else if(day.id <= monthLength){
        window.location.href="info/" + curYear + "-" + getMonthFromString(curMonth) + "-" + day.id;
    } else{
        window.location.href="info/" + curYear + "-" + getMonthFromString(getNextMonth(curMonth)) + "-" + "0" + (day.id - monthLength);
    }
}

for (const day of days) {

    day.addEventListener("click", e => {
        goToWindow(day);
    })

    if(day.id <= monthLength){
        day.innerHTML = day.id;
    } else{
        day.innerHTML = day.id - monthLength;
    }

    if (day.innerHTML == curDay && curMonth == startMonth && highlightedDay == false){
        console.log(startMonth);
        day.classList.add("curDay");
        highlightedDay = true;
    } else {
        if(day.classList.contains("curDay")){
            console.log("hi");
            day.classList.remove("curDay");
        }
    }
}

