#include <stdio.h>
#include <string.h>

int main()
{
  int ch;
  for(ch=32;ch<=127;ch++)
  {
    (void)printf("ASCII value = %d, Character = %c\n", ch, ch);
  }
  

return 0;
}




/*
#include <string.h>

strlen(ch)------------------------------Longueur d'une chaîne
strcpy(ch1,ch2) / strncpy---------------Copier une chaîne
strcat(ch1,ch2) / strncat(ch1,ch2,n)----Ajouter une chaîne
strcmp(ch1,ch2) / strncmp---------------Comparer des chaînes
strchr / strrchr------------------------Trouver un caractère
strstr----------------------------------Trouver une sous-chaîne
strtok----------------------------------Découper une chaîne
memset----------------------------------Initialiser un bloc mémoire
memcpy / memmove------------------------Copier de la mémoire
strspn / strcspn------------------------Trouver un préfixe/suffixe

atoi : alpha to integer (transforme une chaine de car en nombre)
atol : alpha to long 
strtod : string to double
strtof : string to float

*/
