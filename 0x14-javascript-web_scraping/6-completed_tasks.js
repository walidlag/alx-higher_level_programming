#!/usr/bin/node
// Script to compute the number of tasks completed by each user ID

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    let object = {};
    const tasks = JSON.parse(body);
    for (const a in tasks) {
      const task = tasks[a];
      if (task.completed === true) {
        if (object[task.userId] === undefined) {
          object[task.userId] = 1;
        } else {
          object[task.userId]++;
        }
      }
    }
    console.log(object);
  }
});
