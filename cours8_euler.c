#include <stdio.h>
#include <math.h>

void print_t(double[], int);

int main()
{
  int i;
  double tmin = 0.0;
  double tmax = 100.0;
  double dt = 0.1;
  double T0 = 100.0;
  double TR = 20.0;
  double k = 0.07;
  
  int Nt = ((tmax - tmin) / dt);
  //double t[Nt+1];
  
  double T[Nt];
  
  for (i=0; i<Nt; i++) {T[i] = 0.0;}
  
  T[0] = T0;
  /*t[0] = tmin;      // ici le t de sert à rien
  
  printf("Nt = %d\n", Nt);
  
  for (i=1; i<=Nt; i++)
  {
    t[i] = t[i-1] + tmin + (tmax-tmin)/Nt;
  }
  //print_t(t, Nt);
  */
  
  printf("T[0] = %lf, ", T0);
  for (i=0; i<Nt; i++)
  {
    T[i+1] = T[i] + dt*(-k*(T[i]-TR));
    printf("T[%d] = %lf, ", i+1, T[i+1]);
  }
  printf("\n");
  
return 0;
}
  



void print_t(double t[], int Nt)
{
  int i;

  for(i = 0; i < Nt+1; i++) 
  {
   printf("%lf ", t[i]);  
  }
  printf("\n\n");
}




/*

yn+1 = yn + h*f(tn, yn)


*/
