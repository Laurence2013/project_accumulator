export default 'sample6!'

export var name = 'Lozza'

function Employee(name, age, postcode) {
  this.name = name;
  this.age = age;
  this.postcode = postcode;

  this.info = function() {
    return 'My name is ' + this.name + ', I am ' + this.age + ' and my postcode is ' + this.postcode;
  }
}

var empDave = new Employee('Dave', '42', 'wv123ph');
console.log(empDave.info());
console.dir(empDave);

var empCarl = new Employee('Carl', '23', 'wv456ph');
console.log(empCarl.info());
console.dir(empCarl);

Employee.prototype.job = 'Javascript programmer';
Employee.prototype.jobInfo = function() {
  return 'and I am a ' + this.job;
}
console.log(empDave.name);
console.log(empDave.jobInfo());

Employee.prototype.job = 'SQL programmer';
Employee.prototype.jobInfo = function() {
  return 'and I am a ' + this.job;
}
console.log(empCarl.name);
console.log(empCarl.jobInfo());
