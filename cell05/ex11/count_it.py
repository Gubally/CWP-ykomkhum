import sys

sys.argv = ["count_it.py", "My", "Name", "Is", "Ball"]

parameters = sys.argv[1:]

if len(parameters) == 0:
    print("none")
else:
    print("parameters: " + str(len(parameters)))
    for parameter in parameters:
        print(parameter + ": " + str(len(parameter)))
