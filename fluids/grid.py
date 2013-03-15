class Grid(GeometryBase):
    """a grid fluid"""
    def __init__(size,cell_size,density,dampening,linear_dampening,angular_dampening):
        """
        creates a grid liquid simulation

        size: a 2 part tuple of the size of the grig
	    cellSize: 	The real world size of the cell in the grid
	    density: 	The fluid density (eg: 1000)
	    dampening:	The damping coefficient for the fluid itself - controls the fluid's energy levels (try 0.04 - 0.0001)
	    linear_dampening: 	Linear damping (simplified version of palLiquidDrag)
	    angular_dampening: 	Angular damping (simplified version of palLiquidDrag) 
        """
        pass
