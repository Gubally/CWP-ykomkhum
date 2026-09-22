#!/usr/bin/python3

first_number = input("Enter the first number:\n")
first_number = int(first_number)

second_number = input("Enter the second number:\n")
second_number = int(second_number)

result = first_number * second_number

print(str(first_number) + " x " + str(second_number) + " = " + str(result))

if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is zero.")
