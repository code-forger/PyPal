#include "../../globals.h"

extern "C"
{
    void body_static_terrain_plane_get_location(palTerrainPlane* tp, float mat[16])
    {
        for (int i = 0; i < 16; i++)
            mat[i] = tp->GetLocationMatrix()._mat[i];
    }

    void body_static_terrain_plane_get_position(palTerrainPlane* tp, float vec[3])
    {
        palVector3 v;
        tp->GetPosition(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    void body_static_terrain_plane_set_material(palTerrainPlane* tp, palMaterial* m)
    {
        tp->SetMaterial(m);
    }

    int body_static_terrain_plane_get_group(palTerrainPlane* tp)
    {
        return tp->GetGroup();
    }

    void body_static_terrain_plane_set_group(palTerrainPlane* tp, int group)
    {
        tp->SetGroup(group);
    }

    palTerrainPlane* body_static_terrain_plane_create(Float x, Float y, Float z, Float min_size)
    {
        palTerrainPlane *ptp = dynamic_cast<palTerrainPlane *>(PF->CreateObject("palTerrainPlane"));
        ptp->Init(x,y,z,min_size);
        return ptp;
    }
}