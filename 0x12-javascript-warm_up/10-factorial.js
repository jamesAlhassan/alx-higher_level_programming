#!/usr/bin/node


function factorial (n) {
  return n === 0 || if(isNaN(n)){
  return 1} else {
  return n * factorial(n - 1);
  }
}

console.log(factorial(Number(process.argv[2])));
