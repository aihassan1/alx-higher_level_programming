#!/usr/bin/node
// Write a script that prints x times “C is fun”

let i = 0;
const firstArg = process.argv[2];
const counts = parseInt(firstArg);
if (isNaN(counts)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < counts; i++) {
    console.log('C is fun');
  }
}
