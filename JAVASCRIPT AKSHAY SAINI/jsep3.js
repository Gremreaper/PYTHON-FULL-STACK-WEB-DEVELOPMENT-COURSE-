var x =7;

function getName(){
    console.log("Namaste Javascript");
}

getName();
console.log(x);



//but in hoisting

getName();
console.log(x);

var x=7;

function getName(){
    console.log("Namaste Javascript")
}

//hoisting is a phenomenon for accessing variable function even before initialization

var y=8;

function check(){
console.log("Namaste JS");
}

console.log(check);
//prints the whole function from the start

// functions in js can be written in 2 more ways

var getname= () =>{
    console.log("Namaster JS");
}

var getname = function() {
    console.log("Namasye JS")
}
