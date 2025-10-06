#!/usr/bin/env python3

### en Linux on peut utiliser directement ce script en ligne de commande par :
###
###   python3 Ising.py
###
### a executer dans le dossier ou on a depose le fichier Ising.py
### et bien sur une fois le code est correctement
### complete pour les parties "???" ...


### si on utilise ce code dans spyder ou jupyter (jupyter-notebook)
##% il faut decommenter la ligne suivante:
##matplotlib
### dans ce cas les figures seront affichees dans des fenetres hors la
### la fenetre de spyder ou jupyter ce qui est plus pratiques pour
### des animations

########################################################
###   TPO numerique de Physique Statistique          ###
###               Programme Ising.py                 ###
###                                                  ###
###   Modele de ferromagnetisme                      ###
###                                                  ###
###   Annee Universitaire 2024-2025                  ###
###   Universite Toulouse III-Paul Sabatier,         ###
###   Licence Flexible de Physique                   ###
###   ND et KF version 3.0                           ###
########################################################

import matplotlib.pyplot as plt
from random import *
from math import *
from statistics import *


nom = 'GERBAUD Willy'

J=1; ### couplage
H=0.0; ### champ magtique externe

Tc=2/log(1+sqrt(2));

T=Tc+1; ### temperature

L=50 ### taille laterale du systme N=L*L

tsim=100; ### temps de simulations (en units de N)

tprint=10; ### intervalle entre deux affichages

### t_pause =temps de pause en secondes entre les graphes
### une valeur de 0.0 signifie qu'il faut manuellement avancer figure
### par figure en tappant sur <Entree> (ou 's' pour terminer avant)
t_pause=0.1

### rapport T/Tc arrondi sur 3 chiffres
### (pour affichage dans les figures)
Tr=int(1000*T/Tc+0.5)/1000

### ---- Initialisation

### quelques fonctions utiles (ne pas modifier)

def fig_pause(t):
    if t<=0.0:
        plt.show(block=False)
        res=input("taper <Entree> pour continuer, s pour arreter: ")
        if res=='s':
            print('=> last iteration et derniere figure ')
            return 1
    else:
        plt.pause(t)
    return 0

def modulo(a,b):
    return a%b

#######################################################

### RAPPEL: Utiliser la fonction random() qui retourne un nombre
### x reel aleatoire tel que 0 <= x < 1
### ou randint(a,b) qui retourne un entier aleatoire n tel que a <= n <= b

seed(1756567);

### creation de la condition initiale
S=[]
for p in range(L):
    line=[]
    for q in range(L):
        ### valeur initiale du spin a la position (p,q)
        ### Ici coder les differents cas pour la condition initiale
        ### par exemple aleatoire
        ### ou configuration avec -1 dans un cercle et +1 dehors du cercle
        valeur_spin=2*randint(0,1)-1;
        line.append(valeur_spin)
    S.append(line)

mag=sum([sum(x) for x in S])/L/L
M=[mag]
temp=[0]

### ---- Algorithme de Metropolis 

for t in range(tsim+1):
    if t_pause<=0:
        plt.close()
    for k in range(L*L):
        #### ruse pour afficher la 1ere condition initiale
        #### et la figure pour t=0 sans faire de simulation
        if t==0: break

        ### choix aleatoire de la position i=(p,q) du spin 
        p=???
        q=???
        ### calculer ici la somme "somme4v=\sum_j S_j"
        ### sur les voisins j directes du spin i choisi
        somme4v=???
        ### 
        ### Ensuite il faut trouver analytiquement l'expression
        ### de la difference d'energie DeltaE=H(C2)-H(C1)
        ### ou C1=la configuration initiale des spins et C2 celle
        ### ou uniquement la valeur d'un seul spin S_i a la postion i
        ### a modifiee vers (-S_i)
        ### Montrer que DeltaE est une expression simple de somme4v
        ### la valeur de S_i (attention: S_i=S[p][q] et similaire pour S_j
        ### si j est une autre postion avec d'autres valeurs pour p et q.
        DeltaE=2*
        ### implementer le test de la condition quand il faut valider
        ### le changement du spin
        if DeltaE<0:
            S[p][q]=-S[p][q]
    if t%tprint==0:
        print('t = ',t)
        S1=[[S[x][y]+1 for y in range(L)] for x in range(L)]
        plt.clf()
        plt.spy(S1)
        plt.title('T/T_c = '+str(Tr)+' ,  t = '+str(t))
        
        mag=sum([sum(x) for x in S])/L/L
        M.append(mag)
        temp.append(t)

        if fig_pause(t_pause)>0: break        

fig, (ax3) = plt.subplots(1,constrained_layout=True)
ax3.plot(temp,M)
ax3.set(title=nom+' - Aimentation moyenne en fonction du temps',xlabel='t',ylabel='M/N')

ksi=sqrt(variance(M)*L*L)
print('ksi = ',ksi)

plt.show()
