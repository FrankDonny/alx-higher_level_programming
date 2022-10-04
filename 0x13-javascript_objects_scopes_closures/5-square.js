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

  rotate () {
    for (let i = 0; i < this.width; i++) {
      console.log('X'.repeat(this.height));
    }
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
    for (let i = 0; i < (this.height); i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }
}
module.exports = Square;
