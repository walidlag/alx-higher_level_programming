#!/usr/bin/node
// Script that prints the number of movies where the character “Wedge Antilles” is present

const request = require('request');
let movieCount = 0;

request(process.argv[2], function (err, res, body) {
  if (!err) {
    const results = JSON.parse(body).results;

    for (const movie of results) {
      const characters = movie.characters;

      if (characters.find(character => character.endsWith('/18/'))) {
        movieCount++;
      }
    }

    console.log(movieCount);
  } else {
    console.error(err);
  }
});
