
rcb.console.print("Initializing ESC...");
rcb.output.set("esc", 1000);
rcb.wait(callback, 4);  // Wait 4 seconds for ESC initialization sequence

//Create a new log
rcb.files.newLogFile({prefix: "Stress"});

//Start the sequence
readSensor();
	  
    function readSensor() {
        rcb.sensors.read(saveResult,1);
    }

function saveResult(result) {
    rcb.files.newLogEntry(result, readSensor);
}

function callback() {
    var from = 1140;      // 14%
    var to = 2000;        // 100%
    var duration = 30;    // s
    var done = rcb.endScript;
    rcb.output.ramp("esc", from, to, duration, done);
}

