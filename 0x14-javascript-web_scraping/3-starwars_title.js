#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);
const url = `https://swapi-api.hbtn.io/api/films/${args[0]}`;
request(url, function (err, res, body) {
  if (err) {
    console.log(`code: ${err}`);
  } else {
    const obj = JSON.parse(body);
    console.log(obj.title);
  }
});
