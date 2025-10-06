#include <stdio.h>
#include <math.h>


int main()
{
  int i;
  double tmax = 5.0; double tmin = 0.0;
  double dt = 0.02; double t = 0;
  int Nt = (tmax-tmin)/dt;
  double theta, dtheta, omega, domega;
  
  
  theta = 0.0;
  omega = 2.0;
  double w02 = 40.0;
  
  
  printf("t = %lf\t theta = %lf\t omega = %lf\n", t, theta, omega);
  
  for (i=0; i<Nt; i++)
  {
    domega = -w02*sin(theta) * dt;
    dtheta = omega * dt;
    
    theta += dtheta;
    omega += domega;
    t += dt;
    
    printf("t = %lf\t theta = %lf\t omega = %lf\n", t, theta, omega);
  }
  
  
  return 0;
}



