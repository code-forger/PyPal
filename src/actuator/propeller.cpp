#include "../globals.h"

extern "C"
{
    void actuator_propeller_apply(palPropeller *p)
    {
        p->Apply();
    }
    
    void actuator_propeller_set_voltage(palPropeller *p, float voltage)
    {
        p->SetVoltage(voltage);
    }

    palPropeller * actuator_propeller_create(palBody* pb, Float px, Float py, Float pz,
                                             Float ax, Float ay, Float az,
                                                 Float l)
    {
        palPropeller *pp= dynamic_cast<palPropeller*>(PF->CreateObject("palPropeller"));
        pp->Init(pb, px, pz, px,
                 ax, az, ax,
                 l);
        return pp;
    }
}