#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>


void rot(int dec, char* str);

int main(int argc, char **argv)
{
  char *str;
  int dec,l;
  
  if (argc != 3)
  {
    (void)printf("usage: décalage texte\n"); exit(0);
  }
  
  dec = atoi(argv[1]);
  l = strlen(argv[2]);
  
  str = malloc(l * sizeof(char));
  
  strcpy(str, argv[2]);
  
  (void)printf("Original: %s\n", str);
  
  rot(dec, str);
  
  (void)printf("Encrypted: %s\n", str);
  
  rot(26-dec, str);
  
  (void)printf("Decrypted: %s\n", str);
  
  free(str);
  
  
  
  return 0;
}



void rot(int c, char *str)
{
 const char* alpha_low = "abcdefghijklmnopqrstuvwxyz";
 const char* alpha_high = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
 
 int l = strlen(str);
 
 char subst; // substitution character
 int idx;    // index
 int i;      // loop var
 
 for(i=0; i<l; i++)
 {
 
   if(isalpha(str[i])!=0)
   {
     idx = (int)( (tolower(str[i])-'a') +c )%26;
     
     if(isupper(str[i])) subst=alpha_high[idx];
     else                subst=alpha_low[idx];
     
     str[i] = subst;
   }   
    
 }
 
}









/*
for (int i=0; str[i] != '\0'; i++)
{
  if(str[i] >= 'A' && str[i] <= 'Z')
  {
    str[i] = 'A' + (str[i] - 'A' + dec) % 26;
  }
  else if(str[i] >= 'a' && str[i] <= 'z')
  {
    str[i] = 'a' + (str[i] - 'a' + dec) % 26;
  }
}
*/
