//everything inside js happens in execution context

//js is a synchronous single threaded language

var n=2;

function square(num){
  var ans= num *num;
  return ans;
}

var square2 = square(n);
var square4 = square(4);

console.log(square2,square4);

// call stack maintains the order of exection of execution contexts
