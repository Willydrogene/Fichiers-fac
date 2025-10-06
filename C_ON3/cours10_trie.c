#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
  int i, j, *tableau, *tableau_trie, valeur = 10, mon_i = 0, ii = 0, taille = 10; 
  tableau = malloc(taille * sizeof(int));
  tableau_trie = malloc(taille * sizeof(int));
  
  srand(time(0)); 
  
  for (i=0; i<taille; i++)
  {
    tableau[i] = (rand() % 11)-1;
    printf("%d\n", tableau[i]);
  }
  
  
  for (j=0; j<taille; j++)
  {
    for (i=0; i<taille; i++)
    {
      if (tableau[i] < valeur)
      {
        valeur = tableau[i];
        ii = i;
      }
    }
  
    tableau_trie[mon_i] = valeur;
    tableau[ii] = 10;
    mon_i += 1;
    valeur = 10;
  }
  
  printf("\nMon tableau trié:\n");
  
  for (i=0; i<taille; i++)
  {
    printf("%d\n", tableau_trie[i]);
  }
  

  return 0;
}
