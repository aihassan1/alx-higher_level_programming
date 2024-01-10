#!/usr/bin/node
const firstNum = parseInt(process.argv[2]);
const secondNum = parseInt(process.argv[3]);

function add (a, b) {
  return a + b;
}

if (isNaN(firstNum) || isNaN(secondNum)) {
  console.log(NaN);
} else {
  const result = add(firstNum, secondNum);
  console.log(`${result}`);
}
