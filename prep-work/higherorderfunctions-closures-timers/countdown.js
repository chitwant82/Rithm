// Write a function called countdown that accepts a number as a parameter and every 1000 milliseconds decrements the value and console.logs it.
// Once the value is 0 it should log "DONE!" and stop.


function countDown(count) {
    var timerId = setInterval(function() {
        count--;
        if (count <= 0) {
            console.log("DONE!");
            clearInterval(timerId);
        }
        else {
            console.log(count);
        }
    }, 1000);
}

countDown(8);
