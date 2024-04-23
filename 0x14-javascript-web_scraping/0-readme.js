#!/usr/bin/node
// script that reads and prints the content of the file

const filesys = require('fs');
filesys.readFile(process.argv[2], 'utf8', function (err, content) {
  console.log(err || content);
});
