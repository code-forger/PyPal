#include "../../globals.h"

extern "C"
{
    void* cast_static_terrain_plane_body_base(palTerrainPlane* o)
    {
        return dynamic_cast<palBodyBase*>(o);
    }

    palTerrainPlane* body_static_terrain_plane_create(Float x, Float y, Float z, Float min_size)
    {
        palTerrainPlane *ptp = dynamic_cast<palTerrainPlane *>(PF->CreateObject("palTerrainPlane"));
        ptp->Init(x,y,z,min_size);
        return ptp;
    }
}