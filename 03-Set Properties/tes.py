
import numpy as np
import matplotlib.pyplot as plt

print ("\nSet Properties\n")

def sinus (Amplitudo, frekuensi, t_akhir, theta):

    t = np.arange (0, t_akhir, 0.06)
    y = Amplitudo * np.sin (2 * frekuensi * t + np.deg2rad (theta))
    return t, y

t1, y1 = sinus (4,1,5,0)
plot_1 = plt.plot (t1,y1)

t2, y2 = sinus (4,0.5,5,0)
plot_2 = plt.plot (t2, y2)

t3, y3 = sinus (4,2,5,90)
plot_3 = plt.plot (t3, y3)

# plt.setp (plot, style=value, style1=value, ...)
plt.setp (plot_1, color = 'red', linestyle = 'dashdot', linewidth = 3)
plt.setp (plot_2, color = 'green', linestyle = '--', linewidth = 2)
plt.setp (plot_3, color = 'purple', linestyle = 'solid', linewidth = 1)

plt.show ()

print ("\n")