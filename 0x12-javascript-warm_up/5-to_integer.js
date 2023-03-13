#!/usr/bin/node

const arg = process.argv.slice(2);
const firstArg = parseInt(arg[0]);

if (isNaN(firstArg)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${firstArg}`);
}
