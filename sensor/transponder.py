import private_globals as pal
import ctypes as c
import weakref
class Transponder_Reciever(object):
    def __new__(cls,body):
        """
        adds a reciever to the world
        
        body: The body to connect the Reciever to
        """
        
        transponder = super(Transponder_Reciever,cls).__new__(cls)
        transponder._create(body)
        pal.sensor_objects[str(transponder.obj)] = transponder
        return weakref.proxy(transponder)

    def _create(self,body):
        """
        THIS METHOD IS PRIVATE: to create a box use the create class method
        constructs a box and adds it to the world
        
        rect: a 6 part tuple with x,y,z,width,height,depth.
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        static: used to create this object static, if static is true, mass will be ignored
        """
        self.obj = pal.lib.create_transponder_reciever(body.obj)


    def get_distance(self,sender_id):
        """returns the distance to the sender"""
        pal.lib.transponder_reciever_distance.restype = c.c_float
        return pal.lib.transponder_reciever_distance(self.obj,sender_id)

    def get_number_of_senders(self):
        """returns the sender id of the sender in range"""
        return pal.lib.transponder_reciever_get_num_of_senders(self.obj)

    def delete(self):
        pal.lib.transponder_reciever_remove(self.obj)
        del pal.sensor_objects[str(self.obj)]

class Transponder_Sender(object):
    def __new__(cls,body,max_distance):
        """
        adds a sender to the world
        
        body: The body to connect the Reciever to
        """
        
        transponder = super(Transponder_Sender,cls).__new__(cls)
        transponder._create(body,max_distance)
        pal.sensor_objects[str(transponder.obj)] = transponder
        return weakref.proxy(transponder)

    def _create(self,body,max_distance):
        """
        THIS METHOD IS PRIVATE: to create a box use the create class method
        constructs a box and adds it to the world
        
        rect: a 6 part tuple with x,y,z,width,height,depth.
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        static: used to create this object static, if static is true, mass will be ignored
        """
        self.obj = pal.lib.create_transponder_sender(body.obj,c.c_float(max_distance))


    def delete(self):
        pal.lib.transponder_sender_remove(self.obj)
        del pal.sensor_objects[str(self.obj)]
