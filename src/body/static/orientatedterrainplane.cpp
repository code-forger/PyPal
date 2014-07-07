#include "../../globals.h"

extern "C"
{
    void body_static_orientated_terrain_plane_get_location(palOrientatedTerrainPlane* tp, float mat[16])
    {
        for (int i = 0; i < 16; i++)
            mat[i] = tp->GetLocationMatrix()._mat[i];
    }

    void body_static_orientated_terrain_plane_get_position(palOrientatedTerrainPlane* tp, float vec[3])
    {
        palVector3 v;
        tp->GetPosition(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    int body_static_orientated_terrain_plane_get_group(palOrientatedTerrainPlane* tp)
    {
        return tp->GetGroup();
    }

    void body_static_orientated_terrain_plane_set_group(palOrientatedTerrainPlane* tp, int group)
    {
        tp->SetGroup(group);
    }

    palOrientatedTerrainPlane* body_static_orientated_terrain_plane_create(Float x, Float y, Float z, Float nx, Float ny, Float nz, Float min_size)
    {
        palOrientatedTerrainPlane *ptp = dynamic_cast<palOrientatedTerrainPlane *>(PF->CreateObject("palOrientatedTerrainPlane"));
        ptp->Init(x,y,z,nx,ny,nz,min_size);
        return ptp;
    }
}