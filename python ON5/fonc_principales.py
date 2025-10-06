import fonc_2nd
import numpy as np

def verlet_method(t, masse_vaisseau, g, Fp, z, z_point, dt, Nt):
    progress = 0
    for i in range(1, Nt):
        # Calcul du pourcentage d'avancement
        new_progress = int((i / Nt) * 100)
        if new_progress != progress:
            print(f"Avancement : {new_progress}%")
            progress = new_progress


        z_half = z[i - 1] + z_point[i - 1] * dt / 2  # Il faut imaginer la méthode trapèzes des intégrales
        temp_z_point_verlet = z_point[i - 1] + fonc_2nd.func_2eme_ordre_z(t[i], masse_vaisseau, g, Fp) * dt
        z[i] = z_half + temp_z_point_verlet * dt / 2
        z_point[i] = temp_z_point_verlet

    return z, z_point



def lune(t, masse_terre, G, x, x_point, y, y_point, dt, Nt, av, nb_jours, nb_y, nb_y_t):
    progress = 0
    for i in range(1, Nt):

        # Calcul des coefficients k1
        k1_x = x_point[i - 1]
        k1_y = y_point[i - 1]
        k1_x_point = fonc_2nd.func_2eme_ordre_lune_x(G, masse_terre, x[i - 1], y[i - 1])
        k1_y_point = fonc_2nd.func_2eme_ordre_lune_y(G, masse_terre, x[i - 1], y[i - 1])

        # Calcul des coefficients k2
        k2_x = x_point[i - 1] + 0.5 * dt * k1_x_point
        k2_y = y_point[i - 1] + 0.5 * dt * k1_y_point
        k2_x_point = fonc_2nd.func_2eme_ordre_lune_x(G, masse_terre, x[i - 1] + 0.5 * dt * k1_x, y[i - 1] + 0.5 * dt * k1_y)
        k2_y_point = fonc_2nd.func_2eme_ordre_lune_y(G, masse_terre, x[i - 1] + 0.5 * dt * k1_x, y[i - 1] + 0.5 * dt * k1_y)

        # Calcul des coefficients k3
        k3_x = x_point[i - 1] + 0.5 * dt * k2_x_point
        k3_y = y_point[i - 1] + 0.5 * dt * k2_y_point
        k3_x_point = fonc_2nd.func_2eme_ordre_lune_x(G, masse_terre, x[i - 1] + 0.5 * dt * k2_x, y[i - 1] + 0.5 * dt * k2_y)
        k3_y_point = fonc_2nd.func_2eme_ordre_lune_y(G, masse_terre, x[i - 1] + 0.5 * dt * k2_x, y[i - 1] + 0.5 * dt * k2_y)

        # Calcul des coefficients k4
        k4_x = x_point[i - 1] + dt * k3_x_point
        k4_y = y_point[i - 1] + dt * k3_y_point
        k4_x_point = fonc_2nd.func_2eme_ordre_lune_x(G, masse_terre, x[i - 1] + dt * k3_x, y[i - 1] + dt * k3_y)
        k4_y_point = fonc_2nd.func_2eme_ordre_lune_y(G, masse_terre, x[i - 1] + dt * k3_x, y[i - 1] + dt * k3_y)

        # Mise à jour des valeurs de position et vitesse
        x[i] = x[i - 1] + (dt / 6) * (k1_x + 2 * k2_x + 2 * k3_x + k4_x)
        y[i] = y[i - 1] + (dt / 6) * (k1_y + 2 * k2_y + 2 * k3_y + k4_y)
        x_point[i] = x_point[i - 1] + (dt / 6) * (k1_x_point + 2 * k2_x_point + 2 * k3_x_point + k4_x_point)
        y_point[i] = y_point[i - 1] + (dt / 6) * (k1_y_point + 2 * k2_y_point + 2 * k3_y_point + k4_y_point)



        """
        x_half = x[i - 1] + x_point[i - 1] * dt / 2  # Il faut imaginer la méthode trapèzes des intégrales
        temp_x_point = x_point[i - 1] + fonc_2nd.func_2eme_ordre_lune_x(G, masse_terre, x_half, y[i-1]) * dt
        x[i] = x_half + temp_x_point * dt / 2
        x_point[i] = temp_x_point
        
        y_half = y[i - 1] + y_point[i - 1] * dt / 2  # Il faut imaginer la méthode trapèzes des intégrales
        temp_y_point = y_point[i - 1] + fonc_2nd.func_2eme_ordre_lune_y(G, masse_terre, x[i-1], y_half) * dt
        y[i] = y_half + temp_y_point * dt / 2
        y_point[i] = temp_y_point
        """

        if round(y[i], -int(3 + np.log10(dt))) == 0:
            nb_y[0] = nb_y[0]+1
            nb_y[1] = y[i]
            nb_y[2] = x[i]
        if round(y[i], -int(5 + np.log10(dt))) == 0:
            nb_y_t[0] = nb_y_t[0]+1
            nb_y_t[1] = y[i]
            nb_y_t[2] = x[i]


        # Calcul du pourcentage d'avancement
        new_progress = int((i / Nt) * 100)
        if new_progress != progress:
            print(f"Avancement {av} / {nb_jours} : {new_progress}%")
            progress = new_progress

    return x, x_point, y, y_point