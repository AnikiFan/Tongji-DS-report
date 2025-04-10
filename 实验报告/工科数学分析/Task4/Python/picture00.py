import matplotlib.pyplot as plt
import numpy as np

X, Y = np.meshgrid(np.arange(-2, 2, .2), np.arange(-2, 2, .2))
U = 0.2
V = X+Y+Y*Y
fig1, ax1 = plt.subplots()
ax1.set_title('Arrows scale with plot width, not view')
Q = ax1.quiver(X, Y, U, V, units='width')
qk = ax1.quiverkey(Q, 0.9, 0.9, 1, r'$1 \frac{m}{s}$', labelpos='E',
                   coordinates='figure')
plt.show()