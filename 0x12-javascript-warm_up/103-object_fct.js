#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12,
};
console.log(myObject);

function incr () {
  incr = function () {
    myObject.value = myObject.value + 1;
  };
  myObject.func = incr;
}

incr();

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
