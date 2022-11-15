#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
const url = args[0];

request(url, function (err, res, body) {
  if (err) { console.log(err); } else {
    const obj = JSON.parse(body);
    const object = {};
    let count = 0;
    for (let num = 1; num < 5; num++) {
      // console.log(typeof (obj[0]['completed']));
      if (obj.userId === num && obj.completed === false) {
        count++;
      }
      object[`${num}`] = count;
    }
    console.log(object);
  }
});
