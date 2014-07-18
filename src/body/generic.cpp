#include "../globals.h"

extern "C"
{
    void* cast_generic_body(palGenericBody* o)
    {
        return dynamic_cast<palBody*>(o);
    }

    void* cast_generic_body_base(palGenericBody* o)
    {
        return dynamic_cast<palBodyBase*>(o);
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

    void body_generic_connect_geometry(palGenericBody* g,palGeometry*geom)
    {
        g->ConnectGeometry(geom);
    }

    void body_generic_connect_capsule_geometry(palGenericBody* g,palCapsuleGeometry*geom)
    {
        g->ConnectGeometry(geom);
    }

    void body_generic_connect_convex_geometry(palGenericBody* g,palConvexGeometry*geom)
    {
        g->ConnectGeometry(geom);
    }

    void body_generic_connect_concave_geometry(palGenericBody* g,palConcaveGeometry*geom)
    {
        g->ConnectGeometry(geom);
    }

    void body_generic_connect_sphere_geometry(palGenericBody* g,palSphereGeometry*geom)
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