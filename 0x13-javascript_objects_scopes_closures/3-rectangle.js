#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w < 1 || h < 1) || (w === undefined || h === undefined)) {
      /* pass */
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
