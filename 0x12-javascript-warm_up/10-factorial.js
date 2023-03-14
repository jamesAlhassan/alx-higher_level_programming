#!/usr/bin/node

function factorial (n) {
  if (n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const a = process.argv[2];
if (isNaN(a)) {
  console.log(1);
} else {
  console.log(factorial(a));
}
