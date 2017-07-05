// Write a function called numberFact which takes in a number and a callback and returns the result of the callback with the number passed to it

function isEven(num) {
    return num % 2 === 0;
}

console.log("2 is even: " + isEven(2));
console.log("3 is even: " + isEven(3));

function isOdd(num) {
    return num % 2 !== 0;
}

console.log("3 is odd: " + isOdd(3));
console.log("14 is odd: " + isOdd(14));

function isPrime(num) {
    for(var i = 2; i <= Math.sqrt(num); i++) {
        //console.log(i);
        if (num % i == 0)
           return false;
    }
    return num > 1;
}

console.log("8 is prime: " + isPrime(8));
console.log("17 is prime: " + isPrime(17));
console.log("5 is prime: " + isPrime(5));

function numberFact(a, callback) {
    return callback(a);
}

console.log("59 is even: " + numberFact(59, isEven));
console.log("59 is odd: " + numberFact(59, isOdd));
console.log("59 is prime: " + numberFact(59, isPrime));
