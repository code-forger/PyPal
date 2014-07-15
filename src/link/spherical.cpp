#include "../globals.h"

extern "C"
{
    palSphericalLink * link_spherical_create(palBody *parent,palBody *child,Float x,Float y,
                                      Float z, bool collide)
    {
        palSphericalLink *psl= PF->CreateSphericalLink();
        psl->Init(parent,child,x,y,z,collide); //initialize it, set its location to 0,0,0 and minimum size to 50
        return psl;
    }

    float link_spherical_get_feedback(palSphericalLink* sl)
    {
        return sl->GetFeedback()->GetValue();
    }
    
    void link_spherical_set_limits(palSphericalLink* sl, float cone, float twist)
    {
        sl->SetLimits(cone, twist);
    }
}