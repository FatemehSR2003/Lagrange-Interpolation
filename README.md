# Lagrange-Interpolation
Implementing Lagrangian interpolation

▎Lagrange Interpolation

This repository contains a Python implementation of the Lagrange interpolation method. The code allows users to input a set of points and a function, then calculates and visualizes the interpolating polynomial along with the error between the polynomial and the original function.

▎Features

• Input a number of data points.

• Input a mathematical function for interpolation.

• Calculate the Lagrange interpolating polynomial.

• Visualize the polynomial and the original function.

• Display the error between the interpolating polynomial and the original function.

▎Requirements

Make sure you have the following libraries installed:

• matplotlib

• numpy

• sympy

You can install the required libraries using pip:

pip install matplotlib numpy sympy


▎Usage

1. Clone this repository to your local machine:

      git clone <repository_url>
   cd <repository_directory>
   

2. Run the script:

      python lagrange_interpolation.py
   

3. Follow the prompts to enter:

   • The number of points (n).

   • The x values for each point (e.g., x0, x1, ..., xn).

   • The function to interpolate (e.g., sin(x), cos(x), etc.).

4. The program will compute the Lagrange interpolation polynomial and display the results, including:

   • The interpolated polynomial.

   • A plot of the interpolated polynomial and original function.

   • A plot showing the error between the interpolated polynomial and original function.

▎Example

n: 3
x0: 0
x1: 1
x2: 2
x3: 3
f: sin(x)


▎Notes

• Ensure that the function you input is compatible with Python's syntax.

• The code handles basic mathematical functions like sin, cos, tan, sqrt, log, etc.

• If there is a division by zero during interpolation, an appropriate message will be displayed.

▎License

This project is licensed under the MIT License. See the LICENSE file for more details.

▎Acknowledgments

This implementation is based on the mathematical principles of Lagrange interpolation. For more information on this topic, you can refer to any standard numerical analysis textbook or online resources.

---

Feel free to contribute to this project by submitting issues or pull requests!
