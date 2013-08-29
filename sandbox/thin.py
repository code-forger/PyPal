import pypalgame as pal

pal.init()

box = pal.body.Box((0,0,0,1,1,1),mass=1)
gps = pal.sensor.GPS(box,100,10,10)

for x in range(25):
    pal.update(0.02)
    print "answer",gps.get_string()


pal.cleanup()
