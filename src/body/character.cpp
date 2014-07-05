#include "../globals.h"

extern "C"
{
    void body_character_get_location(palCharacterController *pcc, float mat[16])
    {
        for (int i = 0; i < 16; i++)
            mat[i] = pcc->GetLocationMatrix()._mat[i];
    }

    void body_character_get_position(palCharacterController *pcc, float vec[3])
    {
        palVector3 v;
        pcc->GetPosition(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    int body_character_get_group(palCharacterController *pcc)
    {
        return pcc->GetGroup();
    }

    void body_character_set_group(palCharacterController *pcc, int group)
    {
        pcc->SetGroup(group);
    }

    void body_character_walk(palCharacterController*pcc,float x,float y,float z, float duration)
    {
        palVector3 direction;
        direction[0] = x;
        direction[1] = y;
        direction[2] = z;
        pcc->Walk(direction, duration);
    }

    void body_character_warp(palCharacterController*pcc,float x,float y,float z)
    {
        palVector3 direction;
        direction[0] = x;
        direction[1] = y;
        direction[2] = z;
        pcc->Warp(direction);
    }

    palCharacterController * body_character_create(Float x, Float y, Float z, Float radius, Float length)
    {
        palCharacterController *pcc = dynamic_cast<palCharacterController*>(PF->CreateObject("palCharacterController")); //create a box

        palCharacterControllerDesc desc;
        palCapsuleGeometry *pcg = PF->CreateCapsuleGeometry();

        palMatrix4x4 pos;
        mat_set_translation(&pos, x,y,z);
        mat_set_rotation(&pos, 0,0,0);
        pcg->Init (pos, radius, length, 1);
        desc.m_pShape = pcg;
        desc.m_Group = 1;
        pcc->Init(desc);
        palVector3 vec;
        vec[0] = x;
        vec[1] = y;
        vec[2] = z;
        pcc->Warp(vec);
        return pcc;
    }
}