#include <stdio.h>
#include <math.h>

double f(double t, double y)
{
  return t * sqrt(y);
}



int main()
{
  double y, t = 0.0, dt = 0.01;
  double tmax = 10.0;
  int Nt = (tmax - 0.0) / dt;
  FILE *fp;
  fp = fopen("osc_exp.txt", "w");

  y = 1.0;


  for (int i = 0; i <= Nt; i++)
  {
    // RK4 coefficients
    double k1 = dt * f(t, y);
    double k2 = dt * f(t + 0.5 * dt, y + 0.5 * k1);
    double k3 = dt * f(t + 0.5 * dt, y + 0.5 * k2);
    double k4 = dt * f(t + dt, y + k3);

    // Mise à jour de y avec la méthode RK4
    y += (k1 + 2 * k2 + 2 * k3 + k4) / 6.0;

    // Écriture dans le fichier
    fprintf(fp, "%lf %lf 0\n", t, y);

    // Incrément du temps
    t += dt;
  }

  fclose(fp);

  return 0;
}
