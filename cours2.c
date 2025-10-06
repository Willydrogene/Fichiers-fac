#include <stdio.h>
#include <stdlib.h> //drand48
#include <time.h> //srand48(time(0))

int main()
{

double tab[10];
int i;
srand48(time(0));

for(i=0; i<10; i=i+1)
{tab[i] = drand48();}

printf("Voici mon tableau : \n");

for(i=0; i<10; i=i+1)
{printf("%d valeur: %lf \n", i+1, tab[i]);}

return 0;

}





/*

gcc -Wall -O3 cours2.c -o hello 


structure de contrôle: 
	boucle:
		int i;
		for(i=0; i<=10; i=i+1)
		{
		printf("i=%d\n",i);
		}

		
		while(i<=10)
		{
		printf("i=%d\n",i);
		i = 23*4/abc;
		}
		
		
		do
		{
		printf("i=%d\n",i);
		}while(i<=10);
		
		
	test:
		if((a<4)&&(b>5))	 et: &&, ou: || 
		{
		...
		}
		else
		{
		...
		}
		else if(...)
		{
		...
		}


nombres aléatoires:
	rand() -> nombres entiers uniforme entre 0 et randmax
	drand48() -> 0 et 1 réel

*/
