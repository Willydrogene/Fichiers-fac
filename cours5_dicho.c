#include <stdio.h>
#include <math.h>
#include <stdlib.h>

float f(float);

int main()
{


float a=-0.0;
float b=5.0;
float c;
float precision=1e-6;

while ((b-a)/2 > precision)
{
  c=(a+b)/2;
  if (fabs(f(c)) < precision)
  {printf("Racine trouvée : %f\n", c); exit(0);}
  else if (f(a)*f(c) < 0)
  {b=c;}
  else
  {a=c;}
}
printf("On a donc comme racine: %f\n", (a+b)/2);

return 0;
}


    
    
float f(float x)
{return -(x*x)+2*x+3;}

