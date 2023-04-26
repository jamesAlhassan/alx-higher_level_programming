#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const id = '18';
let count = 0;

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    data.results.map((result) => {
      result.characters.map((character) => {
        if (character.includes(id)) {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});
