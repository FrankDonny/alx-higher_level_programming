#!/usr/bin/node
const args = process.argv;
function factorial (num) {
  let fact;
  if (num === 1) {
    return (num);
  } else {
    fact = num * factorial(num - 1);
    return fact;
  }
}

if (args.length - 2 === 0) {
  console.log(1);
} else {
  const num = factorial(args[2]);
  console.log(num);
}
