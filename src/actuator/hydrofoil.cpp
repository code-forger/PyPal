#include "../globals.h"

extern "C"
{
    void actuator_hydrofoil_apply(palHydrofoil* h)
    {
        h->Apply();
    }

    void actuator_hydrofoil_set_angle(palHydrofoil* h, float angle)
    {
        h->SetAngle(angle);
    }

    palHydrofoil * actuator_hydrofoil_create_on_box(palBox* pb, Float px, Float py, Float pz,
                                                            Float ax, Float ay, Float az,
                                                            Float lx, Float ly, Float lz,
                                                            Float af,
                                                            Float a, Float b, Float c,
                                                            Float density)
    {
        palHydrofoil *ph= dynamic_cast<palHydrofoil*>(PF->CreateObject("palHydrofoil"));
        ph->Init(pb, px, pz, px,
                 ax, az, ax,
                 lx, lz, lx,
                 af,
                 a, b,  c,
                 density);
        return ph;
    }

    palHydrofoil * actuator_hydrofoil_create_on_sphere(palSphere* pb, Float px, Float py, Float pz,
                                                            Float ax, Float ay, Float az,
                                                            Float lx, Float ly, Float lz,
                                                            Float af,
                                                            Float a, Float b, Float c,
                                                            Float density)
    {
        palHydrofoil *ph= dynamic_cast<palHydrofoil*>(PF->CreateObject("palHydrofoil"));
        ph->Init(pb, px, pz, px,
                 ax, az, ax,
                 lx, lz, lx,
                 af,
                 a, b,  c,
                 density);
        return ph;
    }

    palHydrofoil * actuator_hydrofoil_create_on_capsule(palCapsule* pb, Float px, Float py, Float pz,
                                                            Float ax, Float ay, Float az,
                                                            Float lx, Float ly, Float lz,
                                                            Float af,
                                                            Float a, Float b, Float c,
                                                            Float density)
    {
        palHydrofoil *ph= dynamic_cast<palHydrofoil*>(PF->CreateObject("palHydrofoil"));
        ph->Init(pb, px, pz, px,
                 ax, az, ax,
                 lx, lz, lx,
                 af,
                 a, b,  c,
                 density);
        return ph;
    }

    palHydrofoil * actuator_hydrofoil_create_on_compound(palCompoundBody* pb, Float px, Float py, Float pz,
                                                            Float ax, Float ay, Float az,
                                                            Float lx, Float ly, Float lz,
                                                            Float af,
                                                            Float a, Float b, Float c,
                                                            Float density)
    {
        palHydrofoil *ph= dynamic_cast<palHydrofoil*>(PF->CreateObject("palHydrofoil"));
        ph->Init(pb, px, pz, px,
                 ax, az, ax,
                 lx, lz, lx,
                 af,
                 a, b,  c,
                 density);
        return ph;
    }

    palHydrofoil * actuator_hydrofoil_create_on_convex(palConvex* pb, Float px, Float py, Float pz,
                                                            Float ax, Float ay, Float az,
                                                            Float lx, Float ly, Float lz,
                                                            Float af,
                                                            Float a, Float b, Float c,
                                                            Float density)
    {
        palHydrofoil *ph= dynamic_cast<palHydrofoil*>(PF->CreateObject("palHydrofoil"));
        ph->Init(pb, px, pz, px,
                 ax, az, ax,
                 lx, lz, lx,
                 af,
                 a, b,  c,
                 density);
        return ph;
    }

    palHydrofoil * actuator_hydrofoil_create_on_generic(palGenericBody* pb, Float px, Float py, Float pz,
                                                            Float ax, Float ay, Float az,
                                                            Float lx, Float ly, Float lz,
                                                            Float af,
                                                            Float a, Float b, Float c,
                                                            Float density)
    {
        palHydrofoil *ph= dynamic_cast<palHydrofoil*>(PF->CreateObject("palHydrofoil"));
        ph->Init(pb, px, pz, px,
                 ax, az, ax,
                 lx, lz, lx,
                 af,
                 a, b,  c,
                 density);
        return ph;
    }
}