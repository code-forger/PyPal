#include "../globals.h"

extern "C"
{
    void body_sphere_get_location(palSphere* s, float mat[16])
    {
        for (int i = 0; i < 16; i++)
            mat[i] = s->GetLocationMatrix()._mat[i];
    }

    void body_sphere_get_position(palSphere* s, float vec[3])
    {
        palVector3 v;
        s->GetPosition(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    int body_sphere_get_group(palSphere* s)
    {
        return s->GetGroup();
    }

    void body_sphere_set_group(palSphere* s, int group)
    {
        s->SetGroup(group);
    }

    void body_sphere_set_position(palSphere* s, float x, float y, float z, float roll, float pitch, float yaw)
    {
        s->SetPosition(x, y, z, roll, pitch, yaw);
    }

    void body_sphere_set_orientation(palSphere* s, float roll, float pitch, float yaw)
    {
        s->SetOrientation(roll, pitch, yaw);
    }

    void body_sphere_apply_force(palSphere* s, float x, float y, float z)
    {
        s->ApplyForce(x, y, z);
    }

    void body_sphere_apply_torque(palSphere* s, float x, float y, float z)
    {
        s->ApplyTorque(x, y, z);
    }

    void body_sphere_apply_force_at_position(palSphere* s, float x, float y, float z, float px, float py, float pz)
    {
        s->ApplyForceAtPosition(x, y, z, pz, py, pz);
    }

    void body_sphere_apply_impulse(palSphere* s, float ix, float iy, float iz)
    {
        s->ApplyImpulse(ix,iy,iz);
    }

    void body_sphere_apply_angular_impulse(palSphere* s, float ix, float iy, float iz){
        s->ApplyAngularImpulse(ix, iy, iz);
    }

    void body_sphere_apply_impulse_at_position(palSphere* s, float x, float y, float z, float px, float py, float pz)
    {
        s->ApplyImpulseAtPosition(x, y, z, pz, py, pz);
    }

    void body_sphere_get_linear_velocity(palSphere* s, float vec[3])
    {
        palVector3 v;
        s->GetLinearVelocity(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    void body_sphere_get_angular_velocity(palSphere* s, float vec[3])
    {
        palVector3 v;
        s->GetAngularVelocity(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    void body_sphere_set_linear_velocity(palSphere* s, palVector3 v)
    {
        s->SetLinearVelocity(v);
    }

    void body_sphere_set_linear_angular(palSphere* s, palVector3 v)
    {
        s->SetAngularVelocity(v);
    }

    bool body_sphere_is_active(palSphere* s)
    {
        return s->IsActive();
    }

    void body_sphere_set_active(palSphere* s,bool active)
    {
        s->SetActive(active);
    }

    palSphere* body_sphere_create(Float x, Float y, Float z, Float width, Float mass)
    {
        palSphere *ps = PF->CreateSphere();
        ps->Init(x,y,z,width,mass);
        return ps;
    }
}