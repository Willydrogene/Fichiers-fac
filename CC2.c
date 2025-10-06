#include <stdio.h>
#include <stdlib.h>
#include <time.h>   // Pour srand()
#include <math.h>

void fonction(int, double, double, double[], double[]);

int main()
{
  int a, i;
  double x0, y0;
  
  
  srand48(time(0)); 
  
  printf("Combien de points? ");
  scanf(" %d", &a);
  printf("Quel est le point de départ?\nx0=");
  scanf(" %lf", &x0);
  printf("y0=");
  scanf(" %lf", &y0);
  
  printf("a=%d, (%lf,%lf)\n", a, x0, y0);



  double x[a], y[a];


  for(i=0; i<a; i++)
  {
    x[i] = drand48() * 2-1;
    y[i] = drand48() * 2-1;
    printf("(%lf,%lf)\n", x[i], y[i]);
  }
  
  fonction(a, x0, y0, x, y);
  
  
  
  return 0;
}


void fonction(int a, double x0, double y0, double x[], double y[])
{
  double tableau[a]; int i;
  double distance_min = fabs(sqrt(x0 * x0 + y0 * y0));
  double x_min=0.0, y_min=0.0;
  FILE *fp;
  fp = fopen("mes_points.txt", "w");
  
  
  for (i=0; i<a; i++)
  {
    tableau[i] = fabs(sqrt((x[i]-x0) * (x[i]-x0) + (y[i]-y0) * (y[i]-y0)));
    printf("distance[%d] = %lf\n", i+1, tableau[i]);
    
    if (distance_min > tableau[i])
    {
      distance_min = tableau[i]; 
      x_min=x[i]; 
      y_min=y[i];
    }
    
  }
  printf("La distance minimale est : %lf\n", distance_min);
  printf("Le point le plus proche est donc (%lf,%lf)\n", x_min, y_min);
  
  fprintf(fp, "%lf %lf %lf %lf %lf\n", x0, y0, x_min, y_min, distance_min);
  
  fclose(fp);
  //return tableau;
}





/* CC2 printemps 2025 Phys2-ON3

  Le but du programme est de chercher un chemin "assez court" entre plusieurs points.

  L'utilisateur entre au clavier le nombre de points choisi et le point de depart.

  Stocker dans deux tableaux 1D (une seule dimension x et y) les coordonnees aleatoires des points entre -1 et 1

  Ecrire une fonction qui prend en entree la position actuelle et qui retourne
  le tableau des distances du point choisi aux autres. (il peut y avoir d'autres parametres necessaires en entree)

  Trouver le point le plus proche du point actuel.

  Afficher a l'ecran et enregistrer dans un fichier le point, ses coordonnees et sa distance au point precedent.

  Continuer le chemin de proche en proche sans repasser deux fois par le meme point.

  On pourra afficher la distance totale parcourue.

  PS: on fera des allocations memoires. On verifiera bien que toutes les operations sont valides.
*/

