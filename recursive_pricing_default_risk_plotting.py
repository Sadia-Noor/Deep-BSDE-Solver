# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 23:16:33 2022

@author: HP
"""


import matplotlib.pyplot as plt
import numpy as np

epochs = np.array([0, 1000,2000, 3000, 4000, 5000, 6000 ])
Loss_mean = np.array([123.582, 40.172, 26.0527, 25.7447, 25.528, 25.4471, 25.1507])
L1_rel = ([0.196017452, 0.087246073, 0.026802792, 0.005867365, 0.004478185, 0.004401396, 0.003689354])
y = ([46.0682, 52.3008, 55.7642, 56.9638, 57.0434, 57.0478, 57.0886])
fig, ax = plt.subplots(1,2,figsize=(15,6))
color = 'tab:blue'

ax[0].plot(epochs, L1_rel, color=color)
#ax[0].fill_between(epochs, y_mean-y_std, y_mean+y_std, alpha=0.2)
ax[0].set_xlabel('Number of iteration steps')
ax[0].set_ylabel('Relative approximation error')
#ax[0].set_ylim([10^-3,10^0])
ax[0].set_title('(a) Relative L1-approximation error')


ax[1].semilogy(epochs, Loss_mean, color=color)
#ax[1].fill_between(epochs, Loss_mean-Loss_std, Loss_mean+Loss_std, alpha=0.2)
ax[1].set_xlabel('Number of iteration steps')
ax[1].set_ylabel('Loss')
ax[1].set_title('(b) Mean of the loss function')
#ax[1].set_ylim([1e1,1e2])




#plt.plot(epochs, y)
#plt.xlabel("Number of iteration steps")
#plt.ylabel("u(t=0,x=(100,…,100))")