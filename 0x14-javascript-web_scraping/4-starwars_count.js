#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
const url = args[0];
request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    let count = 0;
    const obj = JSON.parse(body);
    for (const item of obj.results) {
      for (const charItem of item.characters) {
        if (charItem.includes(18)) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
