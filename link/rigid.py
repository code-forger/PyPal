import private_globals as pal
import ctypes as c
import weakref
class Rigid(object):
    """a link that connects two objects telescopically"""
    def __new__(cls,parent,child,collide):
        """
        constructs a rigid link and adds it to the world
        
        rect: a 6 part tuple with x,y,z,width,height,depth.
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        static: used to create this object static, if static is true, mass will be ignored
        """
        link = super(Rigid,cls).__new__(cls)
        link._create(parent,child,collide)
        pal.all_objects[str(pal.all_next)] = link
        link.index = pal.all_next
        pal.all_next += 1
        return weakref.proxy(link)

    def _create(self,parent,child,collide):
        """
        connects two objects together

        parent: the parent body
        child: the child body
        pos: a 3 part tuple for the position of the link
        direction: a 3 part unit vector of the driection of the link
        """
        self.obj = pal.lib.create_rigid(parent.obj,child.obj,c.c_bool(collide))


    def delete(self):
        x = self.index
        pal.lib.rigid_link_remove(self.obj)
        del pal.all_objects[str(x)]
