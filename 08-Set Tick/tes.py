
import numpy as np
import matplotlib.pyplot as plt

print ("\nSet Ticks\n")

x = np.arange (0,360,1)
y = np.sin (np.deg2rad (x))

plt.plot (x, y)

plt.xlabel ("sudut")
plt.ylabel ("amplitudo")

plt.yticks ([-1,0,1])
plt.xticks (
    [    0,          90,          180,          270,          360],
    [r'${0}^o$', r'${90}^o$', r'${180}^o$', r'${270}^o$', r'${360}^o$']
    )

plt.show ()

print ("\n")