#!/usr/bin/node
// prints the second biggest number

const args = process.argv;

if (args.length <= 3) {
  console.log(0);
} else {
  let max = Math.floor(Number(args[2]));
  let second = 0;

  for (let i = 3; i < args.length; i++) {
    const num = Math.floor(Number(args[i]));

    if (num > max) {
      second = max;
      max = num;
    } else if (num > second && num !== max) {
      second = num;
    }
  }

  console.log(second);
}
