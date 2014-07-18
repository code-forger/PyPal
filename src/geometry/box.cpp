#include "../globals.h"

extern "C"
{
    void* cast_box_geometry(palBoxGeometry* o)
    {
        return dynamic_cast<palGeometry*>(o);
    }

    palBoxGeometry * geometry_box_create(Float x, Float y, Float z,Float rx, Float ry, Float rz, Float width, Float height, Float depth, Float mass)
    {
        palBoxGeometry *bg= PF->CreateBoxGeometry ();
        palMatrix4x4 pos;
        mat_set_translation(&pos, x, y, z);
        mat_set_rotation(&pos, rx, ry, rz);
        bg->Init (pos, width, height, depth, mass);
        return bg;
    }
}