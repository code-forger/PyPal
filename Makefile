#pypal(){
#    g++ -fpermissive -c -fPIC -I /home/m/BuildEnv/pal-code/build -I /home/m/BuildEnv/pal-code PyPalGame.cpp -o PyPalGame.o
#    g++ -shared -Wl,-soname,libPyPalGame.so  -o libPyPalGame.so PyPalGame.o -L/usr/local/lib64/x86_64-linux-gnu/  -lpal -ldl -lpal_bullet
#    rm PyPalGame.o
#    mv libPyPalGame.so libs/libPyPalGame.so
#}

CXX           = g++
CXXFLAGS      = -fpermissive -c -fPIC
INCPATH       = -I /home/m/BuildEnv/pal-code/build -I /home/m/BuildEnv/pal-code


LIBCXXFLAGS      = -shared -Wl,-soname,libPyPalGame.so
LIBLIBS          = -L/usr/local/lib64/x86_64-linux-gnu/ -lpal -ldl -lpal_bullet


all: libPyPalGame.so
	rm PyPalGame.o
	mv libPyPalGame.so libs/libPyPalGame.so

libPyPalGame.so: PyPalGame.o
	g++ $(LIBCXXFLAGS) -o libPyPalGame.so PyPalGame.o  $(LIBLIBS)

PyPalGame.o: PyPalGame.cpp
	g++ $(CXXFLAGS) $(INCPATH) PyPalGame.cpp


