var nums = [1, 7, 2, 5, 9, 11, 15, 10];
nums.sort(function(a, b){
    return a-b;
});
// console.log(nums);

var friends = ["salam", "jobbar", "karim", "rahim", "alamotali"];
var len = 0;
var ans;
for(var i = 0; i < friends.length; i++){
    if(friends[i].length > len){
        ans = friends[i];
        len = friends[i].length;
    }
}
// console.log(ans);

//function
function add(a, b){
    return a+b;
}

console.log(add(2, 4));
