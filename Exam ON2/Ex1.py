import numpy as np
import matplotlib.pyplot as plt


def bale(nmax):
    somme = 0
    liste_nmax = [0]
    liste = [somme]
    for i in range(1, nmax):
        somme += 1/(i**2)
        print(somme)
        liste.append(somme)
        liste_nmax.append(i)
    return liste, liste_nmax
        
        

nmax = 15

liste, liste_nmax = bale(nmax)
print(len(liste))
print(len(liste_nmax))

resultat_attendu = np.pi**2/6
erreur = resultat_attendu - liste[-1]

print('Il y a une différence de:', erreur)

plt.title('Somme')
plt.plot(liste, liste_nmax, label='Somme 1 -> {} de 1/n**2'.format(nmax))
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()