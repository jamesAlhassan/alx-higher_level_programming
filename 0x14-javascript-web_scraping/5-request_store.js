#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];

request(url, (err, res, content) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(file, content, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
