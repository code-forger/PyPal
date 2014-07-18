#include "../../globals.h"

extern "C"
{
    void* cast_static_heightmap_terrain_body_base(palTerrainHeightmap* o)
    {
        return dynamic_cast<palBodyBase*>(o);
    }

    palTerrainHeightmap * body_static_heightmap_terrain_create(Float x, Float y, Float z, Float width, Float depth, int terrain_data_width, int terrain_data_depth, const Float *pHeightmap)
    {
        palTerrainHeightmap *pth= PF->CreateTerrainHeightmap();
        pth->Init(x,y,z,width,depth,terrain_data_width,terrain_data_depth,pHeightmap);
        return pth;
    }
}