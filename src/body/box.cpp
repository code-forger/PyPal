#include "../globals.h"

extern "C"
{
    void body_box_get_location(palBox* b, float mat[16])
    {
        for (int i = 0; i < 16; i++)
            mat[i] = b->GetLocationMatrix()._mat[i];
    }

    void body_box_get_position(palBox* b, float vec[3])
    {
        palVector3 v;
        b->GetPosition(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    int body_box_get_group(palBox* b)
    {
        return b->GetGroup();
    }

    void body_box_set_group(palBox* b, int group)
    {
        b->SetGroup(group);
    }

    void body_box_set_position(palBox* b, float x, float y, float z, float roll, float pitch, float yaw)
    {
        b->SetPosition(x, y, z, roll, pitch, yaw);
    }

    void body_box_set_orientation(palBox* b, float roll, float pitch, float yaw)
    {
        b->SetOrientation(roll, pitch, yaw);
    }

    void body_box_apply_force(palBox* b, float x, float y, float z)
    {
        b->ApplyForce(x, y, z);
    }

    void body_box_apply_torque(palBox* b, float x, float y, float z)
    {
        b->ApplyTorque(x, y, z);
    }

    void body_box_apply_force_at_position(palBox* b, float x, float y, float z, float px, float py, float pz)
    {
        b->ApplyForceAtPosition(x, y, z, pz, py, pz);
    }

    void body_box_apply_impulse(palBox* b, float ix, float iy, float iz)
    {
        b->ApplyImpulse(ix,iy,iz);
    }

    void body_box_apply_angular_impulse(palBox* b, float ix, float iy, float iz){
        b->ApplyAngularImpulse(ix, iy, iz);
    }

    void body_box_apply_impulse_at_position(palBox* b, float x, float y, float z, float px, float py, float pz)
    {
        b->ApplyImpulseAtPosition(x, y, z, pz, py, pz);
    }

    void body_box_get_linear_velocity(palBox* b, float vec[3])
    {
        palVector3 v;
        b->GetLinearVelocity(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    void body_box_get_angular_velocity(palBox* b, float vec[3])
    {
        palVector3 v;
        b->GetAngularVelocity(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    void body_box_set_linear_velocity(palBox* b, palVector3 v)
    {
        b->SetLinearVelocity(v);
    }

    void body_box_set_linear_angular(palBox* b, palVector3 v)
    {
        b->SetAngularVelocity(v);
    }

    bool body_box_is_active(palBox* b)
    {
        return b->IsActive();
    }

    void body_box_set_active(palBox* b,bool active)
    {
        b->SetActive(active);
    }

    palBox* body_box_create(Float x, Float y, Float z, Float width, Float height, Float depth, Float mass)
    {
        palBox *pb = PF->CreateBox();
        pb->Init(x,y,z,width,height,depth,mass);
        return pb;
    }
}