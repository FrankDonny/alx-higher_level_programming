#!/usr/bin/node
const args = process.argv;
const fs = require('fs');
const data1 = fs.readFileSync(args[2], 'utf8');
const data2 = fs.readFileSync(args[3], 'utf8');
fs.writeFileSync(args[4], data1 + data2);
