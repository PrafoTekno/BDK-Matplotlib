
import numpy as np
import matplotlib.pyplot as plt

print ("\nMenambahkan Text\n")

def sinus (A, f, t_akhir, theta):
    t = np.arange (0,t_akhir,0.01)
    y = A * np.sin (2 * f * t + np.deg2rad (theta))
    return t,y

t1,y1 = sinus (4,1,5,0)
plt.plot (t1, y1)

plt.text (2.3,3.8, "Ini Text")
plt.text (2.3,1.4, "Text 2")

plt.show ()

print ("\n")