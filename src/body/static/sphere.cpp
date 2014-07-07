#include "../../globals.h"

extern "C"
{
    void body_static_sphere_get_location(palStaticSphere* s, float mat[16])
    {
        for (int i = 0; i < 16; i++)
            mat[i] = s->GetLocationMatrix()._mat[i];
    }

    void body_static_sphere_get_position(palStaticSphere* s, float vec[3])
    {
        palVector3 v;
        s->GetPosition(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    int body_static_sphere_get_group(palStaticSphere* s)
    {
        return s->GetGroup();
    }

    void body_static_sphere_set_group(palStaticSphere* s, int group)
    {
        s->SetGroup(group);
    }

    palStaticSphere* body_static_sphere_create(Float x, Float y, Float z, Float width)
    {
        palStaticSphere *ps = dynamic_cast<palStaticSphere *>(PF->CreateObject("palStaticSphere"));
        ps->Init(x,y,z,width);
        return ps;
    }
}