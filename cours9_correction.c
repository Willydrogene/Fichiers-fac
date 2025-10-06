#include <stdio.h>
#include <math.h>


int main()
{
  double dtheta, domega;
  double dt = 0.02;
  double om2 = 40.0;
  double t = 0;
  double theta = 0;
  double omega = 2.0;
  FILE *fp;
  
  fp = fopen("osc_exp.txt", "w");
  do
  {
    domega = om2 * dt * sin(theta);
    dtheta = omega * dt;
    
    theta += dtheta;
    omega -= domega;
    
    (void)fprintf(fp, "%f %f %f\n", t, theta, omega);
  }
  while ( (t+=dt) <= 5.0 );
  (void)fclose(fp);
  
return 0;
}

