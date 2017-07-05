// Write a function called find. It should take in an array and a callback and return
// the first value found in the array that matches the condition.

// Write a function called findIndex. It should take in an array and a callback and
// return the index of first value found in the array that matches the condition.

function find(arr, fn) {
    for (var i=0; i < arr.length; i++) {
        if (fn(arr[i]))
            return arr[i];
    }
}

var ele = find([8,11,4,27], function(val){return val >= 10});
console.log("Element found is: " + ele);
ele = find([8,11,4,27], function(val){return val === 5});
console.log("Element found is: " + ele);

function findIndex(arr, fn) {
    for (var i=0; i < arr.length; i++) {
        if (fn(arr[i]))
            return i;
    }
}

var idx = findIndex([8,11,4,27], function(val){return val >= 10});
console.log("Index found is: " + idx);
idx = findIndex([8,11,4,27], function(val){return val === 7});
console.log("Index found is: " + idx);
