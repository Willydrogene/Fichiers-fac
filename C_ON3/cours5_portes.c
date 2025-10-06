#include <stdio.h>

void print_les_portes(int[]);

int main()
{

int porte[100] = {0};
int i,j;

print_les_portes(porte);

for(i=1; i<=100; i++)
{
  for (j=i-1; j<100; j+=i)
  {
    porte[j]=!porte[j];
  }
}

print_les_portes(porte);

return 0;
}

void print_les_portes(int porte[])
{
  int i;

  for(i = 0; i < 100; i++) 
  {
   printf("%d ", porte[i]);  
  }
  printf("\n\n");
}
