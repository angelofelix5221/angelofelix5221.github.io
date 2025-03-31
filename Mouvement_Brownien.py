#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np #Pour les calcul num et pour generer les donnees aleatoires


# In[9]:


import matplotlib.pyplot as plt #Pour les graphes

# In[10]:


def main():
    n = 1000  # Discretisation
    T = 1.0   #Temps
    times = np.linspace(0., T, n) # Génère 10 valeurs entre 0 et 1
    dt = T / n
    
    # Génération des incréments brownien
    Z = np.random.normal(size=n-1) #Pour generer n variables aleatoires i.i.d de loi N(0,1)
    dB = np.sqrt(dt) * Z 
    
    # Initialisation du mouvement brownien avec B(0) = 0
    B = np.zeros(n) # Initialisation de tableau de taille n avec B(0) = 0
    for i in range(1, n):
        B[i] = B[i-1] + dB[i-1]
    
    # Visualisation
    plt.figure(figsize=(8, 5))
    plt.plot(times, B, label='Mouvement Brownien')
    plt.xlabel('Temps')
    plt.ylabel('B(t)')
    plt.title('Simulation d\'un Mouvement Brownien')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()


# In[ ]:





# In[ ]:




