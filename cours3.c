#include <stdio.h>
#include <stdlib.h> // Pour rand() et drand48()
#include <time.h>   // Pour srand()

int main()
{
  int a[3][3], b[3][3], c[3][3];
  int i, j, k; 

  srand48(time(0)); 

    
  for(i=0; i<3; i++)
  {
    for(j=0; j<3; j++)
    {
      a[i][j] = (int)(drand48()*10); 
      b[i][j] = (int)(drand48()*10); 
      c[i][j] = 0; 
            
      printf("a[%d][%d] = %d, b[%d][%d] = %d\n", i, j, a[i][j], i, j, b[i][j]);
    }
  }
  
  // Calcul de c, produit de a et b
  for(i=0; i<3; i++)
  {
    for(j=0;j<3; j++)
    {
      for(k=0; k<3; k++)
      {
        c[i][j]=c[i][j]+(a[i][k]*b[k][j]);
      }
    }
  }
  

// Affichage de la matrice a
  printf("\nVoici la matrice a :\n");
  for(i=0; i<3; i++)
  {
    for(j=0; j<3; j++)
      {
        printf("%d ", a[i][j]);
      }
    printf("\n");
  }

// Affichage de la matrice b
  printf("\nVoici la matrice b :\n");
  for(i=0; i<3; i++)
  {
    for(j=0; j<3; j++)
    {
      printf("%d ", b[i][j]);
    }
      printf("\n");
  }
    
// Affichage de la matrice c, produit de a et b
  printf("\nVoici la matrice c :\n");
  for(i=0; i<3; i++)
  {
    for(j=0; j<3; j++)
    {
      printf("%d ", c[i][j]);
    }
      printf("\n");
  }

  return 0;
}

