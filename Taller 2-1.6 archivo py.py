def hola_mundo():
    print("Hola mundo")

hola_mundo()
print("hola mundo")

def cambiemos(a,b):
    return a*b

print(cambiemos(3,4))


import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-10, 10, 400)
y = x**2

plt.plot(x, y)
plt.show()