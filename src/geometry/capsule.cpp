#include "../globals.h"

extern "C"
{
    void geometry_capsule_get_location(palCapsuleGeometry* c, float mat[16])
    {
        for (int i = 0; i < 16; i++)
            mat[i] = c->GetLocationMatrix()._mat[i];
    }

    void geometry_capsule_get_offsett(palCapsuleGeometry* c, float mat[16])
    {
        for (int i = 0; i < 16; i++)
            mat[i] = c->GetOffsetMatrix()._mat[i];
    }

    void geometry_capsule_get_position(palCapsuleGeometry* c, float vec[3])
    {
        palVector3 v;
        c->GetPosition(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    void geometry_capsule_set_mass(palCapsuleGeometry* cg, float mass)
    {
        cg->SetMass(mass);
    }

    float geometry_capsule_get_mass(palCapsuleGeometry* cg)
    {
        return cg->GetMass();
    }

    float geometry_capsule_get_margin(palCapsuleGeometry* cg)
    {
        return cg->GetMargin();
    }

    bool geometry_capsule_set_margin(palCapsuleGeometry* cg, float margin)
    {
        return cg->SetMargin(margin);
    }


    palCapsuleGeometry * geometry_capsule_create(Float x, Float y, Float z,Float rx, Float ry, Float rz, Float width, Float height, Float mass)
    {
        palCapsuleGeometry *cg= PF->CreateCapsuleGeometry ();
        palMatrix4x4 pos;
        mat_set_translation(&pos, x, y, z);
        mat_set_rotation(&pos, rx, ry, rz);
        cg->Init (pos, width, height, mass);
        return cg;
    }
}