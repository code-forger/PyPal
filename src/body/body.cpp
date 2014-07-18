#include "../globals.h"

extern "C"
{
    void body_set_position(palBody* b, float x, float y, float z, float roll, float pitch, float yaw)
    {
        b->SetPosition(x, y, z, roll, pitch, yaw);
    }

    void body_set_orientation(palBody* b, float roll, float pitch, float yaw)
    {
        b->SetOrientation(roll, pitch, yaw);
    }

    void body_apply_force(palBody* b, float x, float y, float z)
    {
        b->ApplyForce(x, y, z);
    }

    void body_apply_torque(palBody* b, float x, float y, float z)
    {
        b->ApplyTorque(x, y, z);
    }

    void body_apply_force_at_position(palBody* b, float x, float y, float z, float px, float py, float pz)
    {
        b->ApplyForceAtPosition(x, y, z, pz, py, pz);
    }

    void body_apply_impulse(palBody* b, float ix, float iy, float iz)
    {
        b->ApplyImpulse(ix,iy,iz);
    }

    void body_apply_angular_impulse(palBody* b, float ix, float iy, float iz){
        b->ApplyAngularImpulse(ix, iy, iz);
    }

    void body_apply_impulse_at_position(palBody* b, float x, float y, float z, float px, float py, float pz)
    {
        b->ApplyImpulseAtPosition(x, y, z, pz, py, pz);
    }

    void body_get_linear_velocity(palBody* b, float vec[3])
    {
        palVector3 v;
        b->GetLinearVelocity(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    void body_get_angular_velocity(palBody* b, float vec[3])
    {
        palVector3 v;
        b->GetAngularVelocity(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    void body_set_linear_velocity(palBody* b, float vec[3])
    {
        palVector3 v;
        for (int i = 0; i < 3; i++)
            v._vec[i] = vec[i];
        b->SetLinearVelocity(v);
    }

    void body_set_angular_velocity(palBody* b, float vec[3])
    {
        palVector3 v;
        for (int i = 0; i < 3; i++)
            v._vec[i] = vec[i];
        b->SetAngularVelocity(v);
    }

    bool body_is_active(palBody* b)
    {
        return b->IsActive();
    }

    void body_set_active(palBody* b,bool active)
    {
        b->SetActive(active);
    }
}