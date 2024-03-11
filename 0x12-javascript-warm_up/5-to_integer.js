#!/usr/bin/node

const [, arg] = process.argv;

const num = parseInt(arg);

// Check if the parsed number
if (!isNaN(num)) {
    console.log(`My number: ${num}`);
} else {
    console.log('Not a number');
}
