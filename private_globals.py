import ctypes as c
lib = c.cdll.LoadLibrary('/usr/local/lib/libPyPalGame.so')

physics = None
collision = None

userdata = []
