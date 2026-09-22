import sys

sys.argv = ["append_it.py", "parallel", "egoism", "human", "alcohol"]

parameters = sys.argv[1:]

if len(parameters) == 0:
    print("none")
else:
    for parameter in parameters:
        if parameter.endswith("ism"):
            continue
        print(parameter + "ism")
