class Particle(GeometryBase):
    """a particle fluid"""
    def __init__():
        """
        must be called prior to to add_particle or finalize
        """
        pass

    def add_particle(pos,velocity):
        """
        adds a particle to the fluid
        
        pos: a 3 part tuple of the position of the particle
        velocity: a 3 part tuple of  the velocity of the particle
        """
        pass

    def finalize():
        """
        must be calledafter all the particles have been added.
        """
        pass

    def get_particles():
        """
        returns a list of all the particle positions
        """
        pass
