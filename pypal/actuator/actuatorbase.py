from pypal import private_globals as _pal
import ctypes as c
import weakref
import action

class ActuatorBase(_pal.PalObject):
    action = None
    def turn_on(self):
        self.action = action.Action("Actuator " + str(self.obj),
                                    self.apply)
        self.action.run()

    def turn_off(self):
        try:
            self.action.pause()
            self.action = None
        except:
            pass
