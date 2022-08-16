
import numpy as np
import matplotlib.pyplot as plt

print ("\nSet Label dan Title\n")

def parabola (x) :
    y = x**2 + 3*x - 2
    return y

x_value = np.arange (0,6)
y_value = parabola (x_value)

plt.plot (x_value, y_value)

title = "Grafik Parabola\n"
judul = r"$ \mathcal{Y} = x^{2} + 3x - 2$"

x_label = r"x (cm)"
y_label = r"$ \mathcal{Y}$ (cm)"

plt.title (title + judul)

plt.xlabel (x_label)
plt.ylabel (y_label)

plt.show ()

print ("\n")
