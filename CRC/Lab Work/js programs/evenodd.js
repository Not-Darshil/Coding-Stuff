function handleClick() {
    const Num = document.querySelector("#num").value;
    let Ans = document.querySelector("#he");
    {
        if (Num % 2 === 0) {
            Ans.innerHTML = "Even"
        }
        else {
            Ans.innerHTML = "Odd"
        }
    }
}