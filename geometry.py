from geom2d.point import *

l1 = [Point(i, i*i) for i in range(-5, 6)]

l2 = [Point(el.x, -el.y) for el in l1]

print(l1)
print(l2)
