import pypal as pypal
from pypal import private_globals as pal
import ctypes as c
import weakref
import math
from generic_body import GenericBody
class Ghost(GenericBody):
    def __init__(self, pos, rotation=[0,0,0]):
        GenericBody.__init__(self, pos, rotation)
        self.dynamic_type = "static"
        self.mass = 0
        self.collision_response = False
        #self.actions = []
        #if parent:
        #    a = pypal.actuator.Action("Ghost" + self.obj + "parent",
        #                        self.move_to, parent)
        #    a.run()
        #    self.actions.append(a)

    def contains_object(self, target):
        for contact in pypal.get_contacts(target):
            for ref in contact:
                if ref in weakref.getweakrefs(self):
                    return True
        return False
