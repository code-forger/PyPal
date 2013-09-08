from pypalgame import private_globals as pal
import ctypes as c
import weakref
import action

class ActuatorBase(pal.PalObject):
    action = None
    def turn_on(self):
        self.action = action.Action("Actuator " + str(self.obj),
                                    self.run)
        self.action.run()

    def turn_off(self):
        try:
            self.action.pause()
            self.action = None
        except:
            pass
