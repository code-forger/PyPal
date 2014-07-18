#include "../globals.h"

extern "C"
{
    void* cast_sphere_geometry(palSphereGeometry* o)
    {
        return dynamic_cast<palGeometry*>(o);
    }

    palSphereGeometry * geometry_sphere_create(Float x, Float y, Float z,Float rx, Float ry, Float rz, Float width, Float mass)
    {
        palSphereGeometry *sg= PF->CreateSphereGeometry ();
        palMatrix4x4 pos;
        mat_set_translation(&pos, x, y, z);
        mat_set_rotation(&pos, rx, ry, rz);
        sg->Init (pos, width, mass);
        return sg;
    }
}