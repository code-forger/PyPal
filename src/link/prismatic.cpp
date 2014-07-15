#include "../globals.h"

extern "C"
{
    palPrismaticLink * link_prismatic_create(palBody *parent,palBody *child,Float x,Float y,
                                      Float z, Float axis_x,Float axis_y, Float axis_z, bool collide)
    {
        palPrismaticLink *ppl= PF->CreatePrismaticLink();
        ppl->Init(parent,child,x,y,z,axis_x,axis_y,axis_z,collide); //initialize it, set its location to 0,0,0 and minimum size to 50
        return ppl;
    }

    float link_prismatic_get_feedback(palPrismaticLink* pl)
    {
        return pl->GetFeedback()->GetValue();
    }

    void link_prismatic_set_limits(palPrismaticLink*pl,float min,float max)
    {
        pl->SetLimits(min, max);
    }
}