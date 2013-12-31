CXX           = g++
CXXFLAGS      = -fpermissive -c -fPIC
INCPATH       = -I /usr/local/include/pal


LIBCXXFLAGS      = -shared -Wl,-soname,libPyPal.so
LIBLIBS          = -L/usr/local/lib64/x86_64-linux-gnu/ -lpal -ldl -lpal_bullet


all: libPyPal.so
	rm PyPal.o
	mv libPyPal.so libs/libPyPal.so

libPyPal.so: PyPal.o
	g++ $(LIBCXXFLAGS) -o libPyPal.so PyPal.o  $(LIBLIBS)

PyPal.o: PyPal.cpp
	g++ $(CXXFLAGS) $(INCPATH) PyPal.cpp


