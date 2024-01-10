#!/usr/bin/node
let first_arg = process.argv[2];

let number = parseInt(first_arg, 10);

// Check if the string is enclosed in single or double quotes

if (isNaN(number) || number.toString() != first_arg) {
  console.log('Not a number');
} else {
  console.log(`My number: ${number}`);
}
