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
                if ((autre_objet.rayon + self.rayon) / (distance)) >= 1.0:
                    # print('ON Y EST', (autre_objet.rayon+self.rayon)/(round(distance, int(np.log10(0.01/dt)))))
                    # print((autre_objet.rayon+self.rayon)/distance)
                    contact = True
                    contact_avec[0] = autre_objet
                    break
                acceleration_x = -G * autre_objet.masse * distance_x / distance ** 3
                acceleration_y = -G * autre_objet.masse * distance_y / distance ** 3
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
                print('ici', i, t)
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


class Fusee(Objets_Celestes):
    def acceleration(self, objets_celestes, x, y, n):
        ref_terr_x = terre.x[n]
        ref_terr_y = terre.y[n]
        for i, objet in enumerate(objets_celestes):
            objet.x[n] -= ref_terr_x  # On se met dans le référentiel terrestre
            objet.y[n] -= ref_terr_y

        conso_par_sec, sec_par_pas = (nb_etages[nb_etages_pop[0]].masse[0] - nb_etages[nb_etages_pop[0]].masse_vide) / \
                                     nb_etages[nb_etages_pop[0]].duree_fct, tmax / Nt
        conso_par_pas = conso_par_sec * sec_par_pas
        if nb_etages_pop[0] < 2:
            nb_etages[nb_etages_pop[0]].masse[n] = nb_etages[nb_etages_pop[0]].masse[n - 1] - conso_par_pas
            if nb_etages[nb_etages_pop[0]].masse[n] <= nb_etages[nb_etages_pop[0]].masse_vide:
                print('#########################################')
                print('On est a',
                      ((fusee.x[n] - terre.x[n]) ** 2 + (fusee.y[n] - terre.y[n]) ** 2) ** 0.5 - terre.rayon, 'm')
                print('#########################################')
                print('vitesse nécessaire=', (np.sqrt(
                    (G * terre.masse) / (((fusee.x[n] - terre.x[n]) ** 2 + (fusee.y[n] - terre.y[n]) ** 2) ** 0.5))))
                print('vitesse actuelle=', (fusee.x_point[n] ** 2 + fusee.y_point[n] ** 2) ** 0.5, fusee.x_point[n],
                      fusee.y_point[n])
                nb_etages_pop[0] += 1
                liste_plots_fusee.append(n)
        elif nb_etages_pop[0] == 2 and u[0] == 0:
            nb_etages[nb_etages_pop[0]].masse[n] = nb_etages[nb_etages_pop[0]].masse[n - 1] - conso_par_pas
            if nb_etages[nb_etages_pop[0]].masse[n] <= (
                    136 * (nb_etages[nb_etages_pop[0]].masse[0] - nb_etages[nb_etages_pop[0]].masse_vide) / nb_etages[
                nb_etages_pop[0]].duree_fct) + nb_etages[nb_etages_pop[0]].masse_vide:
                print('#########################################')
                print('On est a',
                      ((fusee.x[n] - terre.x[n]) ** 2 + (fusee.y[n] - terre.y[n]) ** 2) ** 0.5 - terre.rayon, 'm')
                print('#########################################')
                print('vitesse nécessaire=', (np.sqrt(
                    (G * terre.masse) / (((fusee.x[n] - terre.x[n]) ** 2 + (fusee.y[n] - terre.y[n]) ** 2) ** 0.5))))
                print('vitesse actuelle=', (fusee.x_point[n] ** 2 + fusee.y_point[n] ** 2) ** 0.5, fusee.x_point[n],
                      fusee.y_point[n])
                liste_plots_fusee.append(n)
                u[0] = 1

        self.masse = sum(elem.masse[n] for elem in nb_etages[nb_etages_pop[0]:])

        acc_x, acc_y, contact = super().acceleration(objets_celestes, x, y,n)  # On calcule l'acc fusée dans le ref terrestre
        # print('             ', n, acc_x, acc_y, (acc_x**2+acc_y**2)**0.5, fusee.x_point[n], fusee.y_point[n], (fusee.x_point[n]**2+fusee.y_point[n]**2)**0.5)
        Fp = nb_etages[nb_etages_pop[0]].poussee_max / self.masse

        etage_actuel = nb_etages_pop[0] + 1
        r_fusee_1 = (fusee.x[n - 1] ** 2 + fusee.y[n - 1] ** 2) ** 0.5
        r_fusee_2 = (fusee.x[n] ** 2 + fusee.y[n] ** 2) ** 0.5

     

        def cherche_angle(angle, angle):
            acc_testx = acc_x + Fp * np.cos(angle)
            acc_testy = acc_y + Fp * np.sin(angle)
            
            fusee_x1 = fusee.x[n-1] + dt * fusee.x_point[n-1]
            fusee_y1 = fusee.y[n-1] + dt * fusee.y_point[n-1]
            fusee_x_point1 = fusee.x[n-1] + dt * acc_testx
            fusee_y_point1 = fusee.y[n-1] + dt * acc_testy
            
            rr = (fusee_x1**2+fusee_y1**2)**0.5
            vit = (fusee_x_point1**2+fusee_y_point1**2)**0.5
            return rr, vit
            
        if etage_actuel >1 and r_fusee_1>(140000+terre.rayon):
            
            angle_1 = 0
            angle_2 = 2*np.pi
            
            precision = 0.001  # Précision de la dichotomie
            
            while abs(angle_2 - angle_1) > precision:
                angle_mid = (angle_1 + angle_2) / 2
                
                rr_1, vit_1 = cherche_angle(angle_1)
                rr_2, vit_2 = cherche_angle(angle_2)
                rr_3, vit_3 = cherche_angle(angle_mid)
                
                
                if (rr_1>(140000+terre.rayon) and rr_2>(140000+terre.rayon) and rr_3>(140000+terre.rayon)) and (rr_1<(200000+terre.rayon) and rr_2<(200000+terre.rayon) and rr_3<(200000+terre.rayon)):
                    if abs(vit_1-vit_3) < abs(vit_2-vit_3):
                        # pas la valeur abs
                    
                    if test_liste[0] < vit:
                        angle_1 = angle_mid
                    
 
    
 
        if etage_actuel == 1 and n > 1:
            if int(sec_par_pas * n) != 15:
                acc_x += Fp
            else:
                acc_y += Fp * 0 / 10  # (fusee.x[n]-terre.x[n]) / ((fusee.x[n]-terre.x[n])**2+(fusee.y[n]-terre.y[n])**2)**0.5
                acc_x += Fp * 10 / 10  # (fusee.y[n]-terre.y[n]) / ((fusee.x[n]-terre.x[n])**2+(fusee.y[n]-terre.y[n])**2)**0.5


        elif etage_actuel == 2:# and int(r_fusee_2) < terre.rayon + 200000:
            acc_x += Fp * np.cos(theta[0])
            acc_y += Fp * np.sin(theta[0])
        elif etage_actuel == 2 and int(r_fusee_2) > terre.rayon + 200000:
            acc_x += 0  # Fp * 1/2
            acc_y += Fp * 1

        elif etage_actuel == 3 and ((fusee.x_point[n] ** 2 + fusee.y_point[n] ** 2) ** 0.5) <= (np.sqrt((G * terre.masse) / (((fusee.x[n] - terre.x[n]) ** 2 + (fusee.y[n] - terre.y[n]) ** 2) ** 0.5))):
            acc_x += Fp * np.sin(theta[0])  # Adapte le force de poussée pour que la fusée aille sur la tangente
            acc_y += Fp * np.cos(theta[0])

        elif etage_actuel == 3 and ((fusee.x_point[n] ** 2 + fusee.y_point[n] ** 2) ** 0.5) > (np.sqrt((G * terre.masse) / (((fusee.x[n] - terre.x[n]) ** 2 + (fusee.y[n] - terre.y[n]) ** 2) ** 0.5))):
            acc_x -= 0  # Fp# * (fusee.y[n]-terre.y[n])/((fusee.x[n]-terre.x[n])**2+(fusee.y[n]-terre.y[n])**2)**0.5
            acc_y += 0  # Fp #Fp #Fp * (fusee.x[n]-terre.x[n])/((fusee.x[n]-terre.x[n])**2+(fusee.y[n]-terre.y[n])**2)**0.5


        for i, objet in enumerate(objets_celestes):
            objet.x[n] += ref_terr_x  # On se remet dans le référentiel héliocentrique
            objet.y[n] += ref_terr_y
        return acc_x, acc_y, contact


