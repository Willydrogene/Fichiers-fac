#include <stdio.h>
#include <stdlib.h>

void print_le_tableau(int[], int);

int main()
{
  int i, j, limite, a;
  int *tableau;

  scanf("%d", &limite);
  
  tableau = calloc(limite, sizeof(int));
  
  for (i=2; i<limite; i++)
  {
    a=0;
    for (j=2; j<i; j++)
    { 
      if((i%j)==0)
      {a=1;}
      
    }
    if (a==0)
    {
      printf("%d est 1er\n", i);
      tableau[i] = i;
    }
  }
  
  print_le_tableau(tableau, limite);
  
  for (i=0; i<limite; i++)
  {
    if (tableau[i]!=0)
    {
      if ((i<limite-6) && (tableau[i+6]!=0))
      {
        printf("On a un doublé ici: (%d, %d)\n", tableau[i], tableau[i+6]);
        if ((i<limite-12) && (tableau[i+12]!=0))
        {
          printf("On a un triplé ici: (%d, %d, %d)\n", tableau[i], tableau[i+6], tableau[i+12]);
          if ((i<limite-18) && (tableau[i+18]!=0))
          {
            printf("On a un quadruplé ici: (%d, %d, %d, %d)\n", tableau[i], tableau[i+6],
            tableau[i+12], tableau[i+18]);
            if ((i<limite-24) && (tableau[i+24]!=0))
            {
              printf("On a un quintuplé ici: (%d, %d, %d, %d, %d)\n", tableau[i], tableau[i+6],
              tableau[i+12], tableau[i+18], tableau[i+24]);
            }
          }          
        }
      }
      
    }
  }


return 0;
}


void print_le_tableau(int tableau[], int limite)
{
  int i;

  for(i = 0; i < limite; i++) 
  {
   printf("%d ", tableau[i]);  
  }
  printf("\n\n");
}
