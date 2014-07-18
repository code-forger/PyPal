#include "../globals.h"

extern "C"
{
    void* cast_concave_geometry(palConcaveGeometry* o)
    {
        return dynamic_cast<palGeometry*>(o);
    }

    palConcaveGeometry* geometry_concave_create(Float x, Float y, Float z,Float rx, Float ry, Float rz, const Float *pVertices, int nVertices, const int *pIndices, int nIndices, Float mass)
    {

        palConcaveGeometry *pc = dynamic_cast<palConcaveGeometry*>(PF->CreateObject("palConcaveGeometry"));
        palMatrix4x4 pos;
        mat_set_translation(&pos, x, y, z);
        mat_set_rotation(&pos, rx, ry, rz);
        pc->Init(pos, pVertices, nVertices, pIndices, nIndices, mass);
        return pc;
    }

    void geometry_concave_remove(palConcaveGeometry*o){
        delete o;
        o = NULL;
    }
}