#!/usr/bin/node

function add (a, b) {
  return parseInt(a) + parseInt(b);
}

res = add(process.argv[2], process.argv[3]);
console.log(res);
