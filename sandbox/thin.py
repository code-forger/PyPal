import pypalgame as pal

pal.init()

sphere = pal.geometry.Box((0,0,0,1,1,1))

print pal._pal.all_objects

for x in range(1000):
    pal.update(0.02)

sphere.delete()
pal.cleanup()
