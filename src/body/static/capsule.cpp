#include "../../globals.h"

extern "C"
{
    void body_static_capsule_get_location(palStaticCapsule* c, float mat[16])
    {
        for (int i = 0; i < 16; i++)
            mat[i] = c->GetLocationMatrix()._mat[i];
    }

    void body_static_capsule_get_position(palStaticCapsule* c, float vec[3])
    {
        palVector3 v;
        c->GetPosition(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    void body_static_capsule_set_material(palStaticCapsule* c, palMaterial* m)
    {
        c->SetMaterial(m);
    }

    int body_static_capsule_get_group(palStaticCapsule* c)
    {
        return c->GetGroup();
    }

    void body_static_capsule_set_group(palStaticCapsule* c, int group)
    {
        c->SetGroup(group);
    }

    palStaticCapsule* body_static_capsule_create(Float x, Float y, Float z, Float width, Float height)
    {
        palStaticCapsule *pc = dynamic_cast<palStaticCapsule *>(PF->CreateObject("palStaticCapsule"));
        pc->Init(x,y,z,width,height);
        return pc;
    }
}