class Etage(Fusee):
    def __init__(self, nom, largeur, longueur, masse_avec_ergols, masse_vide, poussee_max, duree_fct, couleur):
        self.nom = nom
        self.largeur = largeur  # diamètre mais en 2d
        self.longueur = longueur
        self.masse = np.full(Nt, masse_avec_ergols)
        self.masse_vide = masse_vide
        self.poussee_max = poussee_max
        self.duree_fct = duree_fct
        self.couleur = couleur
        nb_etages.append(self)


def plot_fusee(t, nb_etages_pop):
    if t == 0:
        x_v, y_v = fusee.x[t] - terre.x[t], fusee.y[t] - terre.y[t]
        r = ((terre.x[t] - fusee.x[t]) ** 2 + (terre.y[t] - fusee.y[t]) ** 2) ** 0.5
    else:
        x_v, y_v = fusee.x[t] - fusee.x[t - 1], fusee.y[t] - fusee.y[t - 1]
        r = ((fusee.x[t - 1] - fusee.x[t]) ** 2 + (fusee.y[t - 1] - fusee.y[t]) ** 2) ** 0.5
        axs[0].text(fusee.x[t], fusee.y[t], nb_etages[nb_etages_pop - 1].nom, ha='left', va='top', color='black')
    L = sum(elem.longueur for elem in nb_etages[nb_etages_pop:])  # Les étages additionnés
    cos0, sin0 = x_v / r, y_v / r
    if t == 0:
        x_arr, y_arr = terre.x[t] + (r - L) * cos0, terre.y[t] + (r - L) * sin0
    else:
        x_arr, y_arr = fusee.x[t - 1] + (r - L) * cos0, fusee.y[t - 1] + (r - L) * sin0
    axs[0].plot(fusee.x[t], fusee.y[t], 'ro')
    longueur = [0]
    for i in range(len(nb_etages[nb_etages_pop:])):
        longueur.append(nb_etages[nb_etages_pop + i].longueur + longueur[i])
    for i, elem in enumerate(nb_etages[nb_etages_pop:]):
        sommet = [(x_arr + elem.largeur * sin0 / 2 + longueur[i] * cos0,
                   y_arr - elem.largeur * cos0 / 2 + longueur[i] * sin0),
                  (x_arr - elem.largeur * sin0 / 2 + longueur[i] * cos0,
                   y_arr + elem.largeur * cos0 / 2 + longueur[i] * sin0),
                  (x_arr - elem.largeur * sin0 / 2 + longueur[i + 1] * cos0,
                   y_arr + elem.largeur * cos0 / 2 + longueur[i + 1] * sin0),
                  (x_arr + elem.largeur * sin0 / 2 + longueur[i + 1] * cos0,
                   y_arr - elem.largeur * cos0 / 2 + longueur[i + 1] * sin0)]
        polygon = Polygon(sommet, closed=True, color=elem.couleur)
        axs[0].add_patch(polygon)


