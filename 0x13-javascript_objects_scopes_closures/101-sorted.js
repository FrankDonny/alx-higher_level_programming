let dict = require('./101-data').dict

newDict = {};
li = [];
for (let key in dict) {

  // if (newDict[dict[key]].includes(dict[key])) {
  //   newDict[key].push(dict[key]);
  // } else {
    newDict[dict[key]] = key;
  // }
}

console.log(newDict);