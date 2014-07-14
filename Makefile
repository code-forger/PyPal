CXX           = g++
CXXFLAGS      = -fpermissive -c -fPIC
INCPATH       = -I /usr/local/include/pal


LIBCXXFLAGS      = -shared -Wl,-soname,libPyPal.so
LIBLIBS          = -L/usr/local/lib64/x86_64-linux-gnu/ -lpal -ldl -lpal_bullet

REQUIREDOBJECTS = build/PyPal.o\
				  build/pypal.o\
				  build/body/box.o\
				  build/body/sphere.o\
				  build/body/capsule.o\
				  build/body/compound.o\
				  build/body/convex.o\
				  build/body/generic.o\
				  build/body/character.o\
				  build/body/static/box.o\
				  build/body/static/capsule.o\
				  build/body/static/sphere.o\
				  build/body/static/convex.o\
				  build/body/static/compound.o\
				  build/body/static/terrainplane.o\
				  build/body/static/orientatedterrainplane.o\
				  build/body/static/heightmapterrain.o\
				  build/body/static/meshterrain.o\
				  build/geometry/box.o\
				  build/geometry/capsule.o\
				  build/geometry/sphere.o\
				  build/geometry/convex.o\
				  build/actuator/force.o\
				  build/actuator/dcmotor.o\
				  build/actuator/fakebuoyancy.o\
				  build/actuator/liquiddrag.o\
				  build/actuator/propeller.o\
				  build/actuator/hydrofoil.o\
				  build/actuator/impulse.o

all: libPyPal.so

libPyPal.so: $(REQUIREDOBJECTS)
	g++ $(LIBCXXFLAGS) -o libPyPal.so $(REQUIREDOBJECTS)  $(LIBLIBS)

build/PyPal.o: src/PyPal.cpp
	g++ $(CXXFLAGS) $(INCPATH)  -c $< -o $@

build/pypal.o: src/pypal.cpp
	g++ $(CXXFLAGS) $(INCPATH)  -c $< -o $@

# body object rules
build/body/box.o: src/body/box.cpp
	g++ $(CXXFLAGS) $(INCPATH)  -c $< -o $@

build/body/sphere.o: src/body/sphere.cpp
	g++ $(CXXFLAGS) $(INCPATH)  -c $< -o $@

build/body/capsule.o: src/body/capsule.cpp
	g++ $(CXXFLAGS) $(INCPATH)  -c $< -o $@

build/body/compound.o: src/body/compound.cpp
	g++ $(CXXFLAGS) $(INCPATH)  -c $< -o $@

build/body/convex.o: src/body/convex.cpp
	g++ $(CXXFLAGS) $(INCPATH)  -c $< -o $@

build/body/generic.o: src/body/generic.cpp
	g++ $(CXXFLAGS) $(INCPATH)  -c $< -o $@

build/body/character.o: src/body/character.cpp
	g++ $(CXXFLAGS) $(INCPATH)  -c $< -o $@

# static body object rules
build/body/static/box.o: src/body/static/box.cpp
	g++ $(CXXFLAGS) $(INCPATH)  -c $< -o $@
	
build/body/static/capsule.o: src/body/static/capsule.cpp
	g++ $(CXXFLAGS) $(INCPATH)  -c $< -o $@
	
build/body/static/sphere.o: src/body/static/sphere.cpp
	g++ $(CXXFLAGS) $(INCPATH)  -c $< -o $@

build/body/static/convex.o: src/body/static/convex.cpp
	g++ $(CXXFLAGS) $(INCPATH)  -c $< -o $@

build/body/static/compound.o: src/body/static/compound.cpp
	g++ $(CXXFLAGS) $(INCPATH)  -c $< -o $@

build/body/static/terrainplane.o: src/body/static/terrainplane.cpp
	g++ $(CXXFLAGS) $(INCPATH)  -c $< -o $@

build/body/static/orientatedterrainplane.o: src/body/static/orientatedterrainplane.cpp
	g++ $(CXXFLAGS) $(INCPATH)  -c $< -o $@

build/body/static/heightmapterrain.o: src/body/static/heightmapterrain.cpp
	g++ $(CXXFLAGS) $(INCPATH)  -c $< -o $@

build/body/static/meshterrain.o: src/body/static/meshterrain.cpp
	g++ $(CXXFLAGS) $(INCPATH)  -c $< -o $@

# geometry body object rules
build/geometry/box.o: src/geometry/box.cpp
	g++ $(CXXFLAGS) $(INCPATH)  -c $< -o $@

build/geometry/capsule.o: src/geometry/capsule.cpp
	g++ $(CXXFLAGS) $(INCPATH)  -c $< -o $@

build/geometry/sphere.o: src/geometry/sphere.cpp
	g++ $(CXXFLAGS) $(INCPATH)  -c $< -o $@

build/geometry/convex.o: src/geometry/convex.cpp
	g++ $(CXXFLAGS) $(INCPATH)  -c $< -o $@

# actuator body object rules
build/actuator/force.o: src/actuator/force.cpp
	g++ $(CXXFLAGS) $(INCPATH)  -c $< -o $@

build/actuator/dcmotor.o: src/actuator/dcmotor.cpp
	g++ $(CXXFLAGS) $(INCPATH)  -c $< -o $@

build/actuator/fakebuoyancy.o: src/actuator/fakebuoyancy.cpp
	g++ $(CXXFLAGS) $(INCPATH)  -c $< -o $@

build/actuator/liquiddrag.o: src/actuator/liquiddrag.cpp
	g++ $(CXXFLAGS) $(INCPATH)  -c $< -o $@

build/actuator/propeller.o: src/actuator/propeller.cpp
	g++ $(CXXFLAGS) $(INCPATH)  -c $< -o $@

build/actuator/hydrofoil.o: src/actuator/hydrofoil.cpp
	g++ $(CXXFLAGS) $(INCPATH)  -c $< -o $@

build/actuator/impulse.o: src/actuator/impulse.cpp
	g++ $(CXXFLAGS) $(INCPATH)  -c $< -o $@


install: all
	install -m 0755 libPyPal.so /usr/local/lib


.PHONY: install
