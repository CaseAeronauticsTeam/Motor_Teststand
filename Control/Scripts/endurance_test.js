
rcb.console.print("Initializing ESC...");
rcb.output.set("esc",1000);
rcb.wait(ramp_up, 4);

//Create a new log
rcb.files.newLogFile({prefix: "Endurance"});

rcb.sensors.setSafetyLimit("voltage", 18.5, 25.5);

//Start the sequence
rcb.sensors.read(saveResult, 1);

function saveResult(result){
    rcb.files.newLogEntry(result, readSensor);
}

function readSensor() {
    rcb.sensors.read(saveResult,1);
}

function ramp_up(){
    var from = 1000;
    var to = 1600;
    var duration = 10;
    var done = rcb.endScript;
    rcb.output.ramp("esc", from, to, duration, hold_throttle);
}

function hold_throttle() {
    rcb.output.set("esc", 1600);
}

