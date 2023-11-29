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
            return percent_calculator(intermediate_array);

        }

    }

}

const result_maker = function(first,third)
{
    let second="LOVES";
    let whole=(first.toUpperCase())+second+(third.toUpperCase());
    console.log("whole"+whole);
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
            }
        }
        result.push(cnt);  
    }
    return percent_calculator(result);
}

function button_press() 
{
    console.log("in calculateLove");
    var yourName = document.getElementById('yourName').value.trim();
    var partnerName = document.getElementById('partnerName').value.trim();
    if (yourName === "" || partnerName === "") {
        alert("Please enter both names.");
        return;
    }
    console.log(yourName);
    const output_result=result_maker(yourName, partnerName);  
    console.log("OUTPUT:"+output_result);     
    document.getElementById('result').innerText = output_result;
}

