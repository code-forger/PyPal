#include "../globals.h"

extern "C"
{
    void actuator_force_apply(palForceActuator* fa)
    {
        fa->Apply();
    }

    void actuator_force_set_force(palForceActuator* fa,float force)
    {
        fa->SetForce(force);
    }

    palForceActuator* actuator_force_create(palBody* pb, Float x, Float y, Float z, Float ax, Float ay, Float az)
    {
        palForceActuator*pfa = dynamic_cast<palForceActuator*>(PF->CreateObject("palForceActuator"));
        pfa->Init(pb,x,y,z,ax,ay,az);
        return pfa;
    }
}