#include "../globals.h"

extern "C"
{
    void actuator_dcmotor_apply(palDCMotor* dcm)
    {
        dcm->Apply();
    }

    void actuator_dcmotor_set_voltage(palDCMotor* dcm,float  voltage)
    {
        dcm->SetVoltage(voltage);
    }

    palDCMotor* actuator_dcmotor_create(palRevoluteLink* prl, Float tourque, Float EMF, Float resistance)
    {
        palDCMotor*pdcm = dynamic_cast<palDCMotor*>(PF->CreateObject("palDCMotor"));
        pdcm->Init(prl,tourque, EMF, resistance);
        return pdcm;
    }
}