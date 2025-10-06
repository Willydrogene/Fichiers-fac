import numpy as np
import matplotlib.pyplot as plt


def est_dans_cardioide(x, y):
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    cardioide = 1 - np.cos(theta)
    if r <= cardioide:
        return True
    else:
        return False


def aire_cardioide(n):
    points_dans_cardioide = 0
    total_points = n

    for _ in range(n):
        x = np.random.uniform(-2, 2)
        y = np.random.uniform(-2, 2)
        if est_dans_cardioide(x, y):
            points_dans_cardioide += 1

    aire_estimee = (points_dans_cardioide / total_points) * 16  # 16 est l'aire du carré [-2, 2] x [-2, 2]
    return aire_estimee


def calculer_a(n):
    return aire_cardioide(n)


def calculer_ln_n(n):
    return np.log(n)


imax = 10
n_values = [10 + 3**i for i in range(1, imax+1)]
a_values = [calculer_a(n) for n in n_values]

# Vérifier et remplacer les valeurs négatives par NaN
a_values = np.where(np.array(a_values) < 0, np.nan, a_values)

ln_n_values = [calculer_ln_n(n) for n in n_values]
ln_a_values = np.log(a_values)
ln_S = np.log(3 * np.pi / 2)

aire_obtenue = a_values[-1]  # Récupérer la dernière valeur d'aire calculée
aire_attendue = 3 * np.pi / 2  # Aire attendue

print("Aire obtenue :", aire_obtenue)
print("Aire attendue :", aire_attendue)

plt.plot(ln_n_values, ln_a_values, 'bo-', label='ln(a(n))')
plt.axhline(y=ln_S, color='r', linestyle='--', label='ln(S)')
plt.xlabel('ln(n)')
plt.ylabel('ln(a)')
plt.legend()
plt.show()
