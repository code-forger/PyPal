#include "../globals.h"

extern "C"
{
    void body_base_get_location(palBodyBase* b, float mat[16])
    {
        for (int i = 0; i < 16; i++)
            mat[i] = b->GetLocationMatrix()._mat[i];
    }

    void body_base_get_position(palBodyBase* b, float vec[3])
    {
        palVector3 v;
        b->GetPosition(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    void body_base_set_material(palBodyBase* b, palMaterial* m)
    {
        b->SetMaterial(m);
    }

    int body_base_get_group(palBodyBase* b)
    {
        return b->GetGroup();
    }

    void body_base_set_group(palBodyBase* b, int group)
    {
        b->SetGroup(group);
    }
}