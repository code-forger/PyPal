CXX           = g++
CXXFLAGS      = -fpermissive -c -fPIC
INCPATH       = -I /usr/local/include/pal


LIBCXXFLAGS      = -shared -Wl,-soname,libPyPal.so
LIBLIBS          = -L/usr/local/lib64/x86_64-linux-gnu/ -lpal -ldl -lpal_bullet

REQUIREDOBJECTS = build/PyPal.o\
				  build/body/box.o\
				  build/body/sphere.o\
				  build/body/capsule.o\
				  build/body/compound.o\
				  build/body/convex.o\
				  build/body/generic.o\
				  build/body/character.o\
				  build/body/static/box.o\
				  build/body/static/convex.o\
				  build/geometry/box.o

all: libPyPal.so

libPyPal.so: $(REQUIREDOBJECTS)
	g++ $(LIBCXXFLAGS) -o libPyPal.so $(REQUIREDOBJECTS)  $(LIBLIBS)

build/PyPal.o: src/PyPal.cpp
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

build/body/static/convex.o: src/body/static/convex.cpp
	g++ $(CXXFLAGS) $(INCPATH)  -c $< -o $@

# geometry body object rules
build/geometry/box.o: src/geometry/box.cpp
	g++ $(CXXFLAGS) $(INCPATH)  -c $< -o $@


install: all
	install -m 0755 libPyPal.so /usr/local/lib


.PHONY: install
