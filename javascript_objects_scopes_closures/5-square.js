#!/usr/bin/node

class Rectangle {
    constructor(w, h) {
      if (w <= 0 || h <= 0) {
      } else {
        this.width = w;
        this.height = h;
      }
    }
  
    print() {
        if (!this.width || !this.height){

        }else{
            let str = '';
            for (let i = 0; i < this.height; i++) {
            for (let j = 0; j < this.width; j++) {
                str += 'X';
            }
            console.log(str);
            str = '';
            }
        }
    }
  
    rotate() {
      if (!this.width || !this.height) {
      } else {
        [this.width, this.height] = [this.height, this.width];
      }
    }
  
    double() {
      if (!this.width || !this.height) {
      } else {
        this.width *= 2;
        this.height *= 2;
      }
    }
}
  

class Square extends Rectangle {
    constructor(size) {
      super(size, size);
    }
  }
  
module.exports = Square;