def plot_final(color, x, y, x_point, y_point, nom, rayon, pos_text):
    axs[0].plot(x, y, color, label=nom)
    axs[0].add_artist(plt.Circle((x[0], y[0]), rayon, color=color, alpha=0.7))
    if nom == 'Fusée':
        plot_fusee(0, 0)
        for i in range(len(liste_plots_fusee)):
            plot_fusee(liste_plots_fusee[i], i + 1)
    if nom == 'Terre':
        for i in range(len(liste_plots_fusee)): axs[0].add_artist(
            plt.Circle((terre.x[liste_plots_fusee[i]], terre.y[liste_plots_fusee[i]]), rayon, color='b', alpha=0.7))
    axs[0].text(x[0], y[0], nom, ha='left', va=pos_text, color='black')
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('y')
    axs[0].set_title('Position des astres sur ' + str(tmax / (3600 * 24)) + ' jours')
    axs[0].grid(True)
    axs[0].legend()

    # plt.subplot(1, 2, 2)
    axs[1].plot(x_point, y_point, color, label=nom)
    axs[1].plot(x_point[0], y_point[0], color, marker='o')
    axs[1].set_xlabel('Vitesse x')
    axs[1].set_ylabel('Vitesse y')
    axs[1].set_title('Vitesse des astres')
    axs[1].grid(True)
    axs[1].legend()


tmin = 0
tmax = 3600 * 1 * 1
dt = 0.1  # mettre 1000 pour 365jours
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
theta = [np.pi/4]

test_liste = [0]
test_liste2 = []

# soleil = Objets_Celestes('Soleil', 2*10**30, 696340*10**3, 30*10**3, 'y', 0.0, 0.0, 0.0, 0.0, Nt)

vit_terre = 0  # np.sqrt((G * soleil.masse) / (dist_terre_soleil)) + np.sqrt((G * 7.36*10**22) / (dist_terre_lune))
terre = Objets_Celestes('Terre', 5.972 * 10 ** 24, 6371 * 10 ** 3, 7.2921159 * 10 ** (-5), 'b', 0.0, 0.0, 0.0,
                        vit_terre, Nt)

vit_lune = (np.sqrt((G * terre.masse) / (dist_terre_lune)))
# lune = Objets_Celestes('Lune', 7.36*10**22, 1737.4*10**3, 16.7/3.6, 'r', dist_terre_lune, 0.0, 0.0, vit_lune,  Nt)

# vit_lunet = (np.sqrt((G * terre.masse) / (dist_terre_lune)))
# lunet = Lunet('Lune_ss_sol', 7.36*10**22, 1737.4*10**3, '#999999', dist_terre_lune, 0.0, 0.0, vit_lunet, Nt)

# vit_mercure = (np.sqrt((G * soleil.masse) / (63.524*10**9)))
# mercure = Objets_Celestes('Mercure', 3.285*10**23, 2439.7*10**3, 10.892/3.6, '#999999', 63.524*10**9, 0.0, 0.0, vit_mercure, Nt)

