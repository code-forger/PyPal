import ctypes as c
import weakref
lib = c.cdll.LoadLibrary('/home/m/Python/PyPalGame/libs/libPyPalGame.so')

userdata = {}

all_objects = {} # this dictionarry holds the ONLY strong reference to the objects in this library, never give a strong reference to ANYONE
sensor_objects = {} # this dictionarry holds the ONLY strong reference to the sensors in this library, never give a strong reference to ANYONE
notified_objects = []
all_next = 0


class PalObject(object):
    def __new__(cls, *args, **kwargs):
        if len(args) == 1 and isinstance(args[0], int):
            return all_objects[str(args[0])]
        else:
            o = super(PalObject,cls).__new__(cls)
            o._create(*args, **kwargs)
            all_objects[str(o.obj)] = o
            return weakref.proxy(o)
