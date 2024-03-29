#!/usr/bin/node
// prints a square of size x

let i;
const firstArg = process.argv[2];
const size = parseInt(firstArg);
if (isNaN(size)) {
  console.log('Missing size');
}

for (i = 0; i < size; i++) {
  console.log('X'.repeat(size));
}

/*
#!/usr/bin/node

let i, j;
const firstArg = process.argv[2];
const size = parseInt(firstArg);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (i = 0; i < size; i++) {
    let row = '';
    for (j = 0; j < size; j++) {
      row += 'x';
    }
    console.log(row);
  }
}
*/
