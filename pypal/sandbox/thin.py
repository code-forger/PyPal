import pypal as pal

pal.init()

box2 = pal.body.StaticBox((0,0,0,50,1,50))

box = pal.body.Box((0,20,0,1,1,1), mass=10)


for x in range(100):
    pal.update(0.02)
    print box.get_location_matrix()

pal.cleanup()
