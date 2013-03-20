import pypalgame as pal

pal.init()
terain =  pal.body.Terrain.create((0,0,0),50)
box = pal.body.Box.create((0,1.5,0,1,1,1),mass=1)
capsule = pal.body.Capsule.create((0,6,0,1,3),mass=1)
for x in range(80):
    pal.update(0.02)
    print capsule.get_position()[1],x

print capsule.get_size(),pal._pal.all_objects

pal.cleanup()
