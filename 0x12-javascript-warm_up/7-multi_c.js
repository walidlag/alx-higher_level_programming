#!/usr/bin/node

const [, arg] = process.argv;
let output = '';

if (Number.isNaN(Number(arg))) {
  console.log('Missing number of occurrences');
} else {
  let x = Number(arg);
  while (x > 0) {
    output += 'C is fun\n';
    x--;
  }
  console.log(output);
}
