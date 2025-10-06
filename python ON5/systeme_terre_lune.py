import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import time


class Objets_Celestes:
    def __init__(self, nom, masse, rayon, vit_siderale, couleur, x0, y0, x_point0, y_point0, Nt):
        self.nom = nom
        self.masse = masse
        self.rayon = rayon
        self.vit_siderale = vit_siderale
        self.couleur = couleur
        self.x, self.y = np.zeros(Nt), np.zeros(Nt)
        self.x_point, self.y_point = np.zeros(Nt), np.zeros(Nt)
        self.x[0], self.y[0] = x0, y0
        self.x_point[0], self.y_point[0] = x_point0, y_point0
        tous_les_objets.append(self)

    def acceleration(self, objets_celestes, x, y, n):
        acceleration_totale_x, acceleration_totale_y, contact = 0, 0, False
        for i, autre_objet in enumerate(objets_celestes):
            if autre_objet is not self:  # Ignorer l'objet lui-même
                # Calculer la distance entre les deux objets
                distance_x = x - autre_objet.x[n]
                distance_y = y - autre_objet.y[n]
                distance = (distance_x ** 2 + distance_y ** 2) ** 0.5

                if self.masse < autre_objet.masse:
                    if ((autre_objet.rayon + self.rayon) / (
                            distance)) >= 1.0:  # and (round(contact_y, int(np.log10(1000000/dt))) <= 0.0) and self.nom!='Soleil':
                        contact = True
                        contact_avec[0] = autre_objet
                        acceleration_totale_x, acceleration_totale_y = 0, 0
                        break
                acceleration_x = -G*autre_objet.masse*distance_x/distance**3
                acceleration_y = -G*autre_objet.masse*distance_y/distance**3
                # Ajouter l'accélération à l'accélération totale
                acceleration_totale_x += acceleration_x
                acceleration_totale_y += acceleration_y

        return acceleration_totale_x, acceleration_totale_y, contact

    def calculs_positions(self, i, dt):
        # Calcul des coefficients k1
        k1_x = self.x_point[i - 1]
        k1_y = self.y_point[i - 1]
        acc_x, acc_y, contact1 = self.acceleration(objets_celestes, self.x[i - 1], self.y[i - 1], i - 1)
        k1_x_point = acc_x
        k1_y_point = acc_y

        # Calcul des coefficients k2
        k2_x = self.x_point[i - 1] + 0.5 * dt * k1_x_point
        k2_y = self.y_point[i - 1] + 0.5 * dt * k1_y_point
        acc_x, acc_y, contact2 = self.acceleration(objets_celestes, self.x[i - 1] + 0.5 * dt * k1_x,
                                                   self.y[i - 1] + 0.5 * dt * k1_y, i - 1)
        k2_x_point = acc_x
        k2_y_point = acc_y

        # Calcul des coefficients k3
        k3_x = self.x_point[i - 1] + 0.5 * dt * k2_x_point
        k3_y = self.y_point[i - 1] + 0.5 * dt * k2_y_point
        acc_x, acc_y, contact3 = self.acceleration(objets_celestes, self.x[i - 1] + 0.5 * dt * k2_x,
                                                   self.y[i - 1] + 0.5 * dt * k2_y, i - 1)
        k3_x_point = acc_x
        k3_y_point = acc_y

        # Calcul des coefficients k4
        k4_x = self.x_point[i - 1] + dt * k3_x_point
        k4_y = self.y_point[i - 1] + dt * k3_y_point
        acc_x, acc_y, contact4 = self.acceleration(objets_celestes, self.x[i - 1] + dt * k3_x,
                                                   self.y[i - 1] + dt * k3_y, i - 1)
        k4_x_point = acc_x
        k4_y_point = acc_y

        # Mise à jour des valeurs de position et vitesse
        if ((contact1 == True) or (contact2 == True) or (contact3 == True) or (contact4 == True)) and i > 1:
            cont[0] += 1
            if cont[0] != nouveau_i[0] - 1:
                x_test = self.x[i - 1] + (dt / 6) * (k1_x + 2 * k2_x + 2 * k3_x + k4_x)
                t = np.arccos(x_test / (contact_avec[0].rayon + self.rayon)) / contact_avec[0].vit_siderale
                nouveau_i[0] = int(t * Nt / tmax)
                cont[0] = nouveau_i[0] - 1
                print('ici', i)
            self.x[i] = (contact_avec[0].rayon + self.rayon) * np.cos(
                contact_avec[0].vit_siderale * (tmax / Nt) * (nouveau_i[0]))
            self.y[i] = (contact_avec[0].rayon + self.rayon) * np.sin(
                contact_avec[0].vit_siderale * (tmax / Nt) * (nouveau_i[0]))

            self.x_point[i] = -(contact_avec[0].rayon + self.rayon) * contact_avec[0].vit_siderale * np.sin(
                contact_avec[0].vit_siderale * (tmax / Nt) * (nouveau_i[0]))
            self.y_point[i] = (contact_avec[0].rayon + self.rayon) * contact_avec[0].vit_siderale * np.cos(
                contact_avec[0].vit_siderale * (tmax / Nt) * (nouveau_i[0]))
        else:
            self.x[i] = self.x[i - 1] + (dt / 6) * (k1_x + 2 * k2_x + 2 * k3_x + k4_x)
            self.y[i] = self.y[i - 1] + (dt / 6) * (k1_y + 2 * k2_y + 2 * k3_y + k4_y)

            self.x_point[i] = self.x_point[i - 1] + (dt / 6) * (
                    k1_x_point + 2 * k2_x_point + 2 * k3_x_point + k4_x_point)
            self.y_point[i] = self.y_point[i - 1] + (dt / 6) * (
                    k1_y_point + 2 * k2_y_point + 2 * k3_y_point + k4_y_point)

        if i != i_davant[0]:
            i_davant[0] = i
            nouveau_i[0] += 1

        return self.x, self.y, self.x_point, self.y_point



