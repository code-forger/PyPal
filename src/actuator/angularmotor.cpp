#include "../globals.h"

extern "C"
{
    void actuator_angular_motor_update(palAngularMotor* am, float target)
    {
        am->Update(target);
        am->Apply();
    }

    palAngularMotor* actuator_angular_motor_create(palRevoluteLink* rl, Float max)
    {
        palAngularMotor*pfa = dynamic_cast<palAngularMotor*>(PF->CreateObject("palAngularMotor"));
        pfa->Init(rl, max);
        return pfa;
    }
}