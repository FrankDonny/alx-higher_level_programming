#!/usr/bin/node
const args = process.argv;
function factorial (num) {
  let fact;
  if (num === 0) {
    return (fact);
  } else {
    fact = num * factorial(num - 1);
  }
}