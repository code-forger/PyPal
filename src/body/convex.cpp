#include "../globals.h"

extern "C"
{
    void* cast_convex_body(palConvex* o)
    {
        return dynamic_cast<palBody*>(o);
    }

    void* cast_convex_body_base(palConvex* o)
    {
        return dynamic_cast<palBodyBase*>(o);
    }

    palConvex* body_convex_create_no_triangles(Float x, Float y, Float z, const Float *pVertices, int nVertices, Float mass)
    {
        palConvex *pc = dynamic_cast<palConvex*>(PF->CreateObject("palConvex")); //create a box
        pc->Init(x, y, z, pVertices, nVertices, mass);
        return pc;
    }

    palConvex* body_convex_create_triangles(Float x, Float y, Float z, const Float *pVertices, int nVertices, const int *pIndices, int nIndices, Float mass)
    {

        palConvex *pc = dynamic_cast<palConvex*>(PF->CreateObject("palConvex")); //create a box
        pc->Init(x,y,z, pVertices, nVertices, pIndices, nIndices, mass);
        return pc;
    }

    void body_convex_remove(palConvex*o){
        delete o;
        o = NULL;
    }
}