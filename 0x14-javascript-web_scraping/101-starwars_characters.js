#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = `https://swapi.dev/api/films/${id}/`;
let characters = [];
