#include "../globals.h"

extern "C"
{
    palCompassSensor* sensor_compass_create(palBody* b, Float x, Float y, Float z)
    {
        palCompassSensor *c= PF->CreateCompassSensor();
        c->Init(b,x,y,z);
        return c;
    }

    Float sensor_compass_get_angle(palCompassSensor* c)
    {
        return c->GetAngle();
    }
}