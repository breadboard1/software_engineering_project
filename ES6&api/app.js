// var is functional scope declearation
// let and const is block scope declearation
// let is normal as cpp but const can't be changed within the programme 
// as like as cpp const
// multi line string { `` } use it 
// spread operator ---> ( ... )

const nam = `this is dynamic string`;
let name2 = `hello ${nam}`;
console.log(name2);

const num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const newArray = ["rahim", "karim", ...num];
console.log(newArray);
console.log(...num);   //without comma because of spread operator
console.log(Math.max(...num));   //spread operator is must

// arrow function silimar as lambda fuction in python or cpp
const res = (a) =>{
    return a;
};

console.log(res(100));


//array and object destructuring
const numbers = [1, 2, 3, 4, 7, 9, 10, 3];
const [a, b, c, d] = numbers;
console.log(a, b, c, d);

//object destructiong
const obj = {
    name: "emon",
    age: 20,
    friends: 3,
    github: "yes",
};

// const age = obj.age;
// const name = obj.name;
// to avoid above repetation
const {age, name} = obj;
console.log(age, name);

// nested Object
const test = [{
    name:"rahim",
    age: 14,
    friends : ["jobbar", "karim", "akbor"],
    github : "Yes",
}, {
    name:"mubarok",
    age: 24,
    friends : ["rofik", "boiati", "dj"],
    github : "No",
}, {
    name:"moshiur",
    age: 34,
    friends : ["rahman", "bokhtier", "kuddus"],
    github : "Yes",
}];

console.log(test[0]);

// map, filter, find methods ---> every methods return array
// map all element
// filter conditioned search and new array return
// find for single element searching
const nums = [2, 4, 5];
const newNums = nums.map(x => x*x);
console.log(newNums);

const products = [
    { id: 1, name: "Wireless Mouse", price: 29.99, color: "Black" },
    { id: 2,name: "Mechanical Keyboard",price: 89.99,color: "White" },
    { id: 3,name: "Bluetooth Headphones",price: 59.99,color: "Blue" },
    { id: 4,name: "4K Monitor",price: 399.99,color: "Silver" },
    { id: 5,name: "Laptop Stand",price: 34.99,color: "Gray" },
    { id: 6,name: "USB-C Hub",price: 49.99,color: "Space Gray" },
    { id: 7,name: "External SSD",price: 129.99,color: "Black" },
    { id: 8,name: "Smartwatch",price: 199.99,color: "Rose Gold" },
    { id: 9,name: "Portable Speaker",price: 79.99,color: "Red" },
    { id: 10,name: "Fitness Tracker",price: 49.99,color: "Green" }
];

const result = products.filter((product) => product.color != "Black");
console.log(result);

const result2 = products.find((product) => product.id == 2);
console.log(result2);

//many elements with same value than find returns the first element
// const result3 = products.find((product) => product.color == "Black");
// console.log(result3);

//for each method
const productContainer = document.getElementById("product-container");
const result3 = products.forEach((product) => {
    console.log(product);
    const h1 = document.createElement("h1");
    h1.innerText = product.name;
    productContainer.appendChild(h1);
});

//api
fetch("https://fakestoreapi.com/products/1")
.then((res) => res.json())
.then((data) =>{
    console.log(data);
});

// asyncronous behavior ---> serial break
// setTimeout() ---> this function can make asyncronous behavior
