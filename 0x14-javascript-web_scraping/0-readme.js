#!/usr/bin/node

const fs = require('fs');
const arg = process.argv[2];

fs.readFile(arg, 'utf-8', function (err, data) {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
