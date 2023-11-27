// const prompt = require("prompt-sync")();
const percent_calculator = function(result_array)
{
    let len = result_array.length;
    let intermediate_array = [];
    if (len===1)
    {
        return result_array[0];
    }
    else 
    {
        if(len===2)
        {
            let test=result_array[0]*10+result_array[1];
            return test;
        }
        else
        {
            let half=parseInt(len/2);//9/2=4
            for (let i = 0; i < half; i++)
            {
                let total=(result_array[i]+result_array[len-i-1]);
                if (total<10)
                {
                    intermediate_array.push(total);
                }
                else
                {
                    let string=total.toString();
                    intermediate_array=intermediate_array.concat(string.split('').map(Number));     
                }
            }
            if (len%2===1)
            {
                intermediate_array.push(result_array[half]);
            }
            console.log(intermediate_array);
            return percent_calculator(intermediate_array);

        }

    }

}

const result_maker = function(first,third)
{
    console.log(first);
    let second="LOVES";
    let whole=(first.toUpperCase())+second+(third.toUpperCase());
    console.log(whole);
    let result=[];
    while(whole.length>0)
    {
        let key=whole[0];
        let cnt=0;
        for (let i=0; i<whole.length; i++)
        {
            if (whole[i]===key)
            {
                cnt=cnt+1;
                whole=(whole.slice(0,i))+(whole.slice(i+1));//BEST EXCEPT FOR LL OR REPEATION OF ALPHABETS IN ANY NAME OR ENFING WITH L OR STARTING WITH S
                // console.log("KEY:"+key+" WHOLE:"+whole);
            }
        }
        // console.log("net:"+key+cnt+"\n");   
        result.push(cnt);  

    }
    console.log(result);
    output.innerHTML=percent_calculator(result)
    // return percent_calculator(result)
}


const first_input=document.getElementById("101");
const third_input=document.getElementById("102");
const output=document.getElementById("301");
const button = document.getElementById("201");
button.addEventListener('click', function() {
    result_maker(first_input.value, third_input.value);
});
// output.innerHTML=result_maker(first_input,third_input); 


