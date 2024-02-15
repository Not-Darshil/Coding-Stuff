const prompt = require("prompt-sync")();
// Q1. Create an array of numbers and take input from the user to add numbers to this array


/*
const k = [10,15,20];
console.log("Old Array: ", k);
let n = prompt("How Many numbers? :");
for (let i = 0; i < n; i++) {
    let x = prompt("Enter a number:");
    x=Number.parseInt(x);
    k.push(x);
}
console.log("Old Array: ", k);

*/


/*
// Q2.Keep adding numbers to the array in Q1. until 0 is added to the array.
const k = [10, 15, 20];
console.log("Old Array: ", k);
console.log("Enter 0 for exit: ");
let x
while (x != 0) {
    x = prompt("Enter a number:");
    x = Number.parseInt(x); 
    if (x == "0") {
        break;
    } 
    k.push(x);
}
console.log("New Array: ", k);
*/



/*
// Q3. Filter for number divisible by 10 from a given array.
let k=[10,15,20,25,30,35];
console.log(k)
const greater_than_10 = (a) => {
    return a%10==0;
}
let arr=k.filter(greater_than_10)
console.log("New Array:",arr)
*/


/*

//Q4. Creare an array of the square of the given array.
const k=[2,3,4,5,6,7,8];
console.log("Array:",k);
const fx = (x)=>{
    return x*x;
};
let sqr_arr=k.map(fx)
console.log("Squared Array:",sqr_arr);

*/



/*

//Q5. Use Reduce to calculate the factorial of a given no. from the array of first n natural no.(n being the no. whose factorial needs to be calculated.)
const k = []
let n = Number.parseInt(prompt("Factorial of? :"));

for (let i = 1; i <= n; i++) {
    k.push(i);
}
console.log("Numbers:","\n",k)
const fact = (x1,x2) =>{
    return x1*x2;
}
let f=k.reduce(fact);
console.log("Factorial:",f)

*/