#include <stdio.h>
#include <stdlib.h>
int main()
{

int i, n;
int result=1;

scanf("%d", &n);

for(i=1; i<=n; i++)
{
  result = i*result;
  printf("On a: %d\n", result);
} 

printf("Résultat final: %d\n", result);

return 0;
}


/*

Allocation dynamique de mémoire:

double *t;
t=malloc(taille octets);
if (t==0)
{printf("erreur alloc memoire"); exit(0);}
free(t);


*/
