from ctypes import cdll
#pallib  = cdll.LoadLibrary('./libpal.so')
#palbulletlib  = cdll.LoadLibrary('./libpal_bullet.so')

lib = cdll.LoadLibrary('./libPyPalGame.so')

lib.runer()
