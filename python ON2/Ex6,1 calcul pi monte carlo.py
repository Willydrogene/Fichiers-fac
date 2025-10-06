import random as rd
import numpy as np
import matplotlib.pyplot as plt



def remplissage(n, a):
    liste1 = []
    liste2 = []
    for i in range(n):
        liste1.append(rd.uniform(-a/2,a/2))
        liste2.append(rd.uniform(-a/2, a/2))
    return liste1, liste2


def cercle(a):
    x0, y0 = 0, 0
    theta = np.linspace(0, 2*np.pi, 100)
    x = x0 + a/2 * np.cos(theta)
    y = y0 + a/2 * np.sin(theta)
    
    return x, y


def compter(a, do_plot=False):
    liste1, liste2 = remplissage(n, a)
    liste1 = np.array(liste1)
    liste2 = np.array(liste2)
    x, y = cercle(a)
    danscercle = np.sum(liste1**2 + liste2**2 <= (a/2))
    horscercle = np.sum(liste1**2 + liste2**2 > (a/2))
    
    liste1_in = liste1[np.where(liste1**2 + liste2**2 <= (a/2),)]
    liste2_in = liste2[np.where(liste1**2 + liste2**2 <= (a/2),)]
    liste1_out = liste1[np.where(liste1**2 + liste2**2 > (a/2),)]
    liste2_out = liste2[np.where(liste1**2 + liste2**2 > (a/2),)]
    
    if do_plot:
        # Tracer les points dans le cercle avec une couleur différente
        plt.figure(figsize=(13, 10))
        plt.subplot(1,2,1)
        plt.plot(liste1_in, liste2_in, 'o', color='b', label="Points dans le cercle: " + str(danscercle))
        plt.plot(liste1_out, liste2_out, 'o', color='g', label="Points à l'extérieur du cercle: " + str(horscercle))
        plt.plot(x, y)
        plt.plot(x, y, color='red')
        plt.fill(x, y, color='red', alpha=0.2)
        plt.title("Graphique des points aléatoires")
        plt.xlabel('Axe X')
        plt.ylabel('Axe Y')
        plt.axis('equal')
        plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=2)
        plt.grid()
        plt.tight_layout()
        plt.rcParams.update({'font.size': 15})
    return danscercle, horscercle


n = int(input("n choisi: "))
a = 2


#print(liste1, '\n')
#print(liste2)

erreurs = []
nb_n = []
do_plot = False
for i in range(1,n+1):
    liste1, liste2 = remplissage(i, a)
    cercle(a)
    if i == n:
        do_plot = True
    danscercle, horscercle = compter(a, do_plot)
    rapport = (danscercle / i) * a**2
    erreurs.append(abs(np.pi - rapport))
    nb_n.append(i)
    

plt.subplot(1, 2, 2)
plt.plot(nb_n, erreurs, label='erreurs')
plt.xlabel('n')
plt.ylabel('Erreurs')
plt.legend()

texte = "La valeur de pi est {:.15f}".format(rapport)
plt.text(0.5, -0.1, texte, ha='center', va='center', transform=plt.gca().transAxes)
plt.grid()
print("Nombre de points dans le cercle est de:", danscercle, "\nLe nombre de points à l'extérieur du cercle:", horscercle)
print(rapport)

plt.tight_layout()
plt.show()
