#include "../../globals.h"

extern "C"
{
    void* cast_static_mesh_terrain_body_base(palTerrainMesh* o)
    {
        return dynamic_cast<palBodyBase*>(o);
    }

    palTerrainMesh* body_static_mesh_terrain_create(Float x, Float y, Float z, const Float *pVertices, int nVertices, const int *pIndices, int nIndices)
    {

        palTerrainMesh *pmt = dynamic_cast<palTerrainMesh*>(PF->CreateObject("palTerrainMesh")); //create a box
        pmt->Init(x,y,z, pVertices, nVertices, pIndices, nIndices);
        return pmt;
    }
}