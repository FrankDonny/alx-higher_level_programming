#!/usr/bin/node
const args = process.argv;
if ((args.length - 2) < 2) {
  console.log(0);
} else {
  args.shift();
  args.shift();
  const arg = [];
  for (let i = 0; i < args.length; i++) {
    arg.push(Number(args[i]));
  }
  arg.sort((x, y) => y - x);
  console.log(arg[1]);
}
