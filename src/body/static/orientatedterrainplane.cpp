#include "../../globals.h"

extern "C"
{
    void* cast_static_orientated_terrain_plane_body_base(palOrientatedTerrainPlane* o)
    {
        return dynamic_cast<palBodyBase*>(o);
    }

    palOrientatedTerrainPlane* body_static_orientated_terrain_plane_create(Float x, Float y, Float z, Float nx, Float ny, Float nz, Float min_size)
    {
        palOrientatedTerrainPlane *ptp = dynamic_cast<palOrientatedTerrainPlane *>(PF->CreateObject("palOrientatedTerrainPlane"));
        ptp->Init(x,y,z,nx,ny,nz,min_size);
        return ptp;
    }
}