Example Two
---------------

This example will introduce:
  Two new types of pypal objects: 
    Actuators and Links
  A new type of dynamic body:
    Sphere
  A new type of static body:
    StaticBox
  And a simple 3D rendering utility for prototyping with pypal.

Here is the example in full:

.. literalinclude:: ../examples/example_two.py
    :language: python
    :linenos:

The file is available as ``examples/example_two.py`` in the 
source distribution.

Breakdown
+++++++++

 Lines 1 - 25 aren't too important, they simply set up the rendering correctly.

----------

.. literalinclude:: ../examples/example_two.py
   :lines: 28-45

Here we setup pypal and begin creating objects.
The only thing here that is new is the StaticBox.

The StaticBox has the same parameters as the Box, except it has no mass.

----------

.. literalinclude:: ../examples/example_two.py
   :lines: 48-58

Here we are setting up graphical objects for all the physics objects we just created, the glh.Box class takes either a Box, a StaticBox, or a TerrainPlane as its first parameter and a (r,g,b) color as its second. the color values are in range 0-1.

----------

.. literalinclude:: ../examples/example_two.py
   :lines: 60-64

Here we are adding in all our balls to both the physics engine and the graphics engine.

The Sphere class has an (x, y, z) position just like the Box, but only has (radius) for its size.

We decide to use the default mass of 1. for these spheres.

the glh.Ball class takes either a Sphere or StaticSphere as its first parameter and a color as the second.

----------

.. literalinclude:: ../examples/example_two.py
   :lines: 67

Here we are creating our first link, The Revolute link allows for rotational motion around an axis.

its 5 parameters are as follows:
1: the parent body that can be any object from pypal.body
2: the child body that can be any object from pypal.body
3: the x, y, z position of the center of the link
4: the axis that the rotation will take place.
5: a bool dictation if the objects involved should collide.

We have chosen to put the center of the link at the center or our 'anchor' object, we achieve this by calling :func:`get_position()` on out 'anchor'

We also want the rotation to take place about the y axis, so out axis unit vector is [0, 1, 0]

----------

.. literalinclude:: ../examples/example_two.py
   :lines: 69 - 71

Now we add a DCMotor to the simulations.

It takes a revolute link as its first parameter,
the final three parameters ar the torque, emf, and resistance of the motor

We next set the voltage for the motor.

Then we turn it on.
Note: rather than turning the motor on, we could have used the :func:`apply()` function on it every time the physics engine is updated, in-fact, that is all that turning a motor on does.

----------

.. literalinclude:: ../examples/example_two.py
   :lines: 74 - 82

This is our main loop.

we are only really concerned about line 77 and 78:

:func:`pal.update(1./50.)` will update our physics engine at 50 frames a second

:func:`glh.render(objects)` will render all our objects to the screen.


----------

.. literalinclude:: ../examples/example_two.py
   :lines: 84

Finally, as always, we clean up after ourselves.