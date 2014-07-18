#include "../globals.h"

extern "C"
{
    void* cast_capsule_body(palCapsule* o)
    {
        return dynamic_cast<palBody*>(o);
    }

    void* cast_capsule_body_base(palCapsule* o)
    {
        return dynamic_cast<palBodyBase*>(o);
    }

    palCapsule* body_capsule_create(Float x, Float y, Float z, Float width, Float height, Float mass)
    {
        palCapsule *pc = PF->CreateCapsule();
        pc->Init(x,y,z,width,height,mass);
        return pc;
    }
}