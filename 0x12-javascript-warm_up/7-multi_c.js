#!/usr/bin/node

const arg = process.argv.slice(2);
const firstArg = parseInt(arg[0]);
let i;

if (isNaN(firstArg)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < firstArg; i++) {
    console.log('C is fun');
  }
}
