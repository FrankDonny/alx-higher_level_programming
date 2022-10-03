#!/usr/bin/node
const args = process.argv;
if ((args.length - 2) === 0 || !parseInt(args[2])) {
  console.log('Missing size');
} else if (args[2] < 0) {
  // empty
} else {
  for (let i = 1; i <= args[2]; i++) {
    console.log('X'.repeat(args[2]));
  }
}
