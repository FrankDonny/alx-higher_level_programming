#!/usr/bin/node
const fs = require('fs');
const args = process.argv.slice(2);
const file = args[0];
fs.readFile(file, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
