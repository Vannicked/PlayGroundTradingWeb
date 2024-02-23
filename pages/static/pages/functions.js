function buy(){
    let stock = prompt("What stock do you want to buy?", "NVIDIA");
    let text = "blank";
    if (stock == null || stock == ""){
        text = "No stock entered.";
    }
    else{
        text = "You have purchased " + stock + ".";
    }
    console.log(text);
}

function sell(){
    let stock = prompt("What stock do you want to sell?", "NVIDIA");
    let text = "blank";
    if (stock == null || stock == ""){
        text = "No stock entered.";
    }
    else{
        text = "You have sold " + stock + ".";
    }
    console.log(text);
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