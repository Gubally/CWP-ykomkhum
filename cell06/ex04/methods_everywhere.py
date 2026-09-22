import sys

def shrink(text):
    print(text[:8])

def enlarge(text):
    while len(text) < 8:
        text = text + "."
    print(text)

sys.argv = ["methods_everywhere.py", "lol", "physically", "backpack"]

parameters = sys.argv[1:]

if len(parameters) < 1:
    print("none")
else:
    for parameter in parameters:
        if len(parameter) > 8:
            shrink(parameter)
        elif len(parameter) < 8:
            enlarge(parameter)
        else:
            print(parameter)
