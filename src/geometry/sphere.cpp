#include "../globals.h"

extern "C"
{
    void geometry_sphere_get_location(palSphereGeometry* b, float mat[16])
    {
        for (int i = 0; i < 16; i++)
            mat[i] = b->GetLocationMatrix()._mat[i];
    }

    void geometry_sphere_get_offsett(palSphereGeometry* b, float mat[16])
    {
        for (int i = 0; i < 16; i++)
            mat[i] = b->GetOffsetMatrix()._mat[i];
    }

    void geometry_sphere_get_position(palSphereGeometry* b, float vec[3])
    {
        palVector3 v;
        b->GetPosition(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    void geometry_sphere_set_mass(palSphereGeometry* sg, float mass)
    {
        sg->SetMass(mass);
    }

    float geometry_sphere_get_mass(palSphereGeometry* sg)
    {
        return sg->GetMass();
    }

    float geometry_sphere_get_margin(palSphereGeometry* sg)
    {
        return sg->GetMargin();
    }

    bool geometry_sphere_set_margin(palSphereGeometry* sg, float margin)
    {
        sg->SetMargin(margin);
    }


    palSphereGeometry * geometry_sphere_create(Float x, Float y, Float z,Float rx, Float ry, Float rz, Float width, Float mass)
    {
        palSphereGeometry *sg= PF->CreateSphereGeometry ();
        palMatrix4x4 pos;
        mat_set_translation(&pos, x, y, z);
        mat_set_rotation(&pos, rx, ry, rz);
        sg->Init (pos, width, mass);
        return sg;
    }
}