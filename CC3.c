#include <stdio.h>
#include <math.h>


int puissance(int);
int somme(int);
int premier(int);


int main()
{
  int n, n_originel, resultat, limite = 0, pas_premier;
  
  printf("Quel est le nombre que tu choisis? : ");
  scanf(" %d", &n);
  
  n_originel = n;
  
  do
  {
    resultat = somme(n);
    printf("Ma somme de %d est : %d\n", n, resultat);
    
    n = resultat;
    limite += 1;
  } while ((resultat!=1) && (limite < 30));
  
  if (resultat == 1)
  {printf("%d est un nombre happy!\n", n_originel);}
  else {printf("%d n'est pas un nombre happy\n", n_originel);}
  
  pas_premier = premier(n_originel);
  if ( pas_premier==0 ) {printf("%d est un nombre premier!\n", n_originel);}
  else {printf("%d n'est pas un nombre premier\n", n_originel);}
  
  
  if ((resultat == 1) && (pas_premier == 0))
  {printf("%d est un happy prime number!\n", n_originel);}
  else if ( (resultat==1) && (pas_premier == 1))
  {printf("%d est un happy number!\n", n_originel);}
  
  
  return 0;
}



int puissance(int logg)
{
  int i; int nombre=1;
  for (i=0; i<logg; i++)
  {nombre = nombre *10;}
  return nombre;
}


int somme(int n)
{
  int i, logg, valeur, sum = 0;
  
  logg = log10(n)+1; //Nombre de "chiffres" que contient le nombre
  
  for (i=0; i<logg; i++)
  {
    valeur = n / puissance((logg-1)-i);  //Je récupère ..., la centaine, la dizaine, l'unité.
    n = n - (valeur * puissance((logg-1)-i));  //Si j'ai 235, ca me donne 35
    sum += (valeur * valeur);  //Somme des carres
  }
  
  return sum;
}

int premier(int n)
{
  int i, a=0;
  
  for (i=2; i<n; i++)
  {
    if ( (n%i)==0 ) {a=1;}
  }
  
  return a;
}


/* Soit un nombre entier n compose de plusieurs chiffres.
   On calcule la somme des carres de chaque chiffre de ce nombre.

   Par exemple pour le nombre 712 on obtient 7*7 + 1*1 + 2*2 =54

   On repetera le processus un certain nombre de fois
   (712 -> 54 -> 5*5 + 4*4 = 41 -> 4*4 + 1*1 = 17 -> ... ) jusqu'a eventuellement obtenir 1.
   (penser que ce processus peut-etre infini, on pourra utiliser une valeur 
    maximale d'iterations)
   Si on obtient 1 le nombre est dit 'happy'

   Ecrire une fonction qui renvoie la somme des carres d'un nombre entre au clavier
   et passe comme parametre.

   Ecrire un programme qui verifie si un nombre est 'happy'

   Puis ajouter au programme une deuxieme fonction qui teste si un nombre passe comme parametre est premier.

   Verifier si le nombre choisi est un 'happy prime number'

    exemple de happy number: 23, 193, 367
    exemple de happy prime number:  7, 239, 487

NB: les fonctions modulo et divisions entieres suffisent a resoudre le probleme.
    Sinon on pourra aussi utiliser la fonction log10(x)+1 renvoie le nombre de chiffres du nombre x
*/



