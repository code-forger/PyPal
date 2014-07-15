#include "../globals.h"

extern "C"
{
    palPSDSensor* sensor_psd_create(palBody* b, Float x, Float y, Float z
                                      , Float ax, Float ay, Float az
                                      , Float range)
    {
        palPSDSensor *p= PF->CreatePSDSensor();
        p->Init(b,x,y,z,ax,ay,az,range);
        return p;
    }

    Float sensor_psd_get_distance(palPSDSensor* p)
    {
        return p->GetDistance();
    }
}