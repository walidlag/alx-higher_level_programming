#!/usr/bin/node

const [, , ...args] = process.argv;

/* script that prints a message */
switch (args.length) {
  case 0:
    console.log('No argument');
    break;
  case 1:
    console.log('Argument found');
    break;
  default:
    console.log('Arguments found');
}
