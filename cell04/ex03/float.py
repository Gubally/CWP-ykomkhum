#!/usr/bin/python3

number = input("Give me a number: ")
number = float(number)

if number % 1 == 0:
    print("This number is an integer.")
else:
    print("This number is a decimal.")
