import ctypes as c
import weakref
lib = c.cdll.LoadLibrary('/usr/local/lib/libPyPalGame.so')

userdata = {}

all_objects = {}
all_next = 0
