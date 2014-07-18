#include "../globals.h"

extern "C"
{
    void geometry_get_location(palGeometry* b, float mat[16])
    {
        for (int i = 0; i < 16; i++)
            mat[i] = b->GetLocationMatrix()._mat[i];
    }

    void geometry_get_offsett(palGeometry* b, float mat[16])
    {
        for (int i = 0; i < 16; i++)
            mat[i] = b->GetOffsetMatrix()._mat[i];
    }

    void geometry_get_position(palGeometry* b, float vec[3])
    {
        palVector3 v;
        b->GetPosition(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    void geometry_set_mass(palGeometry* bg, float mass)
    {
        bg->SetMass(mass);
    }

    float geometry_get_mass(palGeometry* bg)
    {
        return bg->GetMass();
    }

    float geometry_get_margin(palGeometry* bg)
    {
        return bg->GetMargin();
    }

    bool geometry_set_margin(palGeometry* bg, float margin)
    {
        return bg->SetMargin(margin);
    }
}