import numpy as np

def func_2eme_ordre_z(t, masse_vaisseau, g, Fp):
    dz_point_dt = -g +Fp/masse_vaisseau
    return dz_point_dt

def func_2eme_ordre_lune(t, masse_terre, G, r, theta_point):
    dr_point_dt = r*(theta_point**2) - (G*masse_terre)/(r**2)
    return dr_point_dt


def func_2eme_ordre_lune_x(G, masse_terre, x, y):
    r = np.sqrt(x ** 2 + y ** 2)
    dx_point_dt = ( (-G * masse_terre) / (r**3)) * x
    return dx_point_dt

def func_2eme_ordre_lune_y(G, masse_terre, x, y):
    r = np.sqrt(x ** 2 + y ** 2)
    dy_point_dt = ( (-G * masse_terre) / (r**3)) * y
    return dy_point_dt