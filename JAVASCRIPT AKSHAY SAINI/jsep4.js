var x=1;
a(); b(); //possible due to hoisting

console.log(x);

function a(){
  var x=10;
  console.log(x);
}

function b(){
  var x=100;
  console.log(x);
}

//understanding the call stack and whole execution context
