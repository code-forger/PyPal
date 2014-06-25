#include "../globals.h"

extern "C"
{
    void body_convex_get_location(palConvex* c, float mat[16])
    {
        for (int i = 0; i < 16; i++)
            mat[i] = c->GetLocationMatrix()._mat[i];
    }

    void body_convex_get_position(palConvex* c, float vec[3])
    {
        palVector3 v;
        c->GetPosition(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    int body_convex_get_group(palConvex* c)
    {
        return c->GetGroup();
    }

    void body_convex_set_group(palConvex* c, int group)
    {
        c->SetGroup(group);
    }

    void body_convex_set_position(palConvex* c, float x, float y, float z, float roll, float pitch, float yaw)
    {
        c->SetPosition(x, y, z, roll, pitch, yaw);
    }

    void body_convex_set_orientation(palConvex* c, float roll, float pitch, float yaw)
    {
        c->SetOrientation(roll, pitch, yaw);
    }

    void body_convex_apply_force(palConvex* c, float x, float y, float z)
    {
        c->ApplyForce(x, y, z);
    }

    void body_convex_apply_torque(palConvex* c, float x, float y, float z)
    {
        c->ApplyTorque(x, y, z);
    }

    void body_convex_apply_force_at_position(palConvex* c, float x, float y, float z, float px, float py, float pz)
    {
        c->ApplyForceAtPosition(x, y, z, pz, py, pz);
    }

    void body_convex_apply_impulse(palConvex* c, float ix, float iy, float iz)
    {
        c->ApplyImpulse(ix,iy,iz);
    }

    void body_convex_apply_angular_impulse(palConvex* c, float ix, float iy, float iz){
        c->ApplyAngularImpulse(ix, iy, iz);
    }

    void body_convex_apply_impulse_at_position(palConvex* c, float x, float y, float z, float px, float py, float pz)
    {
        c->ApplyImpulseAtPosition(x, y, z, pz, py, pz);
    }

    void body_convex_get_linear_velocity(palConvex* c, float vec[3])
    {
        palVector3 v;
        c->GetLinearVelocity(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    void body_convex_get_angular_velocity(palConvex* c, float vec[3])
    {
        palVector3 v;
        c->GetAngularVelocity(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    void body_convex_set_linear_velocity(palConvex* c, palVector3 v)
    {
        c->SetLinearVelocity(v);
    }

    void body_convex_set_linear_angular(palConvex* c, palVector3 v)
    {
        c->SetAngularVelocity(v);
    }

    bool body_convex_is_active(palConvex* c)
    {
        return c->IsActive();
    }

    void body_convex_set_active(palConvex* c,bool active)
    {
        c->SetActive(active);
    }

    palConvex* body_convex_create_no_triangles(Float x, Float y, Float z, const Float *pVertices, int nVertices, Float mass)
    {
        palConvex *pc = dynamic_cast<palConvex*>(PF->CreateObject("palConvex")); //create a box
        pc->Init(x, y, z, pVertices, nVertices, mass);
        return pc;
    }

    palConvex* body_convex_create_triangles(Float x, Float y, Float z, const Float *pVertices, int nVertices, const int *pIndices, int nIndices, Float mass)
    {

        palConvex *pc = dynamic_cast<palConvex*>(PF->CreateObject("palConvex")); //create a box
        pc->Init(x,y,z, pVertices, nVertices, pIndices, nIndices, mass);
        return pc;
    }
}