#include "../globals.h"

extern "C"
{
    palGPSSensor* sensor_gps_create(palBody* b, int sec, Float lat, Float lon)
    {
        palGPSSensor *gps= PF->CreateGPSSensor();
        gps->Init(b,sec,lat,lon);
        return gps;
    }

    void sensor_gps_get_string(palGPSSensor* gps, char * str)
    {
        gps->GetGPSString(str); //TODO
    }

    char* sensor_gps_create_string()
    {
        char* string = new char[100];
    }
}