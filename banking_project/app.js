function handleDeposit(){
    var inputValue = getValue("deposit-input", "value");
    var depositAmount = getValue("deposit-amount", "innerText");
    var sum = inputValue + depositAmount;
    setInnerText("deposit-amount", sum);
    var totalAmount = getValue("total-amount", "innerText");
    var total = inputValue + totalAmount;
    setInnerText("total-amount", total);
    document.getElementById("deposit-input").value = "";
}

function handleWithdraw(){
    var inputValue = getValue("withdraw-input", "value");
    var withdrawAmount = getValue("withdraw-amount", "innerText");
    var sum = inputValue + withdrawAmount;
    setInnerText("withdraw-amount", sum);
    var totalAmount = getValue("total-amount", "innerText");
    var total = totalAmount - inputValue;
    setInnerText("total-amount", total);
    document.getElementById("withdraw-input").value = "";
}

function getValue(id, key){
    if(key == "innerText"){
        var value = document.getElementById(id).innerText;
        return parseFloat(value);
    }
    if(key == "value"){
        var value = document.getElementById(id).value;
        return parseFloat(value);
    }
}

function setInnerText(id, value){
    document.getElementById(id).innerText = value;
}