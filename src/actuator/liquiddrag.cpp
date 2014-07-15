#include "../globals.h"

extern "C"
{
    void actuator_liquid_drag_apply(palLiquidDrag* ld)
    {
        ld->Apply();
    }

    palLiquidDrag* actuator_liquid_drag_create(palBody* pb, Float area, Float CD, Float density)
    {
        palLiquidDrag*pld = dynamic_cast<palLiquidDrag*>(PF->CreateObject("palLiquidDrag"));
        pld->Init(pb,area,CD,density);
        return pld;
    }
}