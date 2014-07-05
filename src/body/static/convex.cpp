#include "../../globals.h"

extern "C"
{
    void body_static_convex_get_location(palStaticConvex* c, float mat[16])
    {
        std::cout << "DEBUG!: ";
        for (int i = 0; i < 16; i++)
        {
            mat[i] = c->GetLocationMatrix()._mat[i];
            std::cout << c->GetLocationMatrix()._mat[i] << " ";
        }
        std::cout << std::endl;
    }

    void body_static_convex_get_position(palStaticConvex* c, float vec[3])
    {
        palVector3 v;
        c->GetPosition(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    int body_static_convex_get_group(palStaticConvex* c)
    {
        return c->GetGroup();
    }

    void body_static_convex_set_group(palStaticConvex* c, int group)
    {
        c->SetGroup(group);
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
}