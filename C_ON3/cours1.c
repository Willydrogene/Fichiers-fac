#include <stdio.h>
int main()
{
printf("Hello world\n");
return 0;
}

/* 
mettre dans le terminal: 
gcc -Wall -O3 cours1.c -o hello 
en début de code : <stdio.h> , <stdlib.h> , <math.h> 


type de variables:

	entier: char 8 bits 1 octet / byte
		short 16 bits
		int 32 bits
		long 64 bits (2⁶⁵-1)

	réels:  float
		double
		
	long a,b; c=a/b; entier donc =0 car division entière



tableau: vecteur, matrice, cube,... 
=> int tab[120]; int tab[120][120]; Attention, 0 => 119



printf("texte"), printf("%d", i); %d:int, %ld:long, %f: float, %lf: double
	exemple: printf("la viariable i vaut %d; la variable f:%ld", i, f);

scanf(" %d", &i); pour demander d'entrer une valeur à l'utilisateur



ouverture de fichier:
	fopen("nom.txt", "w"); ("w": write, "r": readonly, "a": append)

	FILE *fp; 
	fp=fopen(...);
	fprintf(fp, "...%...", i, j);
	fscanf(fp, "%ld", j);
	fclose(fp);

	si erreur ouverture fopen renvoie 0, donc on teste si fp=0 pour s'assurer

*/


