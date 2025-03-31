#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np #Pour les calcul num et pour generer les donnees aleatoires


# In[9]:


import matplotlib.pyplot as plt #Pour les graphes

# In[10]:


def main():
    n = 1000  # Discretisation
    N = 100 #Nombres de trajectoires
    T = 1.0   #Temps
    times = np.linspace(0., T, n) # Génère 10 valeurs entre 0 et 1
    dt = T / n
    
   # Génération des incréments brownien pour N trajectoires
    Z = np.random.normal(size=(N, n-1))  # Matrice N x (n-1) de lois N(0,1)
    dB = np.sqrt(dt) * Z  # Conversion en incréments brownien
    
    # Initialisation de matrice N x n avec B(0) = 0
    B = np.zeros((N, n)) 
     # Calcul de chaque trajectoire via une boucle for
    for i in range(1, n):
        B[:, i] = B[:, i-1] + dB[:, i-1]
    
     # Visualisation de N trajectoires
    plt.figure(figsize=(10, 6))
    for j in range(N):
        plt.plot(times, B[j, :], label=f'Trajectoire {j+1}', alpha=0.6)
    
    plt.xlabel('Temps')
    plt.ylabel('B(t)')
    plt.title(f'Simulation de {N} Trajectoires du Mouvement Brownien')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()


# In[ ]:





# In[ ]:

