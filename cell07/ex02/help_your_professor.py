#!/usr/bin/python3   

def average(students):
    scores = list(students.values())
    return sum(scores) / len(scores)

class_3B = {
    "marine": 15,
    "jean": 15,
    "coline": 15,
    "luc": 1
}
class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")