etage_1 = Etage('Etage 1', 10.1, 42.1, 2279 * 10 ** 3, 130.4 * 10 ** 3, 33.4 * 10 ** 6, 162, 'g')
etage_2 = Etage('Etage 2', 10.1, 24.8, 481 * 10 ** 3, 36.5 * 10 ** 3, 5 * 10 ** 6, 386, 'b')
etage_3 = Etage('Etage 3', 6.6, 17.9, 107 * 10 ** 3, 11.3 * 10 ** 3, 1 * 10 ** 6, 136 + 335, 'y')
module_lunaire_descente = Etage('Module lunaire de descente', 4.27, 7, 14658, 4747, 45040, 12 * 60, 'm')
module_lunaire_remontee = Etage('Module lunaire de remontée', 4.2, 3.2, 4747, 2361, 15600, 7 * 60, 'b')
module_service = Etage('Module de service', 3.9, 7.6, 90000, 24523, 91, 35 * 3600,
                       'g')  # durée d'util indet car: pour les corrections de traj
module_commande = Etage('Module de commande', 3.9, 3.9, 5806, 5806, 0, 35 * 3600, 'r')  # idem
nb_etages_pop = [0]

longueur_fusee = sum(elem.longueur for elem in nb_etages)
masse_fusee = sum(elem.masse[0] for elem in nb_etages[nb_etages_pop[0]:])
vit_fusee = (terre.rayon + longueur_fusee) * terre.vit_siderale
print(vit_fusee, masse_fusee)
fusee = Fusee('Fusée', masse_fusee, longueur_fusee, 0, 'm', (terre.rayon + longueur_fusee), 0.0, 0.0, vit_fusee, Nt)

objets_celestes = [terre]  # mercure
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
        sec, min = 'secondes', 'min'
        end_time_estimation = time.perf_counter()  # Enregistrer le temps de fin d'exécution
        execution_time_estimation = (end_time_estimation - start_time_estimation) * (
                    Nt - i)  # Calculer la durée totale d'exécution
        if execution_time_estimation >= 60:
            print(
                f"Il reste environ : {int(execution_time_estimation / 60)}{min} et {(execution_time_estimation / 60 % 1) * 60:.6f}",
                sec)
        else:
            print(f"Il reste environ : {execution_time_estimation:.6f}", sec)

for attribut in ['x', 'y', 'x_point', 'y_point']:  # remettre la fusée dans le referentiel héliocentrique
    setattr(fusee, attribut, [x + y for x, y in zip(getattr(fusee, attribut), getattr(terre, attribut))])

end_time = time.perf_counter()  # Enregistrer le temps de fin d'exécution
execution_time = end_time - start_time  # Calculer la durée totale d'exécution
print(f"Temps d'exécution : {execution_time:.6f} secondes")

fig, axs = plt.subplots(1, 2, figsize=(11, 7))
for i, objet in enumerate(tous_les_objets):
    plot_final(objet.couleur, objet.x, objet.y, objet.x_point, objet.y_point, objet.nom, objet.rayon, 'top')

axs[0].set_xlim(-terre.rayon * 2, terre.rayon * 2)
axs[0].set_ylim(-terre.rayon * 2, terre.rayon * 2)



from matplotlib.patches import Circle
cercle = Circle((0, 0), terre.rayon+140000, edgecolor='r', facecolor='none')
cercle2 = Circle((0, 0), terre.rayon+200000, edgecolor='r', facecolor='none')
axs[0].add_patch(cercle)
axs[0].add_patch(cercle2)

plt.tight_layout()
plt.show()
"""

from matplotlib.animation import FuncAnimation

# Initialiser la figure et l'axe
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2, color='r')
terre_circle = plt.Circle((0, 0), terre.rayon, color='b', alpha=0.7)
lune_circle = plt.Circle((0, 0), lune.rayon, color='r', alpha=0.7)
ax.add_artist(terre_circle)
ax.add_artist(lune_circle)

# Fonction d'initialisation de l'animation
def init():
    ax.set_xlim(-fusee.x[0]+terre.x[0], fusee.x[0]+terre.x[0])
    ax.set_ylim(0, terre.x[0])
    return line, terre_circle, lune_circle

# Fonction à appeler à chaque frame pour mettre à jour les données
def update(frame):
    terre_circle.set_center((terre.x[frame], terre.y[frame]))
    lune_circle.set_center((lune.x[frame], lune.y[frame]))
    line.set_data(fusee.x[:frame], fusee.y[:frame])
    return line, terre_circle, lune_circle

# Créer l'animation
ani = FuncAnimation(fig, update, frames=len(lune.x), init_func=init, blit=True)

# Afficher l'animation
plt.show()
"""