def plot_final(color, x, y, x_point, y_point, nom, rayon, pos_text):
    axs[0].plot(x, y, color, label=nom)
    axs[0].add_artist(plt.Circle((x[0], y[0]), rayon, color=color, alpha=0.7))
    axs[0].text(x[0], y[0], nom, ha='left', va=pos_text, color='white')
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('y')
    axs[0].set_title('Position des astres sur ' + str(tmax / (3600 * 24)) + ' jours')
    #axs[0].grid(True)
    axs[0].legend()
    axs[0].tick_params(axis='x', colors='white')  # Couleur des graduations de l'axe X en blanc
    axs[0].tick_params(axis='y', colors='white')

    # plt.subplot(1, 2, 2)
    axs[1].plot(x_point, y_point, color, label=nom)
    axs[1].plot(x_point[0], y_point[0], color, marker='o')
    axs[1].set_xlabel('Vitesse x')
    axs[1].set_ylabel('Vitesse y')
    axs[1].set_title('Vitesse des astres')
    #axs[1].grid(True)
    axs[1].legend()
    axs[1].tick_params(axis='x', colors='white')  # Couleur des graduations de l'axe X en blanc
    axs[1].tick_params(axis='y', colors='white')


tmin = 0
tmax = 3600 * 24 * 36
dt = 10  # mettre 1000 pour 365jours
Nt = int((tmax - tmin) / dt) + 1
t = np.linspace(tmin, tmax, Nt)

dist_terre_lune = 384400 * 10 ** 3
dist_terre_soleil = 149597870 * 10 ** 3
G = 6.67 * 10 ** (-11)

tous_les_objets = []
nb_etages = []
liste_plots_fusee = []
u = [0]
k = [0]
cont = [-1]
nouveau_i = [0]
contact_avec = [0]
i_davant = [0]


vit_terre = 0
terre = Objets_Celestes('Terre', 5.972 * 10 ** 24, 6371 * 10 ** 3, 7.2921159*10**(-5),
                        'b', 0.0, 0.0, 0.0, vit_terre, Nt)

vit_lune = (np.sqrt((G * terre.masse) / dist_terre_lune))
lune = Objets_Celestes('Lune', 7.36 * 10 ** 22, 1737.4 * 10 ** 3, 2.664*10**(-6),
                       '#D3D3D3', dist_terre_lune, 0.0, 0.0, vit_lune, Nt)



objets_celestes = [terre]
# objets_celestes = [soleil, terre, lune, mercure]  # Les objets qui intéragissent en gravitation
# tous_les_objets = [soleil, terre, lune, fusee, mercure]  # La totalité des objets que je veux calculer


start_time = time.perf_counter()
start_time_estimation = time.perf_counter()
progress = 0
for i in range(1, Nt):
    for objet in tous_les_objets:
        objet.calculs_positions(i, dt)

    # Calcul du pourcentage d'avancement
    new_progress = int((i / Nt) * 100)
    if new_progress != progress:
        print(f"Avancement : {new_progress}%")
        progress = new_progress

    if i == 1:
        sec, minu = 'secondes', 'min'
        end_time_estimation = time.perf_counter()  # Enregistrer le temps de fin d'exécution
        execution_time_estimation = (end_time_estimation - start_time_estimation) * (
                    Nt - i)  # Calculer la durée totale d'exécution
        if execution_time_estimation >= 60:
            print(
                f"Il reste environ : {int(execution_time_estimation / 60)}{minu} et {(execution_time_estimation / 60 % 1) * 60:.6f}",
                sec)
        else:
            print(f"Il reste environ : {execution_time_estimation:.6f}", sec)


end_time = time.perf_counter()  # Enregistrer le temps de fin d'exécution
execution_time = end_time - start_time  # Calculer la durée totale d'exécution
print(f"Temps d'exécution : {execution_time:.6f} secondes")

fig, axs = plt.subplots(1, 2, figsize=(11, 7))
for i, objet in enumerate(tous_les_objets):
    plot_final(objet.couleur, objet.x, objet.y, objet.x_point, objet.y_point, objet.nom, objet.rayon, 'top')


plt.tight_layout()
axs[0].set_facecolor('black')
axs[1].set_facecolor('black')

axs[0].set_xlim(-(lune.rayon+lune.x[0]), lune.rayon*2+lune.x[0])
axs[0].set_ylim(-(lune.rayon+lune.x[0]), lune.rayon*2+lune.x[0])

axs[1].set_aspect('equal')
plt.show()

