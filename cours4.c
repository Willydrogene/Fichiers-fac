#include <stdio.h>
#include <stdlib.h> //drand48
#include <time.h> //srand48(time(0))


void f(int *, int *);
int main()
{

  int i,j;
  i=4; j=5;
  f(&i,&j);
  printf("%d %d\n", i,j); 



  return 0;
}


void f(int *i, int *j)
{
  printf("%d %d\n", *i,*j);  
  *i=6;*j=7;
  printf("%d %d\n", *i,*j); 
}






/*
int i,j;
i=4;j=5;
f(i,j);
printf("%d %d\n", i,j); renvoie 4,5 car copie de la valeur sans retour

void f(int i, int j)
{
printf("%d %d", i,j);  renvoie 4,5
i=6;j=7;
prinf("%d %d\n", i,j); renvoie 6,7
}

-----------------------------------------------------------------------
int i,j;
i=4;j=5;
f(&i,&j);
printf("%d %d\n", i,j); renvoie 6,7 car remplacement sur l'adresse directement

void f(int *i, int *j)
{
printf("%d %d", *i,*j);  renvoie 4,5
*i=6;*j=7;
prinf("%d %d\n", *i,*j); renvoie 6,7
}
*/
