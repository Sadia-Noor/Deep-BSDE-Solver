# -*- coding: utf-8 -*-
"""
@author: SADIA NOOR

"""

import matplotlib.pyplot as plt
import numpy as np

'''Pricing of European financial derivatives with different interest 
rates for borrowing and lending.
'''


epochs = np.array([0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000])
Loss_mean = np.array([51.9296, 40.5897, 38.1619, 38.0187, 38.0005, 37.8893, 37.9493, 38.1534 ,38.2138])
L1_rel = ([0.216775435, 0.115967886, 0.049255834, 0.016150993, 0.004544814, 0.001427297, 0.000535236, 0.000478896, 4.69506E-06])

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
ax[1].set_ylim([1e1,1e2])


#epochs = np.array([0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000])
#y = ([16.6819, 18.829, 20.2499, 20.955, 21.2022, 21.2686, 21.2876, 21.288, 21.2991])
#plt.plot(epochs, y)
#plt.xlabel("Number of iteration steps")
#plt.ylabel("u(t=0,x=(100,…,100))")







