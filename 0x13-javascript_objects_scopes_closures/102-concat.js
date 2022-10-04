#!/usr/bin/node
const args = process.argv;
const fs = require('fs');

fs.readFile(args[2], 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  }
  fs.writeFile(args[4], data, err => {
    if (err) {
      console.log(err);
    }
  });
  fs.readFile(args[3], 'utf8', (err, data1) => {
    if (err) {
      console.log(err);
    }
    fs.appendFile(args[4], '\n' + data1 + '\n', err => {
      if (err) {
        console.log(err);
      }
    });
  });
});
