#include "../globals.h"

extern "C"
{
    palRevoluteLink * link_revolute_create(palBody *parent,palBody *child,Float x,Float y,
                                      Float z, Float axis_x,Float axis_y, Float axis_z, bool collide)
    {
        palRevoluteLink *prl= PF->CreateRevoluteLink();
        prl->Init(parent,child,x,y,z,axis_x,axis_y,axis_z,collide); //initialize it, set its location to 0,0,0 and minimum size to 50
        return prl;
    }

    float link_revolute_get_feedback(palRevoluteLink* rl)
    {
        return rl->GetFeedback()->GetValue();
    }
    
    void link_revolute_set_limits(palRevoluteLink*rl,float max, float min)
    {
        rl->SetLimits(max,min);
    }

    void link_revolute_get_position(palRevoluteLink*rl,float* vec)
    {
        palVector3 v;
        rl->GetPosition(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    float link_revolute_get_angle(palRevoluteLink*rl){
        return rl->GetAngle();
    }

    float link_revolute_get_angular_velocity(palRevoluteLink*rl){
        return rl->GetAngularVelocity();
    }

    void link_revolute_apply_torque(palRevoluteLink*rl, Float torque){
        rl->ApplyTorque(torque);
    }

    void link_revolute_apply_angular_impulse(palRevoluteLink*rl, Float impulse){
        rl->ApplyAngularImpulse(impulse);
    }

    void link_revolute_get_axis(palRevoluteLink*rl,float* vec)
    {
        palVector3 v;
        v = rl->GetAxis();
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }
}