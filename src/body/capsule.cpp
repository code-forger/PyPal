#include "../globals.h"

extern "C"
{
    void body_capsule_get_location(palCapsule* c, float mat[16])
    {
        for (int i = 0; i < 16; i++)
            mat[i] = c->GetLocationMatrix()._mat[i];
    }

    void body_capsule_get_position(palCapsule* c, float vec[3])
    {
        palVector3 v;
        c->GetPosition(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    int body_capsule_get_group(palCapsule* c)
    {
        return c->GetGroup();
    }

    void body_capsule_set_group(palCapsule* c, int group)
    {
        c->SetGroup(group);
    }

    void body_capsule_set_position(palCapsule* c, float x, float y, float z, float roll, float pitch, float yaw)
    {
        c->SetPosition(x, y, z, roll, pitch, yaw);
    }

    void body_capsule_set_orientation(palCapsule* c, float roll, float pitch, float yaw)
    {
        c->SetOrientation(roll, pitch, yaw);
    }

    void body_capsule_apply_force(palCapsule* c, float x, float y, float z)
    {
        c->ApplyForce(x, y, z);
    }

    void body_capsule_apply_torque(palCapsule* c, float x, float y, float z)
    {
        c->ApplyTorque(x, y, z);
    }

    void body_capsule_apply_force_at_position(palCapsule* c, float x, float y, float z, float px, float py, float pz)
    {
        c->ApplyForceAtPosition(x, y, z, pz, py, pz);
    }

    void body_capsule_apply_impulse(palCapsule* c, float ix, float iy, float iz)
    {
        c->ApplyImpulse(ix,iy,iz);
    }

    void body_capsule_apply_angular_impulse(palCapsule* c, float ix, float iy, float iz){
        c->ApplyAngularImpulse(ix, iy, iz);
    }

    void body_capsule_apply_impulse_at_position(palCapsule* c, float x, float y, float z, float px, float py, float pz)
    {
        c->ApplyImpulseAtPosition(x, y, z, pz, py, pz);
    }

    void body_capsule_get_linear_velocity(palCapsule* c, float vec[3])
    {
        palVector3 v;
        c->GetLinearVelocity(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    void body_capsule_get_angular_velocity(palCapsule* c, float vec[3])
    {
        palVector3 v;
        c->GetAngularVelocity(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    void body_capsule_set_linear_velocity(palCapsule* c, float vec[3])
    {
        palVector3 v;
        for (int i = 0; i < 3; i++)
            v._vec[i] = vec[i];
        c->SetLinearVelocity(v);
    }

    void body_capsule_set_angular_velocity(palCapsule* c, float vec[3])
    {
        palVector3 v;
        for (int i = 0; i < 3; i++)
            v._vec[i] = vec[i];
        c->SetAngularVelocity(v);
    }

    bool body_capsule_is_active(palCapsule* c)
    {
        return c->IsActive();
    }

    void body_capsule_set_active(palCapsule* c,bool active)
    {
        c->SetActive(active);
    }

    palCapsule* body_capsule_create(Float x, Float y, Float z, Float width, Float height, Float mass)
    {
        palCapsule *pc = PF->CreateCapsule();
        pc->Init(x,y,z,width,height,mass);
        return pc;
    }
}