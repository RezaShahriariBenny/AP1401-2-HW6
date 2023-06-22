# Question 1 : Explain the last two arguments and their application with examples.

'''
The First argument *args is used for giving multiple numbers or arguments
at the same time when not knowing how many arguments or numbers are needed
in your code these arguments will get together and are usable inside a tuple
and accessible through (*) operator

'''

import matplotlib.pyplot as plt  # We have plotted the table available in result.pdf
from math import pi, cos, fabs  # some functions we would need
import time  # for measuring Time
import subprocess  # for running CPP code
import random
import math


def summation(*args):
    return sum(args)


print(summation(4, 5, 6))

'''
The second Argument in python is usually used in functions and puts the arguments
inside a dictionary and is accessible through keywords and assignments.

'''


def fruit(**kwargs):
    for key, val in kwargs.items():
        print(f"{key} -> {val}")


fruit(first="Apple", Second="Peach")


# Question 2 : Working With Lists and Dictionary:

A0 = dict(zip(("a", "b", "c", "d", "e"), ("1", "2", "3", "4", "5")))
"Output = a,b,c,d,e as keys -> 1,2,3,4,5 as values"

A1 = range(10)
"Output = numbers from 0 to 9"

A2 = [i for i in A1 if i in A0]
"Output = an empty list, A0 and A1 got nothing in common"

A3 = sorted(A0[i] for i in A0)
"Output = A list from a dictionary"

A4 = [[i, i * i] for i in A1]
"""Output is "well put" as a list of lists """

itemsDefined = dict(zip(("A0", "A1", "A2", "A3", "A4"), (A0, A1, A2, A3, A4)))

for key, val in itemsDefined.items():
    print(f"{key} : {val}")

# Question 3 : Estimating Pi :


def IsInCircule(x, y):
    r = 0.5  # Radius Defined as 0.5
    if (x - r) ** 2 + (y - r) ** 2 <= r**2:  # The Equation of Circle
        return True
    return False


def EstimatePi(n):
    num = [IsInCircule(random.random(), random.random()) for _ in range(n)]
    return 4 * num.count(True) / num.__len__()

# Question 3(cntd.) : Finding Pi :


def Find():
    n = 1
    while True:
        pi = EstimatePi(n)
        n += 1
        diff = abs(pi - math.pi)
        if diff / math.pi < 0.01:
            print(f"Estimate pi number : {pi:0.3f}")
            print(f"real pi : {math.pi:0.3f}")
            print(f"points : {n}")
            break
    return n


Find()

# Question 4 : Legendre Polynomials and estimating Integration :


class GaussMethod:
    def __init__(self, p, a, b, n):
        self.c_p = p
        self.c_a = a
        self.c_b = b
        self.c_n = n

    def CoefLegendre(self, c_n, x):
        if c_n == 0:
            return 1
        elif c_n == 1:
            return x

        else:
            return ((2 * c_n - 1) / c_n) * x * self.CoefLegendre(c_n - 1, x) - ((c_n - 1) / c_n) * self.CoefLegendre(c_n - 2, x)

    def PolyLegendre(self, c_n, x):
        return (c_n / (x * x - 1)) * ((x * self.CoefLegendre(c_n, x)) - self.CoefLegendre(c_n - 1, x))

    def ZeroesLegendre(self, c_n, i):
        newx = 0
        oldx = cos(pi * (i - 0.25) / (c_n + 0.5))
        iteration = 1
        if iteration != 1:
            oldx = newx
            newx = oldx - \
                self.CoefLegendre(c_n, oldx) / self.PolyLegendre(c_n, oldx)
            iter += 1

        while 1 + fabs((newx - oldx)) > 1.0:
            if iteration != 1:
                oldx = newx
            newx = oldx - \
                self.CoefLegendre(c_n, oldx) / self.PolyLegendre(c_n, oldx)
            iteration += 1

        return newx

    def Weight(self, c_n, x):
        return 2 / ((1 - x**2) * self.PolyLegendre(c_n, x) ** 2)

    def Calculate(self):
        integral = 0
        iteration = 1
        iteration += 1
        for i in range(1, self.c_n + 1):
            integral += self.c_p(self.ZeroesLegendre(self.c_n, i)) * \
                self.Weight(self.c_n, self.ZeroesLegendre(self.c_n, i))

        self.c_result = ((self.c_b - self.c_a) / 2) * integral

    def Result(self):
        return self.c_result


def Function(x):
    xN = 0.5 * x + 0.5
    return ((xN**3) / (xN + 1)) * cos(xN**2)


compile_cpp = [
    "g++",
    "./CppFiles/Main.cpp",
    "./CppFiles/GaussMethod.cpp",
    "-o",
    "main",
]


cpp_time_wholesale = list()
python_time_wholesale = list()
iteration = 11

for i in range(1, iteration + 1):
    timeOf_py_start = time.time()
    solver = GaussMethod(Function, 0, 1, i)
    solver.Calculate()
    timeOf_py_end = time.time()
    run_cpp = ["./main", f"{i}"]
    subprocess.run(compile_cpp)
    timeOf_cpp_start = time.time()
    subprocess.call(run_cpp)
    timeOf_cpp_end = time.time()
    python_time = (timeOf_py_end - timeOf_py_start) * 1000  # convert to ms
    cpp_time = (timeOf_cpp_end - timeOf_cpp_start) * 1000  # convert to ms
    print(f"Result of Python code (n = {i}) : {solver.Result()}")
    print(f"Python Calculation Time = : {python_time} ms")
    print(f"C++ Calculation Time = : {cpp_time} ms")
    print()
    cpp_time_wholesale.append(cpp_time)
    python_time_wholesale.append(python_time)

# Now For MatplotLib
x_axis = list(range(1, iteration + 1))  # Creating the X-Axis
plt.figure(num="Comparison Between cpp and Python Calculation Time")
plt.plot(x_axis, python_time_wholesale, color="red", scalex=[1, iteration + 1])
plt.plot(x_axis, cpp_time_wholesale, color="blue", scalex=[1, iteration + 1])
plt.legend(["Python", "Cpp"])
plt.xlabel("Iteration")
plt.ylabel("Time (ms)")
plt.savefig("result.pdf", format="pdf")

# Question 5 : Divisors of 6

Input = list(map(int, input("Enter Numbers : ").split()))
Output = list()
for i in enumerate(Input):
    if i[0] % 6 == 5 and i[1] % 6 == 0:
        Output.append(i[1])
Output.sort()
print(*Output)
