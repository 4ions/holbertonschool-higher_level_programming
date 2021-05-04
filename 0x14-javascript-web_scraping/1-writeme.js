#!/usr/bin/node
const fs = require('fs');
const arg = process.argv[2];
const data = process.argv[3];

fs.appendFile(arg, data, 'utf-8', function (err) {
  if (err) throw err;
});
