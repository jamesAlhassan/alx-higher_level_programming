#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = `https://swapi.dev/api/films/${id}/`;
let characters = [];

request(url, (err, res, content) => {
  if (err) {
    console.log(err);
    return;
  }

  const data = JSON.parse(content);
  characters = data.characters;
  getChar(0);
});

const getChar = (index) => {
  if (index === characters.length) {
    return;
  }

  request(characters[index], (err, res, content) => {
    if (err) {
      console.log(err);
      return;
    }
    const characterData = JSON.parse(content);
    console.log(characterData.name);
    getChar(index + 1);
  });
};
