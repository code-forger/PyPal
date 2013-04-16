import ctypes as c
import weakref
lib = c.cdll.LoadLibrary('/home/m/Python/PyPalGame/libs/libPyPalGame.so')

userdata = {}

all_objects = {} # this dictionarry holds the ONLY strong reference to the objects in this library, never give a strong reference to ANYONE
sensor_objects = {} # this dictionarry holds the ONLY strong reference to the sensors in this library, never give a strong reference to ANYONE
notified_objects = []
all_next = 0
