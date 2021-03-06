import ctypes as c
import weakref
lib = c.cdll.LoadLibrary('/usr/local/lib/libpypal.so')
import sys
user_data = {}

all_objects = {} # this dictionarry holds the ONLY strong reference to the objects in this library, never give a strong reference to ANYONE
materials = {}
actions = {}
notified_objects = []

class PalObject(object):
    def __new__(cls, *args, **kwargs):
        o = super(PalObject,cls).__new__(cls)
        o.__init__(*args, **kwargs)
        all_objects[str(o.obj)] = o
        return weakref.proxy(o)

    def set_user_data(self, data):
        """ 
        Attaches a python object onto this physics object

        This function will associate a python object with this specific physics object.
        This is particulary usefull for when the physics engine returns you a physics object, for example, as part of :func:`pypal.get_contacts()`.
        
        Paremeters:
            data: ``object`` The object to be saved.
        """
        old_data = None
        try:
            old_data = user_data[self.obj]
        except:
            pass
        user_data[self.obj] = data
        return old_data

    def get_user_data(self):
        """ Returns the python object previously attached to this physics object. """
        return user_data[self.obj]

    def delete(self):
        lib.remove_object(self.obj)
        del all_objects[str(self.obj)]


Vec3 = c.c_float * 3
Mat4x4 = c.c_float * 16