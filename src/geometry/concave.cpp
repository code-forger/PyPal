#include "../globals.h"

extern "C"
{
    void geometry_concave_get_location(palConcaveGeometry* b, float mat[16])
    {
        for (int i = 0; i < 16; i++)
            mat[i] = b->GetLocationMatrix()._mat[i];
    }

    void geometry_concave_get_offsett(palConcaveGeometry* b, float mat[16])
    {
        for (int i = 0; i < 16; i++)
            mat[i] = b->GetOffsetMatrix()._mat[i];
    }

    void geometry_concave_get_position(palConcaveGeometry* b, float vec[3])
    {
        palVector3 v;
        b->GetPosition(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    void geometry_concave_set_mass(palConcaveGeometry* bg, float mass)
    {
        bg->SetMass(mass);
    }

    float geometry_concave_get_mass(palConcaveGeometry* bg)
    {
        return bg->GetMass();
    }

    float geometry_concave_get_margin(palConcaveGeometry* bg)
    {
        return bg->GetMargin();
    }

    bool geometry_concave_set_margin(palConcaveGeometry* bg, float margin)
    {
        return bg->SetMargin(margin);
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