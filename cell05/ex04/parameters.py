import sys
sys.argv = ["this", "is", "crazy"]  

number_of_parameters = len(sys.argv) - 1
print("Number of parameters: " + str(number_of_parameters) + ".")
