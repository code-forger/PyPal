CXX           = g++
CXXFLAGS      = -fpermissive -c -fPIC
INCPATH       = -I /usr/local/include/pal


LIBCXXFLAGS      = -shared -Wl,-soname,libPyPal.so
LIBLIBS          = -L/usr/local/lib64/x86_64-linux-gnu/ -lpal -ldl -lpal_bullet


all: libPyPal.so
	rm PyPal.o

libPyPal.so: PyPal.o
	g++ $(LIBCXXFLAGS) -o libPyPal.so PyPal.o  $(LIBLIBS)

PyPal.o: src/PyPal.cpp
	g++ $(CXXFLAGS) $(INCPATH) src/PyPal.cpp

install: all
	install -m 0755 libPyPal.so /usr/local/lib


.PHONY: install
