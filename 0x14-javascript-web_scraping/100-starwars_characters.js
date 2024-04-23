#!/usr/bin/node

// Script to print all characters of a Star Wars movie based on Movie ID

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const content = JSON.parse(body);
    const characters = content.characters;
    // Extract list characters URLs from movie data
    for (const character of characters) {
      request.get(character, (err, response, body) => {
        if (err) {
          console.log(err);
        } else {
          // characters name from response body
          const names = JSON.parse(body);
          console.log(names.name);
        }
      });
    }
  }
});
