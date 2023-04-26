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
	console.log("File written successfully\n");

      if (err) {
        console.log(err);
      }
    });
  }
});
