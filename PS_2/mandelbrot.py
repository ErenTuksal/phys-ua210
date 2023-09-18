import numpy as np
import matplotlib.pyplot as plt

xmin, xmax = -2, 2
ymin, ymax = -2, 2
N = 1000

x = np.linspace(xmin, xmax,N)
y = np.linspace(ymin, ymax,N)
x, y = np.meshgrid(x, y)
c = x + 1j * y

z = np.zeros_like(c)
mandelbrot = np.zeros_like(c, dtype=int)


for i in range(100):
    mask = np.abs(z) < 2.0
    z[mask] = z[mask] ** 2 + c[mask]
    mandelbrot += mask

plt.imshow(mandelbrot, extent=(xmin, xmax, ymin, ymax), interpolation='bilinear')
plt.colorbar()
plt.title("Mandelbrot Set")
plt.xlabel("Real Numbers")
plt.ylabel("Imaginary Numbers")
plt.show()
plt.savefig('mandelbrot.png')
