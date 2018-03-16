import numpy as np
import matplotlib.pyplot as plt

x_cords = range(-50,50)
y_cords = [x*x for x in x_cords]

plt.scatter(x_cords, y_cords)
plt.show()