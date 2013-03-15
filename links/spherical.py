class Spherical(GeometryBase):
    """a link that connects two objects spherically"""
    def __init__(parent,child,pos):
        """
        connects two objects together

        parent: the parent body
        child: the child body
        pos: a 3 part tuple for the position of the link
        """
        pass

    def set_limits(cone,twist):
        """
        sets the movement limits of the link
        
        cone: limits the rotational movement to a cone specified in radiens
        twist: limits the twisting of the link specified in radiens
        """
