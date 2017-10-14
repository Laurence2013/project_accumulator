import {name} from './js/sample6.js';

connsole.log(name);

function inherits(actor, superActor){
  actor.super_ = superActor;
  actor.prototype = Object.create(superActor.prototype, {
    constructor: {
      value: actor,
      enumerable: false,
      writable: true,
      configurable: true
    }
  });
}

var Person = function(fname){
  this.fname = fname
};

Person.prototype.getName = function(){
  console.log('Hi! My name is ' + this.fname);
}

Person.prototype.shoutName = function(){
  console.log('Hi! My name is ' + this.fname + '!');
}

var mark = new Person('Mark');
var carl = new Person('Carl');

mark.getName();
carl.getName();

mark.fname = 'Marcus';
mark.shoutName();

var Musician = function(name, instrument){
  Musician.super_.call(this, name);
  this.instrument = instrument;
}

inherits(Musician, Person);

Musician.prototype.shoutInstrument = function(){
  console.log('and I play ' + this.instrument);
}

var julia = new Musician('Julia','Guitar');
julia.shoutName();
julia.shoutInstrument();
