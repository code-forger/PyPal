from pypal import private_globals as _pal
import ctypes as c
import weakref

class Action():
    """
    An action that will be performed post step.

    While this class is set to :func:`run()`
    func will be called during every :func:`pypal.update()` with the following format:

        response = func(*args, **kwargs)

    This allows you to register a function that will be called with any arguments, and give you acess to the returned value.
    """
    def __init__(self, name, func, *args, **kwargs):
        """
        Parameters:
          name: ``str`` The unique identifying name for this action. Using the same name twice will overide the first action.
          func: The function to be called every step.
          args: The argument list ot be passed to the function.
          kwargs: the keyword arguments to be passed to the function.
        """
        self.function = func
        self.name = name
        self.args = args
        self.kwargs = kwargs
        self.response = None

    def pause(self):
        """ Stop calling this action every step. """
        del _pal.actions[self.name]

    def run(self):
        """ Start calling this action every step. """
        _pal.actions[self.name] = self
