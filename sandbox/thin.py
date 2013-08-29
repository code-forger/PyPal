import pypalgame as pal

pal.init()

box = pal.body.Box((0,5,0,1,1,1),mass = 1)

print box.set_user_data("hello")
print box.set_user_data("World")

for x in range(25):
    pal.update(0.02)
    print box.get_position()

print pal.get_objects()

pal.cleanup()
