#include "../globals.h"

extern "C"
{
    void body_generic_get_location(palGenericBody* g, float mat[16])
    {
        for (int i = 0; i < 16; i++)
            mat[i] = g->GetLocationMatrix()._mat[i];
    }

    void body_generic_get_position(palGenericBody* g, float vec[3])
    {
        palVector3 v;
        g->GetPosition(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    int body_generic_get_group(palGenericBody* g)
    {
        return g->GetGroup();
    }

    void body_generic_set_group(palGenericBody* g, int group)
    {
        g->SetGroup(group);
    }

    void body_generic_set_position(palGenericBody* g, float x, float y, float z, float roll, float pitch, float yaw)
    {
        g->SetPosition(x, y, z, roll, pitch, yaw);
    }

    void body_generic_set_orientation(palGenericBody* g, float roll, float pitch, float yaw)
    {
        g->SetOrientation(roll, pitch, yaw);
    }

    void body_generic_apply_force(palGenericBody* g, float x, float y, float z)
    {
        g->ApplyForce(x, y, z);
    }

    void body_generic_apply_torque(palGenericBody* g, float x, float y, float z)
    {
        g->ApplyTorque(x, y, z);
    }

    void body_generic_apply_force_at_position(palGenericBody* g, float x, float y, float z, float px, float py, float pz)
    {
        g->ApplyForceAtPosition(x, y, z, pz, py, pz);
    }

    void body_generic_apply_impulse(palGenericBody* g, float ix, float iy, float iz)
    {
        g->ApplyImpulse(ix,iy,iz);
    }

    void body_generic_apply_angular_impulse(palGenericBody* g, float ix, float iy, float iz){
        g->ApplyAngularImpulse(ix, iy, iz);
    }

    void body_generic_apply_impulse_at_position(palGenericBody* g, float x, float y, float z, float px, float py, float pz)
    {
        g->ApplyImpulseAtPosition(x, y, z, pz, py, pz);
    }

    void body_generic_get_linear_velocity(palGenericBody* g, float vec[3])
    {
        palVector3 v;
        g->GetLinearVelocity(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    void body_generic_get_angular_velocity(palGenericBody* g, float vec[3])
    {
        palVector3 v;
        g->GetAngularVelocity(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    void body_generic_set_linear_velocity(palGenericBody* g, float vec[3])
    {
        palVector3 v;
        for (int i = 0; i < 3; i++)
            v._vec[i] = vec[i];
        g->SetLinearVelocity(v);
    }

    void body_generic_set_angular_velocity(palGenericBody* g, float vec[3])
    {
        palVector3 v;
        for (int i = 0; i < 3; i++)
            v._vec[i] = vec[i];
        g->SetAngularVelocity(v);
    }

    bool body_generic_is_active(palGenericBody* g)
    {
        return g->IsActive();
    }

    void body_generic_set_active(palGenericBody* g,bool active)
    {
        g->SetActive(active);
    }    

    void body_generic_set_dynamics_type(palGenericBody* g, char c)
    {
        palDynamicsType p;
        switch(c)
        {
        case 'd':
            p = PALBODY_DYNAMIC;
            break;
        case 's':
            p = PALBODY_DYNAMIC;
            break;
        case 'k':
            p = PALBODY_DYNAMIC;
            break;
        }
        g->SetDynamicsType(p);
    }

    void body_generic_set_gravity_enabled(palGenericBody* g, bool e)
    {
        g->SetGravityEnabled(e);
    }

    void body_generic_set_collision_response_enabled(palGenericBody* g, bool e)
    {
        g->SetCollisionResponseEnabled(e);
    }

    void body_generic_set_mass(palGenericBody* g, Float mass)
    {
        g->SetMass(mass);
    }

    void body_generic_set_inertia(palGenericBody* g, Float x, Float y, Float z)
    {
        g->SetInertia(x,y,z);
    }

    void body_generic_get_inertia(palGenericBody* g, Float &x, Float &y, Float &z)
    {
        g->GetInertia(x,y,z);
    }

    void body_generic_set_linear_damping(palGenericBody* g, Float linear_damping)
    {
        g->SetLinearDamping(linear_damping);
    }

    Float body_generic_get_linear_damping(palGenericBody* g)
    {
        return g->GetLinearDamping();
    }

    void body_generic_set_angular_damping(palGenericBody* g, Float angular_damping)
    {
        g->SetAngularDamping(angular_damping);
    }

    Float body_generic_get_angular_damping(palGenericBody* g)
    {
        return g->GetAngularDamping();
    }

    void body_generic_connect_box_geometry(palGenericBody* g,palBoxGeometry*geom)
    {
        g->ConnectGeometry(geom);
    }

    void body_generic_remove_box_geometry(palGenericBody* g,palGeometry*geom, char typechar)
    {
        //g->RemoveGeometry(GEOMCASTUP(typechar,geom));
    }

    palGenericBody* body_create_generic(Float x, Float y, Float z, Float rx, Float ry, Float rz)
    {
        palGenericBody *gb = dynamic_cast<palGenericBody*>(PF->CreateObject("palGenericBody")); //create a box
        palMatrix4x4 pos;
        mat_set_translation(&pos, x, y, z);
        mat_set_rotation(&pos, rx, ry, rz);
        gb->Init (pos);
        return gb;
    }
}