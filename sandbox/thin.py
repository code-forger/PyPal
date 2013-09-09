import pypalgame as pal

pal.init()

box = pal.body.Box((0,0,0,1,1,1),1)
box1 = pal.body.Box((0,0,0,1,1,1),1)
box1.delete()

for x in range(1000):
    pal.update(0.02)

box.delete()
pal.update(0.02)
pal.cleanup()
