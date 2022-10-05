let dict = require('./101-data').dict
console.log(dict);

let newDict = {};
for (let key in dict) {
    for (let newKey in newDict) {
        if (dict[key] === newKey) {
            newDict[newKey].push(key);
        } else {
            newDict[dict[key]] = key;
        }
    }
}
// console.log(newDict[1])
console.log();
console.log(newDict);