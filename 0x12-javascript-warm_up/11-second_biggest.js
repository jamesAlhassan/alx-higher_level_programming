#!/usr/bin/node

function secondBiggest () {
  if (!arguments[0] || arguments[0].length <= 1) {
    return 0;
  }

  arguments[0].splice(arguments[0].indexOf(String(Math.max(...arguments[0]))), 1);
  return Math.max(...arguments[0]);
}

console.log(secondBiggest(process.argv.slice(2)));
