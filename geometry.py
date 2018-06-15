from geom2d.point import *

l = []

for i in range (-5, 6):
    l.append(Point(i, i*i))

print(l)

for el in l:
    print(el)
