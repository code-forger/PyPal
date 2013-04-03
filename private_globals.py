import ctypes as c
import weakref
lib = c.cdll.LoadLibrary('libs/libPyPalGame.so')

userdata = {}

all_objects = {} # this dictionarry holds the ONLY strong reference to the object in this library, never give a strong reference to ANYONE
notified_objects = {}
all_next = 0
