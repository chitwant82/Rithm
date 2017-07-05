// Write a function called specialMultiply which accepts two parameters. If the function
// is passed both parameters, it should return the product of the two.
// If the function is only passed one parameter - it should return a function which can later
// be passed another parameter to return the product. You will have to use closure
// and arguments to solve this.


function specialMultiply(a,b) {
    if (arguments.length === 1) {
        return function inner(b) {
            return a * b;
        }
    }

    return a * b;
}

var a = specialMultiply(3, 4);
console.log(a);

var b = specialMultiply(3)(4);
console.log(b);

var c = specialMultiply(3);
console.log(c(4));
