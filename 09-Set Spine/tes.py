
import numpy as np
import matplotlib.pyplot as plt

print ("\nSet Spine\n")

x = np.arange (0,360,1)
y = np.sin (np.deg2rad (x))

plt.title ("Sinusoidal")

plt.plot (x, y)

plt.text (370,0.08,"theta")
plt.text (190,1.03,"amplitudo")

plt.yticks ([-1,0,1])
plt.xticks (
    [    0,          90,          180,          270 ,         360],
    [r'${0}^o$', r'${90}^o$', r'${180}^o$', r'${270}^o$', r'${360}^o$']
    )

# Bergantung dengan yticks dan xticks nya, buat atus axis nya

ax = plt.gca () #get current axis (gca)
ax.spines['left'].set_position (('data',180))
ax.spines['right'].set_color(('none'))
ax.spines['top'].set_color(('none'))
ax.spines['bottom'].set_position (('data',0))

plt.show ()

print ("\n")