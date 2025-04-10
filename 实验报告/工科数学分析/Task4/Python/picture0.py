import matplotlib.pyplot as plt
import numpy as np

X, Y = np.meshgrid(np.arange(0, 20, .5), np.arange(0, 10, .5))
U = 0.5
V = Y*(0.2-0.04*Y)
fig1, ax1 = plt.subplots()
ax1.set_title('Arrows scale with plot width, not view')
Q = ax1.quiver(X, Y, U, V, units='width')
qk = ax1.quiverkey(Q, 0.9, 0.9, 1, r'$1 \frac{m}{s}$', labelpos='E',
                   coordinates='figure')
plt.show()