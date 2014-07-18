#include "../../globals.h"

extern "C"
{
    void* cast_static_box_body_base(palBox* o)
    {
        return dynamic_cast<palBodyBase*>(o);
    }

    palStaticBox* body_static_box_create(Float x, Float y, Float z, Float width, Float height, Float depth)
    {
        palStaticBox *pb = dynamic_cast<palStaticBox *>(PF->CreateObject("palStaticBox"));
        pb->Init(x,y,z,width,height,depth);
        return pb;
    }
}