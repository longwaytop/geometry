from geom2d.point import *

l = []

for i in range (-5, 6):
    l.append(Point(i, i*i))

l2 = []

for el in l:
    l2.append(Point(el.x, el.y))
    el.y = -el.y

print(l)
print(l2)
