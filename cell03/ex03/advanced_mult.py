#!/usr/bin/python3

import sys

if len(sys.argv) > 1:
    print("none")
else:
    table = 0
    while table <= 10:
        line = "Table de " + str(table) + ":"
        multiplier = 0
        while multiplier <= 10:
            line = line + " " + str(table * multiplier)
            multiplier = multiplier + 1
        print(line)
        table = table + 1
