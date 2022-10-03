#!/usr/bin/node
const args = process.argv;
function add (a, b) {
  console.log(a + b);
}

if ((args.length - 2) < 2) {
  console.log('NaN');
} else {
  add(parseInt(args[2]), parseInt(args[3]));
}
