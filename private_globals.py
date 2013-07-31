import ctypes as c
import weakref
lib = c.cdll.LoadLibrary('/home/m/Python/PyPalGame/libs/libPyPalGame.so')

userdata = {}

all_objects = {} # this dictionarry holds the ONLY strong reference to the objects in this library, never give a strong reference to ANYONE
actions = {}
notified_objects = []


class PalObject(object):
    def __new__(cls, *args, **kwargs):
        o = super(PalObject,cls).__new__(cls)
        o._create(*args, **kwargs)
        all_objects[str(o.obj)] = o
        return weakref.proxy(o)
