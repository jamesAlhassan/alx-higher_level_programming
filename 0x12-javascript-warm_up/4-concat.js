#!/usr/bin/node

const arg = process.argv.slice(2);
const a = arg[0];
const b = arg[1];

if (a && b === undefined) {
  console.log(`${a} is ${b}`);
} else if (b === undefined) {
  console.log(`${a} is ${b}`);
} else {
  console.log(`${a} is ${b}`);
}
