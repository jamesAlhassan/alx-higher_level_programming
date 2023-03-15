#!/usr/bin/node




const list = require('./100-data.js').list;

const myList = list.map((v, i) => v * i);
console.log(list);
console.log(myList);
