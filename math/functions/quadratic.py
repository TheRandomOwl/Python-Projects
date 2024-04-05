# Calculates the solution to the quadratic formula
import math
try:
    A = float(input("Enter a number for A: "))
    B = float(input("Enter a number for B: "))
    C = float(input("Enter a number for C: "))
except ValueError:
    print("Invalid input")
else:
    ans1 = (-B + math.sqrt(B*B - 4*A*C)) / 2*A
    ans2 = (-B - math.sqrt(B*B - 4*A*C)) / 2*A
    print(f"{ans1}, {ans2}")