
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
  const characters = data.characters;
  characters.forEach((character) => {
  request(character, (err, res, content) => {
    if (err) {
      console.log(err);
      return;
    }
    const data = JSON.parse(content);
    console.log(data.name);
  });
});
});
