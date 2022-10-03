#!/usr/bin/node
const args = process.argv;
args.shift();
args.shift();
if (!args[0]) {
  console.log('No argument');
} else {
  console.log(args[0]);
}
