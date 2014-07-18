#include "../../globals.h"

extern "C"
{
    void* cast_static_convex_body_base(palStaticConvex* o)
    {
        return dynamic_cast<palBodyBase*>(o);
    }

    palStaticConvex* body_static_convex_create_no_triangles(Float x, Float y, Float z, Float rx, Float ry, Float rz, const Float *pVertices, int nVertices)
    {
        palStaticConvex *pc = dynamic_cast<palStaticConvex*>(PF->CreateObject("palStaticConvex")); //create a box
        palMatrix4x4 pos;
        mat_set_translation(&pos, x, y, z);
        mat_set_rotation(&pos, rx, ry, rz);
        pc->Init(pos, pVertices, nVertices);
        return pc;
    }

    palStaticConvex* body_static_convex_create_triangles(Float x, Float y, Float z, Float rx, Float ry, Float rz, const Float *pVertices, int nVertices, const int *pIndices, int nIndices)
    {

        palStaticConvex *pc = dynamic_cast<palStaticConvex*>(PF->CreateObject("palStaticConvex")); //create a box
        palMatrix4x4 pos;
        mat_set_translation(&pos, x, y, z);
        mat_set_rotation(&pos, rx, ry, rz);
        pc->Init(pos, pVertices, nVertices, pIndices, nIndices);
        return pc;
    }

    void body_static_convex_remove(palStaticConvex*o){
        delete o;
        o = NULL;
    }
}