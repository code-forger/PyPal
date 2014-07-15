#include "../globals.h"

extern "C"
{
    void actuator_spring_apply(palSpring* s)
    {
        s->Apply();
    }

    palSpring* actuator_spring_create(palBody* pb1, palBody* pb2, Float rl, Float ks, Float kd)
    {
        palSpring*ps = dynamic_cast<palSpring*>(PF->CreateObject("palSpring"));
        ps->Init(pb1,pb2,rl, ks, kd);
        return ps;
    }
}