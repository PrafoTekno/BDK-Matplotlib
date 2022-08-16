
import numpy as np
import matplotlib.pyplot as plt

print ("\nSet Axis\n")

def parabola (x) :
    y = x**2 + 2*x - 8
    return y

x_value = np.arange (0,11)
y_value = parabola (x_value)

plt.plot (x_value, y_value)

# plt.axis ([x_min, x_max, y_min, y_max])
plt.axis ([-2,10,-10,20])

plt.show ()

print ("\n")