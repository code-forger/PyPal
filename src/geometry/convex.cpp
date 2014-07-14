#include "../globals.h"

extern "C"
{
    void geometry_convex_get_location(palConvexGeometry* b, float mat[16])
    {
        for (int i = 0; i < 16; i++)
            mat[i] = b->GetLocationMatrix()._mat[i];
    }

    void geometry_convex_get_offsett(palConvexGeometry* b, float mat[16])
    {
        for (int i = 0; i < 16; i++)
            mat[i] = b->GetOffsetMatrix()._mat[i];
    }

    void geometry_convex_get_position(palConvexGeometry* b, float vec[3])
    {
        palVector3 v;
        b->GetPosition(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    void geometry_convex_set_mass(palConvexGeometry* bg, float mass)
    {
        bg->SetMass(mass);
    }

    float geometry_convex_get_mass(palConvexGeometry* bg)
    {
        return bg->GetMass();
    }

    float geometry_convex_get_margin(palConvexGeometry* bg)
    {
        return bg->GetMargin();
    }

    bool geometry_convex_set_margin(palConvexGeometry* bg, float margin)
    {
        return bg->SetMargin(margin);
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