#include "../globals.h"

extern "C"
{
    void* cast_compound_body(palCompoundBody* o)
    {
        return dynamic_cast<palBody*>(o);
    }

    void* cast_compound_body_base(palCompoundBody* o)
    {
        return dynamic_cast<palBodyBase*>(o);
    }

    palCompoundBody* body_compound_create(Float x, Float y, Float z)
    {
        palCompoundBody *pc = PF->CreateCompoundBody();
        pc->Init(x,y,z);
        return pc;
    }
    
    void body_compound_finalize(palCompoundBody* c)
    {
        c->Finalize();
    }

    void body_compound_add_box(palCompoundBody*c, Float x, Float y, Float z,
                                             Float rx, Float ry, Float rz,
                                             Float width, Float height,
                                             Float depth, Float mass)
    {
        palBoxGeometry*pbg = c->AddBox();

        palMatrix4x4 pos;
        mat_set_translation(&pos, x, y, z);
        mat_set_rotation(&pos, rx, ry, rz);
        pbg->Init (pos, width, height, depth, mass);
    }
    
    void body_compound_add_sphere(palCompoundBody*c, Float x, Float y, Float z,
                                             Float rx, Float ry, Float rz, Float radius, Float mass)
    {
        palSphereGeometry*psg = c->AddSphere();

        palMatrix4x4 pos;
        mat_set_translation(&pos, x, y, z);
        mat_set_rotation(&pos, rx, ry, rz);
        psg->Init (pos, radius, mass);
    }
    
    void body_compound_add_capsule(palCompoundBody*c, Float x, Float y, Float z,
                                             Float rx, Float ry, Float rz, Float radius, Float height, Float mass)
    {
        palCapsuleGeometry*pcg = c->AddCapsule();

        palMatrix4x4 pos;
        mat_set_translation(&pos, x, y, z);
        mat_set_rotation(&pos, rx, ry, rz);
        pcg->Init (pos, radius, height, mass);
    }
    
    void body_compound_add_convex(palCompoundBody*c, Float x, Float y, Float z,
                                             Float rx, Float ry, Float rz, const Float *pVertices, int nVertices, Float mass)
    {
        palConvexGeometry*pcg = dynamic_cast<palConvexGeometry*>(c->AddGeometry("palConvexGeometry"));

        palMatrix4x4 pos;
        mat_set_translation(&pos, x, y, z);
        mat_set_rotation(&pos, rx, ry, rz);
        pcg->Init (pos, pVertices, nVertices, mass);
    }
}