#!/usr/bin/node

function add (a, b) {
  return parseInt(a) + parseInt(b);
}
let res = 0;
res = add(process.argv[2], process.argv[3]);
console.log(res);
