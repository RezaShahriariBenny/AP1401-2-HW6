#ifndef GAUSSMETHOD_H
#define GAUSSMETHOD_H
class GaussMethod {
public:
  GaussMethod(long double (*pf)(const long double &), long double a,
              long double b, int n);
  void calculate(void);
  long double Result();

private:
  long double (*m_Pf)(const long double &);
  long double c_A, c_B;
  int c_N;
  long double c_Result;

  long double Coeflegendre(int, long double);
  long double PolyLegendre(int, long double);
  long double Zeroeslegendre(int, int);
  long double Weight(int, long double);
};

#endif