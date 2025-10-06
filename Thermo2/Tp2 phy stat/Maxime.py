import random as rd
import math
import matplotlib.pyplot as plt

np = 120
vmax = 1
xmax = 2
m = 1
g = 1
dt = 0.05
dv = 0.5
vsolmax = 1
gamma = 0.1
niter = 20
ntherm = 40
vsolmax = 1


def faire_plot(x,v,xarg,pxth,varg,pvth,t,beta):
    nbx=20
    nbv=16
    t_pause=0.001
    
    fig, (ax1,ax2) = plt.subplots(2,constrained_layout=True)
    ax1.cla()
    ax1.hist(x,bins=nbx,color='white',edgecolor='blue',density=True,\
             label='histogramme')
    ax1.set(title='distribution des positions',xlabel='x',ylabel='p(x)')
    ax1.plot(xarg,pxth,'y',label='theorie')
    ax1.legend()
    
    ax2.cla()
    ax2.hist(v,bins=nbv,color='white',edgecolor='blue',density=True,\
                          label='histogramme')
    ax2.set(title='distribution des vitesses',xlabel='v',ylabel='p(v)')
    ax2.plot(varg,pvth,'y',label='theorie')
    ax2.legend()
    fig.suptitle('N = {0:d}   t = {1:d}   T = {2:.5g}'.format(len(x),int(t),1/beta))
    plt.pause(t_pause)


def vj_init_aleatoire(vjmax):
    vj=[]
    for i in range (np):
        vj.append (rd.uniform(-vjmax,vjmax))
    return vj

def xj_init_aleatoire(xjmax):
    xj=[]
    for i in range (np):
        xj.append (rd.uniform(0, xjmax))
    return xj

def px_theorique(x, beta):
    res = []
    for i in range(len(x)):
        valeur = beta * g * math.exp(-beta * g * x[i])
        res.append(valeur)
    return res

def pv_theorique(v, beta):
    res = []
    for i in range(len(v)):
        valeur = math.sqrt(beta / (2 * math.pi)) * math.exp(-0.5 * beta * v[i]**2)
        res.append(valeur)
    return res


def evolution_1(x, v):           #exercice 2
    for i in range(len(x)):
        v[i] -= g * dt
        x[i] += v[i] * dt
        if x[i] < 0:
            x[i] = -x[i]
            v[i] = -v[i]

def evolution_2(x, v):           #exercice 3
    for i in range(len(x)):
        v[i] -= g * dt
        x[i] += v[i] * dt
        if x[i] < 0:
            var_v =rd.uniform(-vsolmax,vsolmax)
            x[i] = -x[i]
            v[i] = -v[i] + 2*var_v
            
def evolution_3(x, v):           #exercice 4
    for i in range(len(x)):
        v[i] -= (g + gamma * v[i]) * dt
        x[i] += v[i] * dt
        if x[i] < 0:
            var_v =rd.uniform(-vsolmax,vsolmax)
            x[i] = -x[i]
            v[i] = -v[i] + 2*var_v
            

            
def echange_energie_aleatoire(v):
    energie_avant = 0
    for i in range(len(v)):
        energie_avant += 0.5 * v[i]**2

    for i in range(len(v)):
        var_v = rd.uniform(-dv, dv)
        v[i] += var_v

    energie_apres = 0
    for i in range(len(v)):
        energie_apres += 0.5 * v[i]**2

    alpha = math.sqrt(energie_avant / energie_apres)

    for i in range(len(v)):
        v[i] *= alpha
        
    return v

def main (evolution):
    x = xj_init_aleatoire(xmax)
    v = vj_init_aleatoire(vmax)
    
    tt = []
    TT = []
    t=0
    
    for i in range(niter):
        
        for j in range(ntherm):
            evolution (x, v)
            t += dt
        echange_energie_aleatoire(v)
        E_moy = 0
        for j in range(np):
            E_moy += 0.5 * v[j]**2 + g * x[j]
        E_moy = E_moy / np  
        T = (2 / 3) * E_moy
        beta = 1 / T
        
        nplot = 300
    
        h_x = max(x) / (nplot)  
        xarg = [0 + i * h_x for i in range(nplot + 1)]
    
      
        v_max = max(abs(min(v)), abs(max(v)))
        h_v = 2 * v_max / (nplot)  
        varg = [-v_max + i * h_v for i in range(nplot + 1)]  
    
        pxth = px_theorique(xarg, beta)
        pvth = pv_theorique(varg, beta)
        
        faire_plot(x, v, xarg, pxth, varg, pvth, t, beta)
        
        tt.append(t)
        TT.append(T)
        
    plt.plot(tt, TT)
    plt.xlabel('temps')
    plt.ylabel('Temperatuere')
    plt.title('temperature en fonction du temps')  
    plt.show()


main(evolution_3)