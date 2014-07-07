#include "../../globals.h"

extern "C"
{
    void body_static_compound_get_location(palStaticCompoundBody* cb, float mat[16])
    {
        for (int i = 0; i < 16; i++)
            mat[i] = cb->GetLocationMatrix()._mat[i];
    }

    void body_static_compound_get_position(palStaticCompoundBody* cb, float vec[3])
    {
        palVector3 v;
        cb->GetPosition(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    int body_static_compound_get_group(palStaticCompoundBody* cb)
    {
        return cb->GetGroup();
    }

    void body_static_compound_set_group(palStaticCompoundBody* cb, int group)
    {
        cb->SetGroup(group);
    }

    palStaticCompoundBody* body_static_compound_create(Float x, Float y, Float z)
    {
        palStaticCompoundBody *pcb = dynamic_cast<palStaticCompoundBody *>(PF->CreateObject("palStaticCompoundBody"));
        pcb->Init(x,y,z);
        return pcb;
    }


    void body_static_compound_finalize(palStaticCompoundBody*cb)
    {
        cb->Finalize();
    }

    void body_static_compound_add_box(palStaticCompoundBody*cb, Float x, Float y, Float z,
                                             Float rx, Float ry, Float rz,
                                             Float width, Float height,
                                             Float depth, Float mass)
    {
        palBoxGeometry*pbg = cb->AddBox();

        palMatrix4x4 pos;
        mat_set_translation(&pos, x, y, z);
        mat_set_rotation(&pos, rx, ry, rz);
        pbg->Init (pos, width, height, depth, mass);
    }
    
    void body_static_compound_add_sphere(palStaticCompoundBody*cb, Float x, Float y, Float z,
                                             Float rx, Float ry, Float rz, Float radius, Float mass)
    {
        palSphereGeometry*psg = cb->AddSphere();

        palMatrix4x4 pos;
        mat_set_translation(&pos, x, y, z);
        mat_set_rotation(&pos, rx, ry, rz);
        psg->Init (pos, radius, mass);
    }
    
    void body_static_compound_add_capsule(palStaticCompoundBody*cb, Float x, Float y, Float z,
                                             Float rx, Float ry, Float rz, Float radius, Float height, Float mass)
    {
        palCapsuleGeometry*pcg = cb->AddCapsule();

        palMatrix4x4 pos;
        mat_set_translation(&pos, x, y, z);
        mat_set_rotation(&pos, rx, ry, rz);
        pcg->Init (pos, radius, height, mass);
    }
    
    void body_static_compound_add_convex(palStaticCompoundBody*cb, Float x, Float y, Float z,
                                             Float rx, Float ry, Float rz, const Float *pVertices, int nVertices, Float mass)
    {
        palConvexGeometry*pcg = dynamic_cast<palConvexGeometry*>(cb->AddGeometry("palConvexGeometry"));

        palMatrix4x4 pos;
        mat_set_translation(&pos, x, y, z);
        mat_set_rotation(&pos, rx, ry, rz);
        pcg->Init (pos, pVertices, nVertices, mass);
    }
}