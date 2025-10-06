#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 07:58:33 2025

@author: grw4219a
"""


import numpy as np


m = 1  
g = 1  
beta = 1  

dx = 0.001  
dv = 0.001  
x_max = 10  
v_max = 10  


Z1 = 0
x = 0
while x < x_max:
    Z1 += np.exp(-beta * m * g * x) * dx
    x += dx


Z2 = 0
v = -v_max
while v < v_max:
    Z2 += np.exp(-beta * m * v**2 / 2) * dv
    v += dv


Z = Z1 * Z2

E_moy = 3 / (2 * beta)

# Valeurs théoriques données dans l'énoncé
Z1_th = 1/(beta*m*g)
Z2_th = np.sqrt(2 * np.pi / (beta * m))
Z_th = np.sqrt(2 * np.pi) / (g * beta**(3/2))

print(f"Z1 (numérique) = {Z1}, Z1 (théorique) = {Z1_th}")
print(f"Z2 (numérique) = {Z2}, Z2 (théorique) = {Z2_th}")
print(f"Z (numérique) = {Z}, Z (théorique) = {Z_th}")
print(f"⟨E⟩ = {E_moy}")
