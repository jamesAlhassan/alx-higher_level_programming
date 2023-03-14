#!/usr/bin/node
const arg = process.argv.slice(2);
const firstArg = parseInt(arg[0]);

if (isNaN(firstArg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < firstArg; i++) {
    let y = 0;
    let myVar = '';

    while (y < firstArg) {
      myVar += 'X';
      y++;
    }
    console.log(myVar);
  }
}
