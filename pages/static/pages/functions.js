function buy(){
    if (document.getElementById("stockActionsForm").style.display == "none"){
        document.getElementById("stockActionsForm").style.display = "block";
        document.getElementById("sellbutton").style.visibility = "hidden";
        document.getElementById("skipbutton").style.visibility = "hidden";
        document.getElementById("portfolioButton").style.visibility = "hidden";
        document.getElementById("sell_stock").style.visibility = "hidden";
    }
    else {
        document.getElementById("stockActionsForm").style.display = "none";
        document.getElementById("sellbutton").style.visibility = "visible";
        document.getElementById("skipbutton").style.visibility = "visible";
        document.getElementById("portfolioButton").style.visibility = "visible";
        document.getElementById("sell_stock").style.visibility = "visible";
    }
}

function sell(){
    if (document.getElementById("stockActionsForm").style.display == "none"){
        document.getElementById("stockActionsForm").style.display = "block";
        document.getElementById("buybutton").style.visibility = "hidden";
        document.getElementById("skipbutton").style.visibility = "hidden";
        document.getElementById("portfolioButton").style.visibility = "hidden";
        document.getElementById("buy_stock").style.visibility = "hidden";
    }
    else{
        document.getElementById("stockActionsForm").style.display = "none";
        document.getElementById("buybutton").style.visibility = "visible";
        document.getElementById("skipbutton").style.visibility = "visible";
        document.getElementById("portfolioButton").style.visibility = "visible";
        document.getElementById("buy_stock").style.visibility = "visible";
    }
}

function skip(){
    let text = "blank";
    if (confirm("Are you sure you want to skip?")){
        text = "You have skipped";
    }
    else{
        text = "Please choose buy or sell";
    }
    console.log(text);
}

function portfolio(){

}