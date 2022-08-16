
import numpy as np
import matplotlib.pyplot as plt

print ("\nSet Warna dan Marker\n")

def sinus (frekuensi, amplitudo, waktu, theta):
    
    t = np.arange (0, waktu, 0.06)
    y = amplitudo * np.sin (2*frekuensi*t + np.deg2rad (theta))
    return t,y 

t1, y1 = sinus (1,4,4,0)
plt.plot (t1, y1)

t2, y2 = sinus (-1,4,4,0)
plt.plot (t2, y2, 'g-p')

t3, y3 = sinus (2,6,4,0)
plt.plot (t3, y3, 'r-o')

plt.show ()

print ("\n")