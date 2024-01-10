#!/usr/bin/node

function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

if (process.argv[2]) {
  const firstNum = Number(process.argv[2]);
  if (firstNum.isNaN) {
    console.log('NAN');
  } else {
    const result = factorial(firstNum);
    console.log(`${result}`);
  }
} else {
  console.log(1);
}
