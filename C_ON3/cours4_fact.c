#include <stdio.h>
#include <stdlib.h>

long fact(long*,long*,long*);
long fact_recurs(long);

int main()
{

long i, n;
long result=1;

scanf("%ld", &n);

fact(&i, &n, &result);

printf("Résultat final: %ld\n", result);
printf("Récursif: %ld\n", fact_recurs(n));

return 0;
}


long fact(long *i, long *n, long *result)
{
  for(*i=1; *i<=*n; *i=*i+1)
  {
    *result = *i * *result;
    printf("On a: %ld\n", *result);
  }
  return *result; 
}

long fact_recurs(long n)
{
  return n==0 ? 1 : n*fact_recurs(n-1);
}
