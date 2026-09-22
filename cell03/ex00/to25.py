#!/usr/bin/python3

number = input("Enter a number less than 25\n")
number = int(number)

if number > 25:
    print("Error")
else:
    while number <= 25:
        print("Inside the loop, my variable is " + str(number))
        number = number + 1
