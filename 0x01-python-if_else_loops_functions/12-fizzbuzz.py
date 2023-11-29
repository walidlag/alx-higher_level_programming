#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if q % 15 == 0:
            print("FizzBuzz", end=" ")
        elif q % 3 == 0:
            print("Fizz", end=" ")
        elif q % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(q, end=" ")
