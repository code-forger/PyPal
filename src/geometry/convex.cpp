#include "../globals.h"

extern "C"
{
    void* cast_convex_geometry(palConvexGeometry* o)
    {
        return dynamic_cast<palGeometry*>(o);
    }

    palConvexGeometry* geometry_convex_create_no_triangles(Float x, Float y, Float z,Float rx, Float ry, Float rz, const Float *pVertices, int nVertices, Float mass)
    {
        palConvexGeometry *pc = dynamic_cast<palConvexGeometry*>(PF->CreateObject("palConvexGeometry")); //create a box
        palMatrix4x4 pos;
        mat_set_translation(&pos, x, y, z);
        mat_set_rotation(&pos, rx, ry, rz);
        pc->Init(pos, pVertices, nVertices, mass);
        return pc;
    }

    palConvexGeometry* geometry_convex_create_triangles(Float x, Float y, Float z,Float rx, Float ry, Float rz, const Float *pVertices, int nVertices, const int *pIndices, int nIndices, Float mass)
    {

        palConvexGeometry *pc = dynamic_cast<palConvexGeometry*>(PF->CreateObject("palConvexGeometry"));
        palMatrix4x4 pos;
        mat_set_translation(&pos, x, y, z);
        mat_set_rotation(&pos, rx, ry, rz);
        pc->Init(pos, pVertices, nVertices, pIndices, nIndices, mass);
        return pc;
    }

    void geometry_convex_remove(palConvexGeometry*o){
        delete o;
        o = NULL;
    }
}