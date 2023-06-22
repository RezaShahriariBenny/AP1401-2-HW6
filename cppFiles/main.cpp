#include "GaussMethod.h"
#include <cmath>
#include <iomanip>
#include <iostream>

long double aFunction(const long double &);

int main(int argc, char *argv[]) {

  long double a{0}, b{1};
  int n{atoi(argv[1])};
  long double (*pf)(const long double &);
  pf = aFunction; // Pointer initialized
  GaussMethod aSolver(pf, a, b, n);
  aSolver.calculate(); // Calculate the integral
  std::cout.precision(20);
  std::cout << "Result of C++ code =" << std::setw(2) << n << aSolver.Result()
            << std::endl;

  return 0;
}

long double aFunction(const long double &x) {
  long double xN = 0.5 * x + 0.5;
  return (pow(xN, 3) / (xN + 1)) * cos(pow(xN, 2));
}