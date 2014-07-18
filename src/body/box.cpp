#include "../globals.h"

extern "C"
{
    void* cast_box_body(palBox* o)
    {
        return dynamic_cast<palBody*>(o);
    }

    void* cast_box_body_base(palBox* o)
    {
        return dynamic_cast<palBodyBase*>(o);
    }

    palBox* body_box_create(Float x, Float y, Float z, Float width, Float height, Float depth, Float mass)
    {
        palBox *pb = PF->CreateBox();
        pb->Init(x,y,z,width,height,depth,mass);
        return pb;
    }
}