/*Write a Java Script program to generate a random number and store it in a variable. The program then takes an input from the user to tell them whether the Correct, greater or lesser than guess was correct, greater the original number. 
100 - (n     of guesses) is the score of the user The program is expected to terminate once the number is glossed. Number should be between 1-100 */

const prompt = require("prompt-sync")();
console.log("Game Started:");
const x = Math.floor((Math.random() * 100) + 1);
let score = 100;
let guess = -1;
console.log(x);
while ((score>0)||(guess!=x))
{
    score=score-1
    guess=Number.parseInt(prompt("Enter you Guess:"));
    if (guess==x){
        console.log("Your guess was correct");
        console.log("Score: " , score);
        break;
    }
    else if (guess>x){
        console.log("Smaller");
        
    }
    else if (guess<x){
        console.log("Greater");
    }
    
    

}

