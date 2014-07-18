#include "../../globals.h"

extern "C"
{
    void* cast_static_capsule_body_base(palStaticCapsule* o)
    {
        return dynamic_cast<palBodyBase*>(o);
    }

    palStaticCapsule* body_static_capsule_create(Float x, Float y, Float z, Float width, Float height)
    {
        palStaticCapsule *pc = dynamic_cast<palStaticCapsule *>(PF->CreateObject("palStaticCapsule"));
        pc->Init(x,y,z,width,height);
        return pc;
    }
}