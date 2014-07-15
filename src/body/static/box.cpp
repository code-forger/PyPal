#include "../../globals.h"

extern "C"
{
    void body_static_box_get_location(palStaticBox* b, float mat[16])
    {
        for (int i = 0; i < 16; i++)
            mat[i] = b->GetLocationMatrix()._mat[i];
    }

    void body_static_box_get_position(palStaticBox* b, float vec[3])
    {
        palVector3 v;
        b->GetPosition(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    void body_static_box_set_material(palStaticBox* b, palMaterial* m)
    {
        b->SetMaterial(m);
    }

    int body_static_box_get_group(palStaticBox* b)
    {
        return b->GetGroup();
    }

    void body_static_box_set_group(palStaticBox* b, int group)
    {
        b->SetGroup(group);
    }

    palStaticBox* body_static_box_create(Float x, Float y, Float z, Float width, Float height, Float depth)
    {
        palStaticBox *pb = dynamic_cast<palStaticBox *>(PF->CreateObject("palStaticBox"));
        pb->Init(x,y,z,width,height,depth);
        return pb;
    }
}