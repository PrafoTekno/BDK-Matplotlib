
import numpy as np
import matplotlib.pyplot as plt

print ("\nPendahuluan Pyplot\n")

x = np.array ([1,3,5,7,9,11])
y = np.array ([2,4,6,8,10,12])
y1 = np.array ([1,9,25,49,81,121])

plt.plot (x, y)
plt.plot (x,y1)
plt.show ()

print ("\n")