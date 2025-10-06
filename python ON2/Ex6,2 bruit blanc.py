import numpy as np
import matplotlib.pyplot as plt

amplitude = 1.0
frequence = 1000.0
duree = 0.01
nb_echantillons = 10000
temps = np.linspace(0, duree, nb_echantillons)

signal_sinusoidal = amplitude * np.sin(2 * np.pi * frequence * temps)

moyenne = 0.0
ecart_type_bruit = 0.2

bruit_fond = np.random.normal(moyenne, ecart_type_bruit, nb_echantillons)
signal_bruite_fond = signal_sinusoidal + bruit_fond

ecart_types = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3]
fig, axs = plt.subplots(2, 3, figsize=(15, 10))

for i, ax in enumerate(axs.flatten()):
    ecart_type = ecart_types[i]
    bruit = np.random.normal(moyenne, ecart_type, nb_echantillons)
    signal_bruite = signal_sinusoidal + bruit
    ax.hist(signal_sinusoidal, bins=50, alpha=0.5, label='Signal initial', color='b')
    ax.hist(signal_bruite, bins=50, alpha=0.5, label='Signal bruité', color='r')
    ax.hist(signal_bruite_fond, bins=50, alpha=0.5, label='Signal bruité avec bruit de fond', color='g')
    ax.set_title('Écart-type = {}'.format(ecart_type))
    ax.legend()

    if np.std(signal_bruite) > np.std(signal_sinusoidal):
        print('Le signal est noyé dans le bruit pour un écart-type de {}'.format(ecart_type))

plt.show()
