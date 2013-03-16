class Revolute():
    """a link that connects two objects rotationally"""
    def __init__(parent,child,pos,direction):
        """
        connects two objects together

        parent: the parent body
        child: the child body
        pos: a 3 part tuple for the position of the link
        direction: a 3 part unit vector of the driection of the link
        """
        pass

    def set_limits(lower,upper):
        """
        sets the maximum and the minimum rotational angle of the link in radians
        lower: the minimum angle
        upper: the maximum angle
        """
        pass

    def get_position():
        """
        returns the position of the link
        """

    def get_angle():
        """
        returns the angle of the link
        """
        pass

    def get_angular_velocity():
        """
        returns the angular velocity of the link
        """
        pass

    def apple_torque(torque):
        """
        applies a torque to the childabout the link
        torque: a floating point value
        """
        pass

    def apply_angular_impulse(torque):
        """
        applies a torque to the childabout the link
        torque: a floating point value
        """
        pass
