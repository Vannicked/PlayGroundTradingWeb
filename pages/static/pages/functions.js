function buy(){
    document.getElementById("buyStock").style.visibility = "visible";
    document.getElementsByClassName("turnOptions").style.visibility = "hidden";
}

function sell(){
    document.getElementById("sellStock").style.visibility = "visible";
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