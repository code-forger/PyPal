import private_globals as pal
import ctypes as c
import weakref

class Action():
    def __init__(self, name, func, *args, **kwargs):
        self.action = [name ,func, args, kwargs]
        self.name = name

    def pause(self, ):
        del pal.actions[self.name]

    def run(self, ):
        pal.actions[self.name] = self.action
