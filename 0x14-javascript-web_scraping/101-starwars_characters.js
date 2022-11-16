#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
const url = `https://swapi-api.hbtn.io/api/films/${args[0]}`;
request(url, async function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const obj = JSON.parse(body);
    for (const charURL of obj.characters) {
      await new Promise((resolve, reject) => {
        request(charURL, (err, r, body) => {
          if (err) {
            reject(err);
          } else {
            console.log(JSON.parse(body).name);
            resolve();
          }
        });
      });
    }
  //   const chars = obj.characters;
  //   const arr = []
  //   for (const char in chars) {
  //     arr.push(chars[char]);
  //   }
  //   for (let ele = 0; ele < arr.length; ele++) {
  //     request(arr[ele], function (err, res, body) {
  //       if (err) { console.log(err); }
  //       const name = JSON.parse(body);
  //       console.log(name.name);
  //     }
  //     );
  //   }
  //   // console.log(arr)
  }
});
