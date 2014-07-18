#include "../../globals.h"

extern "C"
{
    void* cast_static_sphere_body_base(palStaticSphere* o)
    {
        return dynamic_cast<palBodyBase*>(o);
    }

    palStaticSphere* body_static_sphere_create(Float x, Float y, Float z, Float width)
    {
        palStaticSphere *ps = dynamic_cast<palStaticSphere *>(PF->CreateObject("palStaticSphere"));
        ps->Init(x,y,z,width);
        return ps;
    }
}