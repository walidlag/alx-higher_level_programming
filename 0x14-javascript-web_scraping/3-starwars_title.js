#!/usr/bin/node
// Script that prints the title of a Star Wars movie where the episode number matches a given integer

const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api/films/';
const episodeNum = process.argv[2];

request.get(API_URL + episodeNum, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  if (res.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log('Error code: ' + res.statusCode);
  }
});
