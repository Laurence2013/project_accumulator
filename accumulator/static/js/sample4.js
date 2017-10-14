function Employee(name, age, postcode) {
  this.name = name;
  this.age = age;
  this.postcode = postcode;

  this.getInfo = function() {
    return 'My name is ' + this.name + ' and I am ' + this.age + ' and my post code is ' + this.postcode;
  }
}

var emp = new Employee('Carl', 42, 'wv88ph');
console.log(emp.getInfo())

Employee.prototype.job = emp.job = 'Javascript programmer';
Employee.prototype.empInfo = function() {
  return ' and my job is a ' + this.job;
}

console.log('1.) ',emp.getInfo() + emp.empInfo());
console.log('2.) ',emp.getInfo());

var empDave = new Employee('Dave', 24, 'wv115ph');
empDave.job = 'SQl developer';
console.log('3.) ',empDave.getInfo() + empDave.empInfo());

var empList = [emp, empDave];
console.log(empList.length);
console.dir(empList);

for (var prop in empList){
  console.log(empList[prop]);
}
