// Write a function called randomGame that selects a random number between 0 and 1 every 1000 milliseconds and each time that a random number is picked, add 1
// to a counter.
// If the number is greater than .75, stop the timer and return the number of tries it took before we found a number greater than .75.

function randomGame() {
    var num;
    var count = 0;
    var timerId = setInterval(function() {
        num = Math.random().toFixed(2);
        console.log("RANDOM NUM: " + num);
        count++;
        if (num > 0.75) {
            clearInterval(timerId);
            console.log("TRIES: " + count);
        }

    }, 1000);
}

randomGame();
