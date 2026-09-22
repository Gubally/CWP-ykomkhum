#!/usr/bin/python3

number = input("Enter a number\n")
number = int(number)

for i in range(10):
    print(str(i) + " x " + str(number) + " = " + str(i * number))
