function buy(){
    if (document.getElementById("buyStock").style.display == "none"){
        document.getElementById("buyStock").style.display = "block";
        document.getElementById("sellbutton").style.visibility = "hidden";
        document.getElementById("skipbutton").style.visibility = "hidden";
        document.getElementById("portfolioButton").style.visibility = "hidden";
    }
    else {
        document.getElementById("buyStock").style.display = "none";
        document.getElementById("sellbutton").style.visibility = "visible";
        document.getElementById("skipbutton").style.visibility = "visible";
        document.getElementById("portfolioButton").style.visibility = "visible";
    }
}

function sell(){
    if (document.getElementById("sellStock").style.display == "none"){
        document.getElementById("sellStock").style.display = "block";
        document.getElementById("buybutton").style.visibility = "hidden";
        document.getElementById("skipbutton").style.visibility = "hidden";
        document.getElementById("portfolioButton").style.visibility = "hidden";
    }
    else{
        document.getElementById("sellStock").style.display = "none";
        document.getElementById("buybutton").style.visibility = "visible";
        document.getElementById("skipbutton").style.visibility = "visible";
        document.getElementById("portfolioButton").style.visibility = "visible";
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