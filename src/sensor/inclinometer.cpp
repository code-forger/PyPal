#include "../globals.h"

extern "C"
{
    palInclinometerSensor* sensor_inclinometer_create(palBody* b, Float ax, Float ay, Float az
                                                   , Float ux, Float uy, Float uz
                                                   , Float gx, Float gy, Float gz)
    {
        palInclinometerSensor *i= PF->CreateInclinometerSensor();
        i->Init(b,ax,ay,az,ux,uy,uz,gx,gy,gz);
        return i;
    }

    Float sensor_inclinometer_get_angle(palInclinometerSensor* i)
    {
        return i->GetAngle();
    }
}