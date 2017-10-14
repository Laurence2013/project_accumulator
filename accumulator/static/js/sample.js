var yourName = prompt('What is your name?');

if (yourName != null) {
  document.getElementById('sayHello').innerHTML = 'Hello ' + yourName;
} else {
  document.getElementById('sayHello').innerHTML = 'Twat did not enter a name';
}

var obj = {firstName:'Laurence', lastName:'Mitchell'};

console.log(obj.firstName);


function myFunction(num1, num2) {
  return num1 * num2;
}

document.getElementById('numVal').innerHTML = '<b>total is ' + myFunction(4,4) + '</b>'

var car = {make:'Vauxhall', model:'Astra', engine:'1.9'};
console.log(car)
console.log(car.engine)
document.getElementById('carType').innerHTML = 'My car is a ' + car.make + ' ' + car.model;

console.dir(car);


function myFunc(obj){
  obj.engine = '2.0';
}

console.log(car.engine);

myFunc(car);
c = car.engine;
console.log(c)


for (i = 0; i < 10; i++) {
  console.log(i);
  if (i == 5){
    console.log('High Five!!');
  }
}

// console.log('Max num = ', Number.MAX_VALUE);
// console.log('Min num = ', Number.MIN_VALUE);
//
// var x = 100 / 'Apple';
// var xx = 100 / '10';
// console.log(x);
// console.log(xx);
//
// count = 0;
//
// while (count <= 10) {
//   console.log(count);
//   count++;
// }
//
// count1 = 0;
//
// while (count1 <= 10) {
//   console.log(count1)
//   if (count1 == 5) {
//     console.log('The number I want is ',count1);
//   }
//   console.log(count1);
//   count1++;
// }
