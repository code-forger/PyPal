import pypal as pal

pal.init()

box2 = pal.body.StaticBox((0,0,0,50,1,50))

body = pal.body.GenericBody((0,10,0))

boxgeom = pal.geometry.Box((0,10,0,1,1,1))
body.connect_geometry(boxgeom)

box = pal.body.Box((0,20,0,1,1,1), mass=10)

body.dynamics_type = "dynamic"
body.mass = 1
body.gravity_enabled = True

for x in range(100):
    pal.update(0.02)
    print body.get_position(), body.get_location()#, box.get_location()

pal.cleanup()
