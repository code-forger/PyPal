#include "../globals.h"

extern "C"
{
    void* cast_capsule_geometry(palCapsuleGeometry* o)
    {
        return dynamic_cast<palGeometry*>(o);
    }

    palCapsuleGeometry * geometry_capsule_create(Float x, Float y, Float z,Float rx, Float ry, Float rz, Float width, Float height, Float mass)
    {
        palCapsuleGeometry *cg= PF->CreateCapsuleGeometry ();
        palMatrix4x4 pos;
        mat_set_translation(&pos, x, y, z);
        mat_set_rotation(&pos, rx, ry, rz);
        cg->Init (pos, width, height, mass);
        return cg;
    }
}