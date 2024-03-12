#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = {};
for (const key in initDict) {
  if (newDict[initDict[key]] === undefined) {
    newDict[initDict[key]] = [];
  }
  newDict[initDict[key]].push(key);
}
console.log(newDict);
