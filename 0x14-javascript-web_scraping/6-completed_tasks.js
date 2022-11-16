#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
const url = args[0];

request(url, function (err, res, body) {
  if (err) { console.log(err); } else {
    const completed = {};
  const jsonBody = JSON.parse(body);
  for (const task of jsonBody) {
    if (task.completed) {
      if (completed[task.userId]) {
        completed[task.userId]++;
      } else {
        completed[task.userId] = 1;
      }
    }
  }
  console.log(completed);
  }
});
