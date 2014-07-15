#include "../../globals.h"

extern "C"
{
    void body_static_mesh_terrain_get_location(palTerrainMesh* mt, float mat[16])
    {
        for (int i = 0; i < 16; i++)
            mat[i] = mt->GetLocationMatrix()._mat[i];
    }

    void body_static_mesh_terrain_get_position(palTerrainMesh* mt, float vec[3])
    {
        palVector3 v;
        mt->GetPosition(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    void body_static_mesh_terrain_set_material(palTerrainMesh* mt, palMaterial* m)
    {
        mt->SetMaterial(m);
    }

    int body_static_mesh_terrain_get_group(palTerrainMesh* mt)
    {
        return mt->GetGroup();
    }

    void body_static_mesh_terrain_set_group(palTerrainMesh* mt, int group)
    {
        mt->SetGroup(group);
    }

    palTerrainMesh* body_static_mesh_terrain_create(Float x, Float y, Float z, const Float *pVertices, int nVertices, const int *pIndices, int nIndices)
    {

        palTerrainMesh *pmt = dynamic_cast<palTerrainMesh*>(PF->CreateObject("palTerrainMesh")); //create a box
        pmt->Init(x,y,z, pVertices, nVertices, pIndices, nIndices);
        return pmt;
    }
}