#include "../globals.h"

extern "C"
{
    void* cast_character_body(palCharacterController* o)
    {
        return dynamic_cast<palBody*>(o);
    }

    void* cast_character_body_base(palCharacterController* o)
    {
        return dynamic_cast<palBodyBase*>(o);
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