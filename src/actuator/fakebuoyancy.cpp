#include "../globals.h"

extern "C"
{
    void actuator_fake_buoyancy_apply(palFakeBuoyancy* fb)
    {
        fb->Apply();
    }

    palFakeBuoyancy* actuator_fake_buoyancy_create(palBody* pb, Float density)
    {
        palFakeBuoyancy*pfb = dynamic_cast<palFakeBuoyancy*>(PF->CreateObject("palFakeBuoyancy"));
        pfb->Init(pb,density);
        return pfb;
    }
}