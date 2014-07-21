Getting Started
---------------

Here is a simple example of using PyPal.
It is described in more detail below.

.. literalinclude:: ../examples/basic_example.py
    :language: python
    :linenos:
    :lines: 3-15

The file is available as ``examples/basic_example.py`` in the 
source distribution.

Breakdown
+++++++++

.. literalinclude:: ../examples/basic_example.py
   :lines: 3

Here we import pypal, I oftern call it pal for brevity.

----------

.. literalinclude:: ../examples/basic_example.py
   :lines: 7

We create a TerrainPlane that is 50 by 50 wide at position 0, 0, 0.

Position is always the first parameter for objects that require location.

----------

.. literalinclude:: ../examples/basic_example.py
   :lines: 8

We create a dynamic box that is a 1m cube, 5m above the terrain.

Size is always the second parameter for objects that have size.

----------

.. literalinclude:: ../examples/basic_example.py
   :lines: 10

Here we set the simulation to go for 25 steps

----------

.. literalinclude:: ../examples/basic_example.py
   :lines: 11

Now we step the simulation forward by 0.02 of a second.

----------

.. literalinclude:: ../examples/basic_example.py
   :lines: 12-13

Here we print out the height of our box by using :func:`get_position()` and indexing to 1, the y value.

We also get the total time of the simulation by using :func:`pal.get_time()`

----------

.. literalinclude:: ../examples/basic_example.py
   :lines: 15

Finally we end the simulation and free all the alocated memory by calling :func:`cleanup()`
