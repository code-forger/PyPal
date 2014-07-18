#include "../globals.h"

extern "C"
{
    void* cast_sphere_body(palSphere* o)
    {
        return dynamic_cast<palBody*>(o);
    }

    void* cast_sphere_body_base(palSphere* o)
    {
        return dynamic_cast<palBodyBase*>(o);
    }

    palSphere* body_sphere_create(Float x, Float y, Float z, Float width, Float mass)
    {
        palSphere *ps = PF->CreateSphere();
        ps->Init(x,y,z,width,mass);
        return ps;
    }
}