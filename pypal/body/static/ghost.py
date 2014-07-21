import pypal as pypal
from pypal import private_globals as pal
import ctypes as c
import weakref
import math
from ..generic_body import GenericBody
class Ghost(GenericBody):
    """
    A Static Ghost 

    The Ghost body cannot collide with anything however can still detect objects that are intersecting with it.
    """
    def __init__(self, pos, rotation=[0,0,0]):
        """
        Parameters:
          pos: ``float`` The x, y, z, position of the body.
          rotation: ``float`` the rx, ry, rz rotation of the body.
        """
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
        """
        Will return true if this ghost contains the target.

        Parameters:
          target: ``pypal.body`` The body we want to know, if it is in the ghost.
        """
        for contact in pypal.get_contacts(target):
            for ref in contact:
                if ref in weakref.getweakrefs(self):
                    return True
        return False
