#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
const url = `https://swapi-api.hbtn.io/api/films/${args[0]}`;
request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const obj = JSON.parse(body);
    const chars = obj.characters;
    for (const char of chars) {
      request(char, function (err, res, body) {
        if (err) { console.log(err); }
        const name = JSON.parse(body);
        console.log(name.name);
      }
      );
    }
  }
});
