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

var img = document.getElementById("img");
// console.log(img.getAttribute("src"));
img.setAttribute("alt", "picture");
// console.log(img.getAttribute("alt"));

img.classList.add("testClass");  //what it is doning?
console.log(img);

var hero = document.getElementById("hero");
console.log(hero.innerText);

var input = document.getElementById("input");
// var input = document.getElementById("input").value; //works similarly
console.log(input.value);

var parent = document.getElementById("parent").innerHTML;
console.log(parent);

var testDiv = document.getElementsByClassName("test");
console.log(testDiv[0].childNodes[5]);
//parent node also accessable child ---> html tag e jawa possible!
// console.log(testDiv[0].childNodes[5].parentNode.parentNode); 

//create and append
var newDiv = document.getElementById("newDiv");
var p = document.createElement("p");
p.innerText = "New Created!";
newDiv.appendChild(p);

//function is also helpful for creating an element

document.getElementById("submit-btn").addEventListener("click", function(e){
    // console.log("yess boss");
    var inputValue = document.getElementById("input").value;
    console.log(inputValue);
});

document.getElementById("input").addEventListener("blur", function(e){
    console.log(e.target.value);
});
//only function can do it !!!