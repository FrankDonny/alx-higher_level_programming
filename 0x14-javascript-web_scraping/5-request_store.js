#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const args = process.argv.slice(2);
const url = args[0];
const file = args[1];

request(url, function (err, res, body) {
  if (err) { console.log(err); } else {
    fs.writeFile(file, body, 'utf-8', err => {
      if (err) {
        console.log(err);
      }
    });
  }
});
