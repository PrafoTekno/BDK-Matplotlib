
import numpy as np
import matplotlib.pyplot as plt

print ("\nLegend\n")

def sinus (A,f,t_akhir,theta) :

    t = np.arange (0, t_akhir, 0.01)
    y = A * np.sin (2 * f * t + np.deg2rad (theta))
    return t,y

# Tipe 1 

"""
t1, y1 = sinus (4,1,4,0)
plt.plot (t1, y1, label="sin(0)")

t2, y2 = sinus (4,1,4,90)
plt.plot (t2, y2, label="sin(90)")

plt.legend (loc="upper center")
"""

# Tipe 2
"""
t1, y1 = sinus (4,1,4,0)
plt.plot (t1, y1, label="sin(0)")

t2, y2 = sinus (4,1,4,90)
plt.plot (t2, y2, label="sin(90)")

plt.legend (loc="upper center", bbox_to_anchor=(0,-0.5))
"""

# Tipe 3

plt.figure (1)

ax = plt.subplot (111) #Variable untuk plot kita

t1, y1 = sinus (4,1,4,0)
plt.plot (t1, y1, label="sin(0)")

t2, y2 = sinus (4,1,4,90)
plt.plot (t2, y2, label="sin(90)")

box = ax.get_position () #Mengambil box (plot) agar bisa diedit
ax.set_position ([box.x0, box.y0, box.width*0.8, box.height])

plt.legend (loc="upper center", bbox_to_anchor=(1.2,0.7))

plt.show ()

print ("\n")