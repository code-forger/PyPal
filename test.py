import pypalgame as pal


cpp = False
if cpp:
    pal_lib.runner()
else:

    pal.init()
    pal.body.Terrain((0,0,0),50)
    box = pal.body.Box((0,1.5,0,1,1,1),mass=1)
    for x in range(26):
        pal.update(0.02)
        print box.get_position()
