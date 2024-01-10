#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  let i;
  let biggest = Number.MIN_SAFE_INTEGER;
  let secondBiggest;
  const numbers = [];

  for (i = 2; i < process.argv.length; i++) {
    const numb = Number(process.argv[i]);

    if (!isNaN(numb)) {
      numbers.push(numb);
    }
  }

  for (let j = 0; j < numbers.length; j++) {
    if (biggest < numbers[j]) {
      secondBiggest = biggest;
      biggest = numbers[j];
    } else if (secondBiggest === undefined || secondBiggest < numbers[j]) {
      secondBiggest = numbers[j];
    }
  }

  console.log(secondBiggest !== undefined ? secondBiggest : 0);
}
