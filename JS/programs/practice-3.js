const prompt = require("prompt-sync")();

// write a program to print the marks of a student in an object using for loop
// obj={hary:98}

// const marks={"Harry":98,"Rohan":70,"Aakash":78}
// for (let i=0; i<Object.keys(marks).length; i++)
// {
//     console.log(Object.keys(marks)[i]+":"+marks[Object.keys(marks)[i]])

// }

// q.2 do same using for loop
// for (let w in marks)
// {
//     console.log(w+":"+marks[w]);

// }



// // Q.3 WRITE A PROGRAM TO PRINT "TRY AGAIN" 
// UNTIL THE USER ENTERS THE CORRECT Number.

// const number=501;
// let guess;
// while (guess!=number)
// {
//  console.log("Try Again...");
//  guess=prompt("Enter Your 3 Digited Guess Number:");   
// }
// console.log("You guessed it right");



// Q.5 WRITE A FUNCTION TO FIND THE MEAN OF 5 NUMBERS
const m=(n1,n2,n3,n4,n5) =>
{
    let x=(n1 + n2 + n3 + n4 + n5);
    console.log(x);
    return x/5
}


// let var_n1=prompt("Enter N1:");
// var_n1=Number.parseInt(var_n1)
// let var_n2=prompt("Enter N2:");
// let var_n3=prompt("Enter N3:");
// let var_n4=prompt("Enter N4:");
// let var_n5=prompt("Enter N5:");
// console.log(m(var_n1,var_n2,var_n3,var_n4,var_n5))
console.log(m(4,5,6,7,8))
