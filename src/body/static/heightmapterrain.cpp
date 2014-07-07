#include "../../globals.h"

extern "C"
{
    void body_static_heightmap_terrain_get_location(palTerrainHeightmap* hmt, float mat[16])
    {
        for (int i = 0; i < 16; i++)
            mat[i] = hmt->GetLocationMatrix()._mat[i];
    }

    void body_static_heightmap_terrain_get_position(palTerrainHeightmap* hmt, float vec[3])
    {
        palVector3 v;
        hmt->GetPosition(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    int body_static_heightmap_terrain_get_group(palTerrainHeightmap* hmt)
    {
        return hmt->GetGroup();
    }

    void body_static_heightmap_terrain_set_group(palTerrainHeightmap* hmt, int group)
    {
        hmt->SetGroup(group);
    }
    
    palTerrainHeightmap * body_static_heightmap_terrain_create(Float x, Float y, Float z, Float width, Float depth, int terrain_data_width, int terrain_data_depth, const Float *pHeightmap)
    {
        palTerrainHeightmap *pth= PF->CreateTerrainHeightmap();
        pth->Init(x,y,z,width,depth,terrain_data_width,terrain_data_depth,pHeightmap);
        return pth;
    }
}