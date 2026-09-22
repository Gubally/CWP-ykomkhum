import sys

sys.argv = ["aff_rev_params.py", "is", "name", "my"]

parameters = sys.argv[1:]

if len(parameters) < 2:
    print("none")
else:
    for parameter in parameters[::-1]:
        print(parameter)
