import sys

import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.axes_grid1.inset_locator import inset_axes

try:
    dataFileName = sys.argv[1]
except IndexError:
    print("USAGE: python plotEnergies.py 'filename'")
    sys.exit(0)

HFEnergy3 = 3.161921401722216
HFEnergy6 = 20.71924844033019

numParticles = \
        int(dataFileName[dataFileName.find('N')+1:dataFileName.find('E')-1])
hfenergyFound = False 
if (numParticles == 2):
    HFEnergy = 3.161921401722216
    hfenergyFound = True 
elif (numParticles == 6):
    HFEnergy = 20.71924844033019
    hfenergyFound = True 
else:
    hfenergyFound = False

data = np.loadtxt(dataFileName, dtype=np.float64)
data[:,1] = np.sqrt(data[:,1])

n = len(data[:,0])
x = np.arange(0,n)

fig = plt.figure()

if (hfenergyFound):
    yline = np.zeros(n)
    yline.fill(HFEnergy)
    plt.plot(x, yline, 'r--', label="HF Energy")

msize = 1.0

ax = fig.add_subplot(111)
plt.errorbar(x, data[:,0], yerr=data[:,1],  fmt='bo', markersize=msize, label="VMC Energy")
plt.fill_between(x, data[:,0]-data[:,1], data[:,0]+data[:,1])

plt.xlim(0,n)
plt.xlabel('Iteration')
plt.ylabel('$E_0[a.u]$')
plt.legend(loc='best')

minSub = 80
maxSub = 120
inset_axes(ax, width="50%", height=1.0, loc='right')
plt.errorbar(x[minSub:maxSub], data[minSub:maxSub,0],
        yerr=data[minSub:maxSub,1],  fmt='bo', markersize=msize, label="VMC "
        "Energy")
plt.plot(x[minSub:maxSub], yline[minSub:maxSub], 'r--', label="HF Energy")

plt.show()
