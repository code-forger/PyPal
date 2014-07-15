#include "../globals.h"

extern "C"
{
    void body_compound_get_location(palCompoundBody* c, float mat[16])
    {
        for (int i = 0; i < 16; i++)
            mat[i] = c->GetLocationMatrix()._mat[i];
    }

    void body_compound_get_position(palCompoundBody* c, float vec[3])
    {
        palVector3 v;
        c->GetPosition(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    void body_compound_set_material(palCompoundBody* c, palMaterial* m)
    {
        c->SetMaterial(m);
    }

    int body_compound_get_group(palCompoundBody* c)
    {
        return c->GetGroup();
    }

    void body_compound_set_group(palCompoundBody* c, int group)
    {
        c->SetGroup(group);
    }

    void body_compound_set_position(palCompoundBody* c, float x, float y, float z, float roll, float pitch, float yaw)
    {
        c->SetPosition(x, y, z, roll, pitch, yaw);
    }

    void body_compound_set_orientation(palCompoundBody* c, float roll, float pitch, float yaw)
    {
        c->SetOrientation(roll, pitch, yaw);
    }

    void body_compound_apply_force(palCompoundBody* c, float x, float y, float z)
    {
        c->ApplyForce(x, y, z);
    }

    void body_compound_apply_torque(palCompoundBody* c, float x, float y, float z)
    {
        c->ApplyTorque(x, y, z);
    }

    void body_compound_apply_force_at_position(palCompoundBody* c, float x, float y, float z, float px, float py, float pz)
    {
        c->ApplyForceAtPosition(x, y, z, pz, py, pz);
    }

    void body_compound_apply_impulse(palCompoundBody* c, float ix, float iy, float iz)
    {
        c->ApplyImpulse(ix,iy,iz);
    }

    void body_compound_apply_angular_impulse(palCompoundBody* c, float ix, float iy, float iz){
        c->ApplyAngularImpulse(ix, iy, iz);
    }

    void body_compound_apply_impulse_at_position(palCompoundBody* c, float x, float y, float z, float px, float py, float pz)
    {
        c->ApplyImpulseAtPosition(x, y, z, pz, py, pz);
    }

    void body_compound_get_linear_velocity(palCompoundBody* c, float vec[3])
    {
        palVector3 v;
        c->GetLinearVelocity(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    void body_compound_get_angular_velocity(palCompoundBody* c, float vec[3])
    {
        palVector3 v;
        c->GetAngularVelocity(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    void body_compound_set_linear_velocity(palCompoundBody* c, float vec[3])
    {
        palVector3 v;
        for (int i = 0; i < 3; i++)
            v._vec[i] = vec[i];
        c->SetLinearVelocity(v);
    }

    void body_compound_set_angular_velocity(palCompoundBody* c, float vec[3])
    {
        palVector3 v;
        for (int i = 0; i < 3; i++)
            v._vec[i] = vec[i];
        c->SetAngularVelocity(v);
    }

    bool body_compound_is_active(palCompoundBody* c)
    {
        return c->IsActive();
    }

    void body_compound_set_active(palCompoundBody* c,bool active)
    {
        c->SetActive(active);
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