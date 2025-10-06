import numpy as np
import matplotlib.pyplot as plt

# Chargement des données
data = np.loadtxt("osc_exp.txt", delimiter=" ")

# Séparation des colonnes
t = data[:, 0]       # Temps
theta = data[:, 1]   # Position angulaire
omega = data[:, 2]   # Vitesse angulaire

# Tracé des résultats
plt.figure(figsize=(10, 5))

plt.subplot(2, 1, 1)
plt.plot(t, theta, label=r"$\theta(t)$", color="b")
plt.xlabel("Temps (s)")
plt.ylabel("Angle (rad)")
plt.legend()
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(t, omega, label=r"$\omega(t)$", color="r")
plt.xlabel("Temps (s)")
plt.ylabel("Vitesse angulaire (rad/s)")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
