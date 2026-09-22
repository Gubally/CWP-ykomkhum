import sys

sys.argv = ["Just me", "Dont judge me"]

if len(sys.argv) == 2:
    print(sys.argv[1].lower())
else:
    print("none")
