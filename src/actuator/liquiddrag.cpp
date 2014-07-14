#include "../globals.h"

extern "C"
{
    void actuator_liquid_drag_apply(palLiquidDrag* ld)
    {
        ld->Apply();
    }

    palLiquidDrag* actuator_liquid_drag_create_on_box(palBox* pb, Float area, Float CD, Float density)
    {
        palLiquidDrag*pld = dynamic_cast<palLiquidDrag*>(PF->CreateObject("palLiquidDrag"));
        pld->Init(pb,area,CD,density);
        return pld;
    }

    palLiquidDrag* actuator_liquid_drag_create_on_sphere(palSphere* pb, Float area, Float CD, Float density)
    {
        palLiquidDrag*pld = dynamic_cast<palLiquidDrag*>(PF->CreateObject("palLiquidDrag"));
        pld->Init(pb,area,CD,density);
        return pld;
    }

    palLiquidDrag* actuator_liquid_drag_create_on_capsule(palCapsule* pb, Float area, Float CD, Float density)
    {
        palLiquidDrag*pld = dynamic_cast<palLiquidDrag*>(PF->CreateObject("palLiquidDrag"));
        pld->Init(pb,area,CD,density);
        return pld;
    }

    palLiquidDrag* actuator_liquid_drag_create_on_compound(palCompoundBody* pb, Float area, Float CD, Float density)
    {
        palLiquidDrag*pld = dynamic_cast<palLiquidDrag*>(PF->CreateObject("palLiquidDrag"));
        pld->Init(pb,area,CD,density);
        return pld;
    }

    palLiquidDrag* actuator_liquid_drag_create_on_convex(palConvex* pb, Float area, Float CD, Float density)
    {
        palLiquidDrag*pld = dynamic_cast<palLiquidDrag*>(PF->CreateObject("palLiquidDrag"));
        pld->Init(pb,area,CD,density);
        return pld;
    }

    palLiquidDrag* actuator_liquid_drag_create_on_generic(palGenericBody* pb, Float area, Float CD, Float density)
    {
        palLiquidDrag*pld = dynamic_cast<palLiquidDrag*>(PF->CreateObject("palLiquidDrag"));
        pld->Init(pb,area,CD,density);
        return pld;
    }
}