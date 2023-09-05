// No default
var mon = prompt("Input Month:");
switch(mon){
    case "Feb": console.log("Month with 28/29 days.");
    case "Apr":
    case "Jun":    
    case "Sep":
    case "Nov":  console.log("Month with 30 days.");   
    default: console.log("Month with 31 days.");   

}



