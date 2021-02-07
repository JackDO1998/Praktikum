import numpy as np 
import matplotlib.pyplot as plt 
from uncertainties import ufloat

t = np.linspace(0, 2 * np.pi)
plt.plot(t, np.sin(t))