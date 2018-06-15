from geom2d.point import *

l = []

for i in range (-5, 6):
    l.append(Point(i, i*i))

for el in l:
    el.y = -el.y

print(l)
