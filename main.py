import matplotlib.pyplot as plt
from numpy import linspace
from sympy import symbols, simplify
from math import *

# Prompt the user to input the number of points (n)
n = int(input("n: ")) 
point = []  # List to store x-coordinates of the points
y_point = []  # List to store y-coordinates of the points
fxlx = []  # List to store terms of the Lagrange polynomial

# Loop to input the x-coordinates
for i in range(n+1):
    xi = input(f"x{i}: ")  
    point.append(eval(xi)) 

# Input the function to interpolate    
func = input("f: ")

# Calculate y-coordinates based on the input function
for i in range(n+1):
    x = point[i]
    result = eval(func, {"cos": cos, "sin": sin, "tan": tan, "pi": pi, "x": x, "sqrt": sqrt, "log": log, "log10": log10}) 
    y_point.append(result)

x = symbols("x")

# Function to compute Lagrange interpolating polynomial
def lagrange_interpolated():
    px = 0
    
    for i in range(n+1):
        fx = y_point[i]
        for j in range(n+1):
            if i != j:
                fx *= (x - point[j]) / (point[i] - point[j])
               
        fxlx.append(fx)
        px += fx

    return simplify(px)

# Function to plot the interpolated polynomial
def picture_px():
    x_values = linspace(min(point), max(point), 500)
    y_values = [eval(str(interpolated), {"cos": cos, "sin": sin, "tan": tan, "pi": pi, "x": x, "sqrt": sqrt, "log": log, "log10": log10}) for x in x_values]

    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, label="Interpolated Polynomial")
    plt.scatter(point, y_point, color="red", label="Interpolation Points")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Lagrange Interpolation Polynomial")
    plt.legend()
    plt.grid(True)
    plt.show()

# Function to plot the absolute difference between interpolated polynomial and original function
def picture_px_fx():
    x_values = linspace(min(point), max(point), 500)
    y_values = [abs(eval((str(interpolated - eval(func, {"cos": cos, "sin": sin, "tan": tan, "pi": pi, "x": x, "sqrt": sqrt, "log": log, "log10": log10}))), {"cos": cos, "sin": sin, "tan": tan, "pi": pi, "x": x, "sqrt": sqrt, "log": log, "log10": log10}))  for x in x_values]
    y_point_abs = [abs(eval((str(interpolated - eval(func, {"cos": cos, "sin": sin, "tan": tan, "pi": pi, "x": x, "sqrt": sqrt, "log": log, "log10": log10}))), {"cos": cos, "sin": sin, "tan": tan, "pi": pi, "x": x, "sqrt": sqrt, "log": log, "log10": log10}))  for x in point]

    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, color="green", label="|p(x) - f(x)|")
    plt.scatter(point, y_point_abs, color="red", label="x")
    plt.xlabel("x")
    plt.ylabel("|p(x) - f(x)|")
    plt.title("|p(x) - f(x)|")
    plt.legend()
    plt.grid(True)
    plt.show()
    
interpolated = lagrange_interpolated() 
print(f"p(x) = {interpolated}")

# Check for potential division by zero errors in the polynomial representation
while True:
    if "zoo" in str(interpolated):
        print("ZeroDivisionError")
        break
    else:
        print(f"|p(x) - f(x)| = |{interpolated} - {func}|")
        
    picture_px()
    picture_px_fx()
    break