#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);
const url = args[0];
request(url, function (err, res, body) {
  if (err) {
    console.log(`code: ${err}`);
  } else {
    console.log(`code: ${res.statusCode}`);
  }
});
