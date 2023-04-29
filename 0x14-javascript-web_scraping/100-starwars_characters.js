#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = `https://swapi.dev/api/films/${id}/`;

request.get(url, (err, res, content) => {
  if (err) {
    console.log(err);
    return;
  }

  const data = JSON.parse(content);
  const chars = data.characters;
  for (const cha of chars) {
    request(cha, (err, res, content) => {
      if (err) {
        console.log(err);
        return;
      }
      const char_data = JSON.parse(content);
      console.log(char_data.name);
    });
  }
});
