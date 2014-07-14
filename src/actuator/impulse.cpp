#include "../globals.h"

extern "C"
{
    void actuator_impulse_apply(palImpulseActuator* i)
    {
        i->Apply();
    }

    void actuator_impulse_set_impulse(palImpulseActuator* i, float impulse)
    {
        i->SetImpulse(impulse);
    }

    palImpulseActuator* actuator_impulse_create(palBody* pb, Float x, Float y, Float z, Float ax, Float ay, Float az)
    {
        palImpulseActuator*pia = dynamic_cast<palImpulseActuator*>(PF->CreateObject("palImpulseActuator"));
        pia->Init(pb,x,y,z,ax,ay,az);
        return pia;
    }
}