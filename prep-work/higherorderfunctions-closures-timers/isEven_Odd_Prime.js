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
