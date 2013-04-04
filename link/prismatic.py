import private_globals as pal
import ctypes as c
import weakref
class Prismatic(object):
    """a link that connects two objects telescopically"""
    def __new__(cls,parent,child,pos,direction,collide):
        """
        constructs a revolate link and adds it to the world
        
        rect: a 6 part tuple with x,y,z,width,height,depth.
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        static: used to create this object static, if static is true, mass will be ignored
        """
        link = super(Prismatic,cls).__new__(cls)
        link._create(parent,child,pos,direction,collide)
        pal.all_objects[str(pal.all_next)] = link
        link.index = pal.all_next
        pal.all_next += 1
        return weakref.proxy(link)

    def _create(self,parent,child,pos,direction,collide):
        """
        connects two objects together

        parent: the parent body
        child: the child body
        pos: a 3 part tuple for the position of the link
        direction: a 3 part unit vector of the driection of the link
        """
        self.obj = pal.lib.create_prismatic(parent.obj,child.obj,c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]),c.c_float(direction[0]),c.c_float(direction[1]),c.c_float(direction[2]),c.c_bool(collide))

    def set_limits(self, min_limit, max_limit):
        """
        Sets limits on the link

        maX_limit: the maximum distance the child body can be from the link
        min_limit: the minimum distance the child body can be from the link
        """
        pal.lib.prismatic_link_set_limits(self.obj, c.c_float(min_limit), c.c_float(max_limit))

    def delete(self):
        x = self.index
        pal.lib.prismatic_link_remove(self.obj)
        del pal.all_objects[str(x)]
