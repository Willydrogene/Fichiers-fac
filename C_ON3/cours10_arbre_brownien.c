#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define TAILLE 200

void montrer_tableau(int, int, int[TAILLE][TAILLE]);

void exporter_PBM(int taille, int tableau[TAILLE][TAILLE], const char *nom_fichier) {
    FILE *fichier = fopen(nom_fichier, "w");
    if (fichier == NULL) {
        perror("Erreur d'ouverture du fichier");
        return;
    }

    // Écriture de l'en-tête PBM
    fprintf(fichier, "P1\n%d %d\n", taille, taille);

    // Écriture des pixels
    for (int i = 0; i < taille; i++) {
        for (int j = 0; j < taille; j++) {
            fprintf(fichier, "%d ", tableau[i][j]);
        }
        fprintf(fichier, "\n");
    }

    fclose(fichier);
    printf("Fichier %s généré avec succès.\n", nom_fichier);
}



int main()
{
  //int taille = 11;
  int nb_part, n=-1, a, tableau[TAILLE][TAILLE] = {0}, nb_alea_i, nb_alea_j;
  int alea_i, alea_j, mur_i_inf, mur_i_sup, mur_j_inf, mur_j_sup;
  srand(time(NULL));

  printf("Combien de particules? "); scanf(" %d", &nb_part); printf("\n");

  tableau[100][100] = 1;

  //montrer_tableau(TAILLE, n, tableau);

  for (n=0; n<nb_part; n++)
  {
    a=0;
    do
    {
      nb_alea_i = rand() % (TAILLE);
      nb_alea_j = rand() % (TAILLE);
    } while ( tableau[nb_alea_i][nb_alea_j] == 1 );

    tableau[nb_alea_i][nb_alea_j] = 1;
    //printf("On est la, %d, %d\n", nb_alea_i, nb_alea_j);
    //montrer_tableau(TAILLE, n, tableau);


    while (a==0)
    {


      if (nb_alea_i == 0) {mur_i_inf=-1;} else {mur_i_inf=1;}
      if (nb_alea_i == TAILLE-1) {mur_i_sup=-1;} else {mur_i_sup=1;}
      if (nb_alea_j == 0) {mur_j_inf=-1;} else {mur_j_inf=1;}
      if (nb_alea_j == TAILLE-1) {mur_j_sup=-1;} else {mur_j_sup=1;}

      if ( (tableau[nb_alea_i-mur_i_inf][nb_alea_j]==0) && (tableau[nb_alea_i-mur_i_inf][nb_alea_j-mur_j_inf]==0) &&
           (tableau[nb_alea_i][nb_alea_j-mur_j_inf]==0) && (tableau[nb_alea_i+mur_i_sup][nb_alea_j-mur_j_inf]==0) &&
           (tableau[nb_alea_i+mur_i_sup][nb_alea_j]==0) && (tableau[nb_alea_i+mur_i_sup][nb_alea_j+mur_j_sup]==0) &&
           (tableau[nb_alea_i][nb_alea_j+mur_j_sup]==0) && (tableau[nb_alea_i-mur_i_inf][nb_alea_j+mur_j_sup]==0) )
      {
        if (mur_i_inf==-1) {alea_i = rand()%2;}
        else if (mur_i_sup==-1) {alea_i = -(rand()%2);}
        else {alea_i = (rand()%3)-1;}

        if (mur_j_inf==-1) {alea_j = rand()%2;}
        else if (mur_j_sup==-1) {alea_j = -(rand()%2);}
        else {alea_j = (rand()%3)-1;}

        //printf("iinf = %d, jinf = %d, isup = %d, jsup = %d\n", mur_i_inf, mur_j_inf, mur_i_sup, mur_j_sup);
        //printf("alea_i = %d, alea_j = %d\n", alea_i, alea_j);

        tableau[nb_alea_i][nb_alea_j] = 0;
        nb_alea_i += alea_i; nb_alea_j += alea_j;
        tableau[nb_alea_i][nb_alea_j] = 1;
        //printf("nb_alea_i = %d, nb_alea_j = %d\n", nb_alea_i, nb_alea_j);
        //montrer_tableau(TAILLE, n, tableau);
      }
      else {a=1;}
    }
    //printf("nb_alea_i = %d, nb_alea_j = %d\n", nb_alea_i, nb_alea_j);
    //montrer_tableau(TAILLE, n, tableau);


  }
  //montrer_tableau(TAILLE, n, tableau);
  exporter_PBM(TAILLE, tableau, "resultat.pbm");

  return 0;
}



void montrer_tableau(int taille, int n, int tableau[TAILLE][TAILLE])
{
  int i,j;

  printf("Tableau %d\n", n+1);

  for (i=0; i<taille; i++)
  {
    for (j=0; j<taille; j++)
    {
      printf("%d  ", tableau[i][j]);
    }
    printf("\n");
  }
  printf("\n");
}




/*

Regarder les cases autour, je me dÃŠplace alÃŠatoirement sur une des cases Ã  cotÃŠ, s'il y a un voisin, je m'arrÃĒte.

*/
