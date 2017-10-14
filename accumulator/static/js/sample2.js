var customer = {
  name: 'Laurence Mitchell',

  speak: function() {
    return 'My name is ' + this.name;
  },

  address: {
    Street: 'Wolverhampton New Cross Street',
    City: 'Wolverhampton',
    County: 'West Midlands'
  }
};
//
// console.log(customer.speak());
// console.log(customer.address);
// console.log(customer.address.Street);
//
// customer.address.Country = 'United Kingdom';
// console.log(customer.address);
// console.log(customer.address.Country);

function Person(firstName, lastName) {
  this.fname = firstName;
  this.lname = lastName;

  this.name = function() {
    return 'My first name is ' + this.fname + ' and my last name is ' + this.lname;
  }
}

var myName = new Person('Laurence','Mitchell');
console.log(myName.name());
console.log(myName instanceof Person);

function changeName(person){
  person.name = 'Lorenzo Mitchell';
}

changeName(myName);
console.log('My new name is ' + myName.name);



function getSum(num1, num2) {
  return num1 + num2;
}

console.log('Number of arguments ' + getSum.length);
