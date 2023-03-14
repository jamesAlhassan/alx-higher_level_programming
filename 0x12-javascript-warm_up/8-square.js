#!/usr/bin/node

const arg = process.agrv.slice(2);
const firstArg = parseInt(arg[0]);
let i, j;

if (isNaN(firstArg)) {
  console.log('Missing size');
} else {
  for (i = 0; i < firstArg; i++) {
    let x = '';

    for (j = 0; j < firstArg; j++) {
      x += 'X';
    }
    console.log(x);
  }
}
