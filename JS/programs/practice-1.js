// 1.create a variale of type string and try to
//  add a number to it

let a="hi";
let b=10;
let c;
c=a+b;
console.log(c);

// use typeof operator to find the datatype 
// of the string in the last question
console.log("Datatype of c:",typeof c);

// 3. create a const object in javascript. can 
// you change it to hold a number later?

// 4.try to add a new key to the const object 
// in problem 3. were you able to do it?

const d=
{
    "hi":50,
    "hello":75
};
console.log(d);
d["hi"]=25;
d["whatsup"]=100;
console.log(d);


// 5.WAP to create a word meaning dictionary 
// of 5 words/
const dict = 
{"pen":"stationary",
"eraser":"stationary",
"glass":"utensils",
"food":"grocery",
"mobiles":"electronics"
};
console.log(dict);
