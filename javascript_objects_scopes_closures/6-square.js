#!/usr/bin/node
const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint(c) {
    if (c === undefined) {
      c = "X";
    }
    let str = "";
    for (let i = 0; i < this.width; i++) {
      for (let j = 0; j < this.width; j++) {
        str += c;
      }
      str += "\n";
    }
    console.log(str);
  }
}

module.exports = Square;