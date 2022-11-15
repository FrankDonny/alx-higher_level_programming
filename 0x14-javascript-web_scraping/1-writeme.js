#!/usr/bin/node

const fs = require('fs');

const args = process.argv.slice(2);
const file = args[0];
const content = args[1];

fs.writeFile(file, content, 'utf-8', err => {
  if (err) {
    console.log(err);
  }
});
