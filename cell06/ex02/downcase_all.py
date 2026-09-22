import sys

def downcase_it(text):
    return text.lower()

sys.argv = ["downcase_all.py", "HELLO WORLD", "I understood Arrays well!"]

parameters = sys.argv[1:]

if len(parameters) == 0:
    print("none")
else:
    for parameter in parameters:
        print(downcase_it(parameter))
