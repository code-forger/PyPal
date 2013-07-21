import private_globals as pal
import ctypes as c
import weakref
class Prismatic(pal.PalObject):
    """a link that connects two objects telescopically"""
    def _create(self,parent,child,pos,direction,collide):
        self.obj = pal.lib.create_prismatic(parent.obj,child.obj,c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]),c.c_float(direction[0]),c.c_float(direction[1]),c.c_float(direction[2]),c.c_bool(collide))

    def set_limits(self, min_limit, max_limit):
        """
        Sets limits on the link

        maX_limit: the maximum distance the child body can be from the link
        min_limit: the minimum distance the child body can be from the link
        """
        pal.lib.prismatic_link_set_limits(self.obj, c.c_float(min_limit), c.c_float(max_limit))

    def delete(self):
        pal.lib.prismatic_link_remove(self.obj)
        del pal.all_objects[str(self.obj)]
