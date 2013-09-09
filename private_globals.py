import ctypes as c
import weakref
lib = c.cdll.LoadLibrary('/home/m/Python/pypalgame/libs/libPyPalGame.so')
import sys
user_data = {}

all_objects = {} # this dictionarry holds the ONLY strong reference to the objects in this library, never give a strong reference to ANYONE
actions = {}
notified_objects = []


class PalObject(object):
    def __new__(cls, *args, **kwargs):
        o = super(PalObject,cls).__new__(cls)
        o.__init__(*args, **kwargs)
        all_objects[str(o.obj)] = o
        return weakref.proxy(o)

    def set_user_data(self, data):
        old_data = None
        try:
            old_data = user_data[self.obj]
        except:
            pass
        user_data[self.obj] = data
        return old_data

    def get_user_data(self):
        return user_data[self.obj]

    def delete(self):
        lib.remove_object(self.obj)
        del all_objects[str(self.obj)]
