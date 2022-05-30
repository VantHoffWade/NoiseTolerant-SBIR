import bresenham as bh
import matplotlib.pyplot as plt

points = bh.bresenham(1, 1, 5, 6)
fig, ax = plt.subplots()
for point in points:
	ax.scatter(point[0], point[1], c='r')

plt.show()