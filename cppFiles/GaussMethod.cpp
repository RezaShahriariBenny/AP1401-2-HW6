#include "GaussMethod.h"
#include <iostream>
#include <math.h>
using namespace std;

GaussMethod::GaussMethod(long double (*pf)(const long double &x), long double a,
                         long double b, int n)
    : m_Pf(pf), c_A(a), c_B(b), c_N(n) {}

long double GaussMethod::Coeflegendre(int c_N, long double x) {
  if (c_N == 0)
    return 1;
  else if (c_N == 1)
    return x;
  else
    return ((2.0 * c_N - 1) / c_N) * x * Coeflegendre(c_N - 1, x) -
           ((1.0 * c_N - 1) / c_N) * Coeflegendre(c_N - 2, x);
}

long double GaussMethod::PolyLegendre(int c_N, long double x) {
  long double Polylegendre{};
  Polylegendre = (1.0 * c_N / (x * x - 1)) *
                 ((x * PolyLegendre(c_N, x)) - PolyLegendre(c_N - 1, x));
  return Polylegendre;
}

long double GaussMethod::Zeroeslegendre(int c_N, int i) {
  long double xnew1{}, xold1{};
  long double pi = 3.141592655;
  xold1 = cos(pi * (i - 1 / 4.0) / (c_N + 1 / 2.0));
  int iteration{1};

  do {
    if (iteration != 1)
      xold1 = xnew1;
    xnew1 = xold1 - Coeflegendre(c_N, xold1) / PolyLegendre(c_N, xold1);
    iteration++;
  } while (1 + fabs((xnew1 - xold1)) > 1.);
  return xnew1;
}

long double GaussMethod::Weight(int c_N, long double x) {
  long double weightI{};
  weightI = 2 / ((1 - pow(x, 2)) * pow(PolyLegendre(c_N, x), 2));
  return weightI;
}

void GaussMethod::calculate() {
  long double integral{0};
  int iteration{1};
  iteration++;
  integral = 0;
  // n++;
  for (int i{1}; i <= c_N; i++)
    integral = integral + m_Pf(Zeroeslegendre(c_N, i)) *
                              Weight(c_N, Zeroeslegendre(c_N, i));

  c_Result = ((c_B - c_A) / 2.0) * integral;
}

long double GaussMethod::Result(void) { return c_Result; }