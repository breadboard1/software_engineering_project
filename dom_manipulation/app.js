// alert("Hello World");

// console.log(document.getElementsByTagName("h1"));

//html selector
var title = document.getElementById("title");
console.log(title);

var child = document.getElementsByClassName("child");
// console.log(child);  
console.log(child[0]);  

//query selector, query selector all ---> another selector
//check w3school

//style
var newTitle = document.getElementById("title").style.color="red";
document.getElementById("title").style.removeProperty("color");

