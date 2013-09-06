import pypalgame as pypal
from pypalgame import private_globals as pal
import ctypes as c
import weakref
import math
from bodybase import BodyBase
class Ghost(pal.PalObject):
    count = 0
    def __init__(self,rect,parent=None):#TESTED
        Ghost.count -=1 
        self.obj = str(Ghost.count)
        self.rect = rect
        self.parent = parent

        if len(rect) == 4:
            self.collide = self._collide_sphere
        elif len(rect) == 6:
            self.collide = self._collide_box
        else:
            raise ValueError("Rect parameter for a Ghost must be of length 4 or 6.")

        self.actions = []
        if parent:
            a = pypal.actuator.Action("Ghost" + self.obj + "parent",
                                self.move_to, parent)
            a.run()
            self.actions.append(a)

    def _collide_sphere(self, target):
        tar_pos = target.get_position()
        normalrect = [self.rect[x]-tar_pos[x] for x in range(3)]
        distance = sum([normalrect[x]**2 for x in range(3)])
        distance = math.sqrt(distance)
        if distance <= self.rect[3]:
            return True
        return False

    def _collide_box(self, target):
        tar_pos = target.get_position()
        normalrect = [self.rect[x]-tar_pos[x] for x in range(3)]
        normalrect = [abs(normalrect[x]) for x in range(3)]
        if(normalrect[0] <= self.rect[3] and
           normalrect[1] <= self.rect[4] and
           normalrect[2] <= self.rect[5]):
            return True
        return False

    def move_to(self, name, target):
        pos = target.get_position()
        self.rect[0] = pos[0]
        self.rect[1] = pos[1]
        self.rect[2] = pos[2]

    def collide_list(self, targets):
        ret = []
        for target in targets:
            if self.collide(target):
                ret.append(target)
        return ret

    def get_position(self):
        return rect[:3]

    def set_position(self, pos):
        self.rect[0] = pos[0]
        self.rect[1] = pos[1]
        self.rect[2] = pos[2]

    def delete(self):
        del pal.all_objects[str(self.obj)]
