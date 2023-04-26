#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const characterId = '18';
let count = 0;

request.get(url, (error, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    data.results.map((result) => {
      result.characters.map((character) => {
        if (character.includes(characterId)) {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});
