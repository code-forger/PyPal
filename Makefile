CXX           = g++
CXXFLAGS      = -fpermissive -c -fPIC
INCPATH       = -I /usr/local/include/pal


LIBCXXFLAGS      = -shared -Wl,-soname,libPyPal.so
LIBLIBS          = -L/usr/local/lib64/x86_64-linux-gnu/ -lpal -ldl -lpal_bullet

REQUIREDOBJECTS = build/PyPal.o\
				  build/body/box.o\
				  build/body/sphere.o

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


install: all
	install -m 0755 libPyPal.so /usr/local/lib


.PHONY: install
