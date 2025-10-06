#!/usr/bin/env python3

"""
-----------------------------------------
ATTENTION:
par defaut le code ci-dessous pour la fct. faire_plot(...)
est prevu pour un usage en ligne de commande:

python3 fichier.py

si fichier.py est le nom du fichier python qu'on utilise

Si on utilise spyder ou jupyter il faut commenter et decommenter
certaines lignes (2-3 lignes) ci-dessous pour assurer
le bon fonctionnement technique, voir ci-dessous
-----------------------------------------
"""

import random as rd
from math import *
import matplotlib.pyplot as plt

### propostion de parametres 

np=120 ## nombre de particules 
vmax=1 
xmax=2
m=1
g=1
dt=0.05
dv=0.5
vsolmax=1
niter=20 ## nombre d'iterations globales de pas "ntherm*dt"
ntherm=40 ## nombre d'iterations de pas "dt" entre les plots et echanges aleatoires de vitesses

## On peut encore definir/ajouter d'autres parametres



## ----> decommenter la ligne suivante si on est en jupyter-notebook !!!!
#%matplotlib

## ----> commenter la ligne suivante si on est en spyder !!!!
fig, (ax1,ax2) = plt.subplots(2,constrained_layout=True)


"""
la fonction <faire_plot> ci-dessous est une fonction pour afficher
les deux histogramme de x et v dans une figure et aussi 
tracer les deux courbes theoriques avec affichage de 0.1 secondes

Les parametres sont :
x = liste/tableau des postions x[j] des particules 
v = liste/tableau des vitesses v[j] des particules
Ces deux tableaux sont obtenus par la simulation numeriques.

xarg = liste/tableau technique avec des valeurs equidistantes entre
   xmin et xmax pour la commande plot (choisir xmin=0, xmax=max(x)
   et entre 100 et 1000 points mais
   il faut le faire avant l'appel de la fct. faire_plot)
pxth = liste/tableau de la meme longueur de xarg et contenant
   les valeurs theoriques de la distribution de positions :
   p_{1,th}(xarg[j]) (j=0,...,len(xarg)-1)
   a calculer soi meme avant
varg = liste/tableau technique avec des valeurs equidistantes entre
   vmin et vmax pour la commande plot (choisir vmax=max(max(v),abs(min(v)), 
   vmin=-vmax et entre 100 et 1000 points, mais avant dans une autre fct./code)
pvth = liste/tableau de la meme longueur de varg et contenant
   les valeurs theoriques de la distribution des vitesses :
   p_{2,th}(varg[j]) (j=0,...,len(varg)-1)
   a calculer soi meme avant

t = temps d'iteration, c'est seulement utilise pour un label dans la figure
beta = valeur de beta (temperature) inverse, aussi seulement utilise
pour un label dans la figure

"""

def faire_plot(x,v,xarg,pxth,varg,pvth,t,beta):
    nbx=20 ## nombre de boites de l'histogramme de x
    nbv=16 ## nombre de boites de l'histogramme de v
    t_pause=0.1 ## temps d'affichage pour un plot 
    ## ----> decommenter la ligne suivante si on est en spyder !!!!!
    #fig, (ax1,ax2) = plt.subplots(2,constrained_layout=True)
    ax1.cla()
    ax1.hist(x,bins=nbx,color='white',edgecolor='blue',density=True,\
             label='histogramme')
    ax1.set(title='distribution des positions',xlabel='x',ylabel='p(x)')
    ax1.plot(xarg,pxth,'y',label='theorie')
    ax1.legend()
    
    ax2.cla()
    ax2.hist(v,bins=nbv,color='white',edgecolor='blue',density=True,\
                          label='histogramme')
    ax2.set(title='distribution des vitesses',xlabel='v',ylabel='p(v)')
    ax2.plot(varg,pvth,'y',label='theorie')
    ax2.legend()
    fig.suptitle('N = {0:d}   t = {1:d}   T = {2:.5g}'.format(len(x),t,1/beta))
    plt.pause(t_pause)
    
