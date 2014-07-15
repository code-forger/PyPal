#include "../globals.h"

extern "C"
{
    palRigidLink * link_rigid_create(palBody *parent,palBody *child, bool collide)
    {
        palRigidLink *prl= PF->CreateRigidLink();
        prl->Init(parent,child,collide);
        return prl;
    }

    float link_rigid_get_feedback(palRigidLink* rl)
    {
        return rl->GetFeedback()->GetValue();
    }
}