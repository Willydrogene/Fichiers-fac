import fonc_principales
import numpy as np

def lots(t, masse_terre, G, nb_jours, x, x_point, y, y_point, dt, Nt):
    nb_y = [0, 0, 0]
    nb_y_t = [0, 0, 0]
    liste_x = []
    liste_x_point = []
    liste_y = []
    liste_y_point = []
    for i in range(nb_jours):
        if i > 0:
            # CI
            x = np.zeros(Nt)
            x_point = np.zeros(Nt)
            y = np.zeros(Nt)
            y_point = np.zeros(Nt)

            x[0] = liste_x[i - 1][-1]
            x_point[0] = liste_x_point[i - 1][-1]
            y[0] = liste_y[i - 1][-1]
            y_point[0] = liste_y_point[i - 1][-1]

        fonc_principales.lune(t, masse_terre, G, x, x_point, y, y_point, dt, Nt, i + 1, nb_jours, nb_y, nb_y_t)

        liste_x.append(x)
        liste_x_point.append(x_point)
        liste_y.append(y)
        liste_y_point.append(y_point)
    return liste_x, liste_y, liste_x_point, liste_y_point, nb_y, nb_y_t
