console.log("Hello World");

var number = 10;
console.log(number);

var string = "I am a champion.";
console.log(string);

console.log(typeof string);
console.log(typeof number);

var num1 = 70.5;
var num2 = 50;
var res = parseInt(num1+num2);
console.log(res);

var n1 = 200;
var n2 = "100";
console.log(n1+parseInt(n2));

var n3 = "1000.555";
var n4 = 200;

console.log(parseFloat(n3)+n4);

var now = 11;
if(now > 10){
    console.log("Greater than 10");
}else if(now == 10){
    console.log("Equal");
}else{
    console.log("Less than 10");
}

// object
var person = {
    hands: 2,
    friends: 5,
    age: 35,
    school:{
        name: "bhober bati",
        location: "facebook",
    },
};

// console.log(person);
// console.log(Object.keys(person));
// console.log(Object.values(person));
// console.log(Object.entries(person));

// console.log(person.age);

console.log(person.school.name);

var friends = ["rahim", "jabbar", "karim"];
// console.log(friends[0]);
// console.log(friends.length);
friends.push("salam");
// console.log(friends);

friends.unshift("bokkor");  //push front
console.log(friends);
friends.shift();            //pop front
console.log(friends);

//array methods
// console.log(friends.reverse());
// console.log(friends.slice(2));
// console.log(friends.indexOf("rahim"));

//loop   ---> loop works on array?
// for(var i = 0; i < 10; i++){
//     console.log(i);
// }

for(var i = 0; i < friends.length; i++){
    console.log(friends[i]);
}
