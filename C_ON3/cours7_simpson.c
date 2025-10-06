#include <stdio.h>
#include <math.h>


double f(double x);
double simpson(double a, double b, int n);



int main()
{
  double a = 0;
  double b = M_PI / 2; 
  int n = 100;         
    
  if (n%2!=0) 
  {
    printf("Erreur : n doit être pair pour la méthode de Simpson.\n");
    return 1;
  }

  double result = simpson(a, b, n);

  printf("Le résultat de l'intégration est: %lf\n", result);
  printf("Valeur de pi/4 = %lf\n", M_PI / 4); 

  return 0;
}


double f(double x)
{
  return (cos(x) / (2-cos(x)*cos(x)));
}


double simpson(double a, double b, int n)
{
  double h = (b-a)/n;
  double somme = f(a) + f(b);

  // impairs
  for (int i=1; i<n; i+=2)  
  {
    somme += 4*f(a+i*h);
  }

  // pairs 
  for (int i=2; i<n; i+=2)  
  {
    somme += 2*f(a+i*h);
  }

  return (h/3)*somme;
}

