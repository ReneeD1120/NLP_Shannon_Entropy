#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 12:02:32 2022

@author: renee
"""

entropy_0=[12.33908,12.33847,12.33794,12.33778,12.33648,12.33472,12.33318,12.33084,12.32897,12.32728,12.32443,12.32196,12.31967,12.317,
           12.31446,12.3115,12.30876,12.30575,12.30298,12.29999,12.29742,12.29498,12.29247,12.29077,12.28856,12.28641,12.28423,
           12.28208,12.28007,12.27769,12.2755,12.27347,12.27111,12.27382,12.2768,12.27906,12.28134,12.28365,12.28589,12.28793,12.29039,
           12.29229,12.29399,12.29542,12.29698,12.29931,12.30167,12.30372,12.30605]
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(20,102,40)
plt.title('Change of Shannon Entropy for Chinese texts')
plt.xlabel('File Size(M)')
plt.ylabel('Shannon Entropy(Bits/letter）')
plt.plot(x, entropy_0[9::],color='purple'
         )
