#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import matplotlib.pyplot as plt

# Paramètres du modèle
S0 = 100          # Prix initial de l'actif
mu = 0.08         # Taux de rendement annuel (8%)
sigma = 0.5      # Volatilité annuelle (25%)
T = 1             # Horizon temporel (1 an)
N = 250           # Nombre de pas de temps (jours ouvrés)
dt = T/N          # Pas de temps
n_simulations = 100 # Nombre de trajectoires à simuler

# Initialisation
np.random.seed(42)  # Pour la reproductibilité
t = np.linspace(0, T, N+1)  # Échelle de temps

# Génération des trajectoires
trajectoires = np.zeros((n_simulations, N+1))
trajectoires[:, 0] = S0  # Toutes les trajectoires commencent à S0

for i in range(n_simulations):
    # Mouvement brownien standard
    dW = np.random.normal(0, np.sqrt(dt), N)
    W = np.cumsum(dW)
    W = np.insert(W, 0, 0)  # W(0) = 0
    
    # Application de la formule du MBG
    trajectoires[i, :] = S0 * np.exp((mu - 0.5*sigma**2)*t + sigma*W)

# Visualisation
plt.figure(figsize=(12, 6))
for i in range(n_simulations):
    plt.plot(t, trajectoires[i, :], lw=1, alpha=0.8, label=f'Traj. {i+1}' if i < 5 else None)

plt.axhline(y=S0, color='black', linestyle='--', label='Prix initial')
plt.title(f'Mouvement Brownien Géométrique Angelo ({n_simulations} trajectoires)\n$\mu$={mu}, $\sigma$={sigma}', pad=20)
plt.xlabel('Temps')
plt.ylabel("Prix")
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# In[ ]:




