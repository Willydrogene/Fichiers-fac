import numpy as np
import numpy.random
import matplotlib.pyplot as plt




def f(x):
    return 4 * np.sin(5*x) + x**2 + 5
    


nb_alea = numpy.random.uniform((np.pi/4), (3*np.pi/4), 10000)

dessus = 0
dessous = 0

for i in range(len(nb_alea)):
    if nb_alea[i] >= f(i):
            dessus += 1
    else: 
        dessous += 1


print('En dessus:', dessus)
print('En dessous:', dessous)

rapport = (dessous / nb_alea) * (np.pi/4 * 3*np.pi/4)
print('Le rapport est de:', rapport)