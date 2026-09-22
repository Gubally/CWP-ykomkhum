
import sys
sys.argv = ["upcase_it.py", "This exercise is quite easy!"]

if len(sys.argv) == 2:
    print(sys.argv[1].upper())
else:
    print("none")
