import pypalgame as pal

pal.init()

points = ((1,1,1),
          (0,1,1),
          (1,0,1),
          (1,1,0),
          (0,0,1),
          (0,1,0),
          (1,0,0),
          (0,0,0))

convex = pal.body.Convex((0,0,0),points)

for x in range(1000):
    pal.update(0.02)

pal.cleanup()
