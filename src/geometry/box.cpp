#include "../globals.h"

extern "C"
{
    void geometry_box_get_location(palBoxGeometry* b, float mat[16])
    {
        for (int i = 0; i < 16; i++)
            mat[i] = b->GetLocationMatrix()._mat[i];
    }

    void geometry_box_get_offsett(palBoxGeometry* b, float mat[16])
    {
        for (int i = 0; i < 16; i++)
            mat[i] = b->GetOffsetMatrix()._mat[i];
    }

    void geometry_box_get_position(palBoxGeometry* b, float vec[3])
    {
        palVector3 v;
        b->GetPosition(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    void geometry_box_set_mass(palBoxGeometry* bg, float mass)
    {
        bg->SetMass(mass);
    }

    float geometry_box_get_mass(palBoxGeometry* bg)
    {
        return bg->GetMass();
    }

    float geometry_box_get_margin(palBoxGeometry* bg)
    {
        return bg->GetMargin();
    }

    bool geometry_box_set_margin(palBoxGeometry* bg, float margin)
    {
        return bg->SetMargin(margin);
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