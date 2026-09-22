import sys

sys.argv = ["string_are_arrays.py", "a lot of aaaaa"]

if len(sys.argv) == 2:
    text = sys.argv[1]
    found = False
    for character in text:
        if character == "a":
            print("a")
            found = True
    if found == False:
        print("none")
else:
    print("none")
