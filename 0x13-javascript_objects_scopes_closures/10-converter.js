#!/usr/bin/node
exports.converter = function (base) {
  return  function (num) {
    if (base === 10) {
      return num;
    } else if (base === 16) {
      num = num / 16
    }
  }
}













