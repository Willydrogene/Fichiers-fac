import numpy as np
import matplotlib.pyplot as plt

def ly(x):
    return 95 - (12 * (4 + (x/30)**4))


def f(x, ρ, g, H, L):
    ff = ρ*g*(H-x)*L
    fL = ρ*g*(H-x)*ly(x) 
    return fL

# Ma fonction pas très précise d'intégrale
def rectangle_a_gauche(a, b, n):
    h = (b-a) / n
    somme = 0
    for i in range(n):
        somme += f(a + i*h, ρ, g, H, L)
    somme *= h
    return somme

# Ma fonction un peu plus précise d'intégrale
def rectangle_point_milieu(a, b, n):
    h = (b-a) / n
    somme = 0
    for i in range(n):
        somme += f(a + (i+0.5)*h, ρ, g, H, L)
    somme *= h
    return somme

# Ma fonction qui est encore plus précise
def trapeze(a, b, n):
    h = (b-a) / n
    somme = (f(a, ρ, g, H, L) + f(b, ρ, g, H, L)) /2
    for i in range(1, n):
        somme += f(a+i*h, ρ, g, H, L)
    somme *= h
    return somme

# Ma fonction qui calcule les erreurs des deux fonctions
def erreur(valeur_attendu, resultat_gauche, resultat_milieu, valeurs_erreurs_gauche, valeurs_erreurs_milieu, valeurs_erreurs_trapeze, a, b, n):
    liste = []
    for i in range(1, n+1, 1):
        liste.append(i)
        erreur_gauche = abs(valeur_attendu - rectangle_a_gauche(a, b, i))
        erreur_milieu = abs(valeur_attendu - rectangle_point_milieu(a, b, i))
        erreur_trapeze = abs(valeur_attendu - trapeze(a, b, i))
        valeurs_erreurs_gauche.append(erreur_gauche)
        valeurs_erreurs_milieu.append(erreur_milieu)
        valeurs_erreurs_trapeze.append(erreur_trapeze)  
        
    return liste, valeurs_erreurs_gauche, valeurs_erreurs_milieu, valeurs_erreurs_trapeze
        

valeurs_erreurs_gauche = []
valeurs_erreurs_milieu = []
valeurs_erreurs_trapeze = []

################################## Valeurs à compléter ############################################
H = 22
ρ = 1000
g = 9.8
L = 95

a = 0
b = H
n = 11
###################################################################################################


resultat_gauche = rectangle_a_gauche(a, b, n)
resultat_milieu = rectangle_point_milieu(a, b, n)
resultat_trapeze = trapeze(a, b, n)

x = np.linspace(a, b, n)

valeur_attendu = (1/2) * ρ * g * ly(x) * H**2

print("Méthode des rectangles à gauche: ", resultat_gauche)
print("Méthode des rectangles au point milieu: ", resultat_milieu)
print("Méthode des trapèzes: ", resultat_trapeze, "\n")
print("Valeur attendue:", valeur_attendu, "\n")
print("Erreur rect gauche:", valeur_attendu - resultat_gauche, "\nErreur rect milieu:", 
      valeur_attendu - resultat_milieu, "\nErreur trapeze:", valeur_attendu - resultat_trapeze, "\n")



# Taille du plot
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10,5))
fig.suptitle('Méthodes des rectangles')


# Premier plot en haut à gauche de ma première fonction
plt.subplot(2,2,1)
plt.plot(x, f(x, ρ, g, H, L), label='sin(x)')
plt.bar(x[:-1], f(x[:-1], ρ, g, H, L), width=(b-a)/n, align='edge', edgecolor='black', alpha=0.5)
plt.fill_between(x, f(x, ρ, g, H, L), color='blue', alpha=0.2, where=(x >= a) & (x <= b))
plt.text(0.1, 0.9, f'Resultat: {resultat_gauche:.2f}', transform=plt.gca().transAxes)
plt.title("Rectangles à gauche")


# Deuxième plot en haut à droite de ma deuxième fonction
plt.subplot(2,2,2)
plt.plot(x, f(x, ρ, g, H, L), label='sin(x)')
plt.bar(x[:-1]+(b-a)/(2*n), f(x[:-1]+(b-a)/(2*n), ρ, g, H, L), width=(b-a)/n, align='center', edgecolor='black', alpha=0.5)
plt.fill_between(x, f(x, ρ, g, H, L), color='blue', alpha=0.2, where=(x >= a) & (x <= b))
plt.text(0.1, 0.9, f'Resultat: {resultat_milieu:.2f}', transform=plt.gca().transAxes)
plt.title("Rectangles au point milieu")

# Troisième plot en bas à gauche de ma deuxième fonction
ax = fig.add_subplot(2, 2, 3)
ax.plot(x, f(x, ρ, g, H, L), label='sin(x)')
ax.fill_between(x, f(x, ρ, g, H, L), color='blue', alpha=0.2, where=(x >= a) & (x <= b))
ax.axhline(y=0, color='black')
ax.axvline(x=0, color='black')
ax.set_title('Approximation de l\'intégrale par la méthode des trapèzes')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
# Afficher les barres verticales représentant les approximations de l'intégrale pour chaque sous-intervalle
h = (b-a)/n
for i in range(n):
    xi = a + i*h
    ax.bar(xi, f(xi, ρ, g, H, L), width=h, align='edge', alpha=0.5, edgecolor='black')
    # Afficher le résultat de l'approximation de l'intégrale
ax.text(0.1, 0.9, f'Resultat: {resultat_trapeze:.2f}', transform=ax.transAxes)

# Quatrième plot de mes erreurs de fonctions
liste_n, valeurs_erreurs_gauche, valeurs_erreurs_milieu, valeurs_erreurs_trapeze = erreur(valeur_attendu, resultat_gauche, resultat_milieu, valeurs_erreurs_gauche, valeurs_erreurs_milieu, valeurs_erreurs_trapeze, a, b, n)
plt.subplot(2,2,4)
plt.yscale('log')
plt.xscale('log')
plt.plot(liste_n, valeurs_erreurs_gauche, label='erreurs gauche', color='r')
plt.plot(liste_n, valeurs_erreurs_milieu, label='erreurs milieu', color='g')
plt.plot(liste_n, valeurs_erreurs_trapeze, label='erreurs trapèze', color='b')

#print(liste_n)
#print('valeurs_erreurs_gauche:',valeurs_erreurs_gauche)
#print('valeurs_erreurs_milieu:',valeurs_erreurs_milieu)
#print('valeurs_erreurs_trapeze:',valeurs_erreurs_trapeze)

plt.grid()
#plt.legend()
plt.tight_layout()
plt.show()
