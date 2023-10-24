
var exerciseName = '';
var setAmount = '';
var repAmount = '';
var durationTimer = '';
var durationMinutes = '';
var durationSeconds = '';
let [minutes,seconds] = [0,0];


//event listeners
window.addEventListener("DOMContentLoaded", (event) => {
  const el = document.getElementById('start');
  if (el) {
    //powering the sun
    el.addEventListener('click', poweringSun);
  }
});

function createUserWeightWorkout(){
    //dont know if these values will work, first time working with objects/keys
    //TO-DO: Create user array to save custom workout for reuse.
}

function createUserCardioWorkout(){
    var runTimer;
    console.log('Enter the run duration:')
}
//goal of this function is to grab the value of all our labels and begin the process here.
//WORKING
function poweringSun(){
  //grabbing and setting values needed
  durationMinutes = $('#dMinutes').val();
  durationSeconds = $('#dSeconds').val();
  exerciseName = $('#eName').val();
  setAmount = $('#sAmount').val();
  repAmount = $('#rAmount').val();
//creating object of the current exercise
  const currentExercise = {
    name:exerciseName,
    duration:durationTimer,
    set: setAmount,
    minutes: durationMinutes,
    seconds: durationSeconds,
  }
  //passing
  beginTimer(currentExercise);
}

//function to begin the timer
//returning something back to blackhole?
//cycle back to this idea in a second
//TO-DOs
//VALIDATION CHECK FOR 60 SECONDS

function beginTimer(time){
     const d = new Date();
      let sec = 0;
      let minute = 0;
      timerSeconds = time.seconds;
      timerMinutes = time.minutes;
      //counting a second
      console.log("inside begin timer, seconds amount", timerSeconds);
      //testing here setting up new variables to be used
      //setting time element
      const timeElement = document.getElementById("time");
      let invalidId = null;
      console.log('starting setInterval|| Time before: ', timerSeconds, " ", timerMinutes);

         if(time.seconds > 60){
         console.log('dumbass');
         timeElement.innerHTML = "Please enter a proper second amount";
         }else{
          invalidId = setInterval(() =>{
            for(let i = 0; i <= timerSeconds; i++){
            console.log(i, " ", timerSeconds);
            //if statement to properly put a zero into the html if the seconds go under 10
            if(timerSeconds < 10){
            timeElement.innerHTML =  timerMinutes + ":0" + timerSeconds;
            }else{
                 timeElement.innerHTML =  timerMinutes+ ":" + timerSeconds;
                }
            }
            timerSeconds--;
            //works (for now)
            if(timerSeconds == 0 & timerMinutes != 0){
                timerMinutes--;
                timerSeconds = 99;
            }
            console.log('ending: ', timerSeconds);
          },1000);
          //set up a way to stop the loop from running here
          //invalidId = null;
          console.log(minute, " ", sec, " timers");
         }

}



//starting our sprint workout
function startSprintWorkout(runTimer){
//create timer

//start and show timer

}


