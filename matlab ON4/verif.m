clear all
n = input('n?')
carre = magic(n);

liste_resultats_lignes = [];
liste_resultats_colonnes = [];
liste_resultats_diag1 = [];
liste_resultats_diag2 = [];

indice_diag1 = 1;
indice_diag2 = length(carre);
addition_diag1 = 0;
addition_diag2 = 0;

for ligne_puis_colonne=1 : 1 : length(carre)
    addition_lignes = 0;
    addition_colonnes = 0;
    
    for colonne_puis_ligne=1 : 1 : length(carre)
        addition_lignes = addition_lignes + carre(ligne_puis_colonne, colonne_puis_ligne);
        addition_colonnes = addition_colonnes + carre(colonne_puis_ligne, ligne_puis_colonne);
    end        
    
    
    addition_diag1 = addition_diag1 + carre(ligne_puis_colonne, indice_diag1);
    addition_diag2 = addition_diag2 + carre(ligne_puis_colonne, indice_diag2);
    indice_diag1 = indice_diag1 + 1;
    indice_diag2 = indice_diag2 - 1;
        
    liste_resultats_lignes = [liste_resultats_lignes, addition_lignes]; 
    liste_resultats_colonnes = [liste_resultats_colonnes, addition_colonnes];
end
liste_resultats_diag1 = [liste_resultats_diag1, addition_diag1];
liste_resultats_diag2 = [liste_resultats_diag2, addition_diag2];


clc
disp(carre)
disp([newline, 'Liste des sommes lignes:', newline, num2str(liste_resultats_lignes)])
disp(['Liste des sommes colonnes:', newline, num2str(liste_resultats_colonnes)])
disp(['Liste des sommes diag1:', newline, num2str(liste_resultats_diag1)])
disp(['Liste des sommes diag2:', newline, num2str(liste_resultats_diag2)])