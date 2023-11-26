// const percent_calculator = function(result_array)
// {
//     if (result_array.length===2)
//     {
//         let first_digit=result_array[0].toString();
//         let second_digit=result_array[1].toString();
//         return first_digit+second_digit;
//     }
//     else
//     {
//         let intermediate_array=[];
//         if (result_array.length==1)
//         {
//             intermediate_array.push(result_array[0]);
//         }
//         for (let i=0; i<(parseInt(result_array.length/2)); i++)
//         {
//             intermediate_array.push(result_array[0]+result_array[-1]);
//             result_array.shift();
//             result_array.pop();
//         }
//         intermediate_array.push(result_array[0]);
//         console.log(intermediate_array);
//     }
// }

// percent_calculator([1,1,1,2,2,1,3,1]);//percent:2424..86
// percent_calculator([3,1,2,2,1,3,1]);//percent:4432..67

// need to focus on the borrow method while adding
// indexing ka use krke kre agr like [0]+[-1] aur loop run kia len/2 and last element agr h to push also while adding make sure krenge ki uski value <10 h agr nahi h to 2 bar push krdenge



const percent_calculator = function(result_array)
{
    
    let len = result_array.length;
    let half=parseInt(len/2);//9/2=4

    for (let i = 0; i < half; i++)
    {
        let total=(result_array[i]+result_array[len-i-1]);
        // console.log("i"+result_array[i]);
        // console.log("len-i-1"+result_array[len-i-1]);
        // console.log(total);
        if (total<10)
        {
            intermediate_array.push(total);
        }
        else
        {
            let string=total.toString();
            // console.log(string.split('').map(Number));
            intermediate_array=intermediate_array.concat(string.split('').map(Number));     
            // console.log("Multiple");
        }
    }
    if (len%2===1)
    {
        intermediate_array.push(result_array[half]);
    }
    console.log(intermediate_array);
}



let intermediate_array = [];
percent_calculator([3,1,2,2,1,3,1]);//percent:4432
intermediate_array = [];
percent_calculator([9,1,2,2,1,3,9]);//percent:18432
