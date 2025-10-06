#include <stdio.h>
#include <stdlib.h> //drand48
#include <time.h> //srand48(time(0))
#include <math.h> // Pour fabs()

int main()
{

int i;
int n;
double somme=0.0;
double somme_avant = -1.0;

double pi_car_sur_6 = M_PI*M_PI/6.0;

printf("Entrez la valeur maximale de la somme 1/n:\n\n");
scanf("%d", &n);


for(i=1; i<=n; i=i+1)
{
  somme = somme + 1.0/(i*i);
  //printf("La on est a: %.15lf", fabs(somme - somme_avant));
  if (i > 1 && fabs(somme - somme_avant) <= 1.0e-9)
  {
   printf("On y est "); 
   break;
  }
  somme_avant = somme;
}

printf("\nRésultat : %d %.15lf \n\n", i, somme);
printf("\nPi²/6 vaut : %.15lf \n\n", pi_car_sur_6);



return 0;

}
