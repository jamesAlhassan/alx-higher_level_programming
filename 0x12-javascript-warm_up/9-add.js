#!/usr/bin/node

const arg = process.argv.slice(2);
const firstArg = arg[0];
const secondArg = arg[1];


function add(a, b){
return (a + b);
}

console.log(add(parseInt(firstArg), parseInt(secondArg)));
