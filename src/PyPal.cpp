#include "globals.h"
/* This is the c++ -> c bindings:
 * the pal_ prefix relates to any function that uses PF excluding all the create functions
 * the create_ prefix relates to any function that creats and adds an object to the world
 * all other prefixes relate to the class that should be passed in as its first parameter
 *
 *
 *
 */

#define GEOMCASTUP(char,in) (char=='b') ? reinterpret_cast<palBoxGeometry*>(in):\
                            (char=='s') ? reinterpret_cast<palSphereGeometry*>(in):\
                            (char=='c') ? reinterpret_cast<palCapsuleGeometry*>(in):\
                            (char=='x') ? reinterpret_cast<palConvexGeometry*>(in):in

void* castup_bodybase(palBodyBase* in)
{
    if (palBox* obj = dynamic_cast<palBox*>(in))
    {
        return obj;
    }
    else if (palSphere* obj = dynamic_cast<palSphere*>(in))
    {
        return obj;
    }
    else if (palCapsule* obj = dynamic_cast<palCapsule*>(in))
    {
        return obj;
    }
    else if (palCompoundBody* obj = dynamic_cast<palCompoundBody*>(in))
    {
        return obj;
    }
    else if (palConvex* obj = dynamic_cast<palConvex*>(in))
    {
        return obj;
    }
    else if (palGenericBody* obj = dynamic_cast<palGenericBody*>(in))
    {
        return obj;
    }
    else if (palTerrainPlane* obj = dynamic_cast<palTerrainPlane*>(in))
    {
        return obj;
    }
    else if (palTerrainHeightmap* obj = dynamic_cast<palTerrainHeightmap*>(in))
    {
        return obj;
    }
    else if (palTerrainMesh* obj = dynamic_cast<palTerrainMesh*>(in))
    {
        return obj;
    }
    else if (palOrientatedTerrainPlane* obj = dynamic_cast<palOrientatedTerrainPlane*>(in))
    {
        return obj;
    }
    return in;
}

/*********************************************************
 *                                                       *
 *               the pal functions                       *
 *                                                       *
 *********************************************************/
extern "C"
{
    bool pal_ray_hit(Float x, Float y, Float z, Float dx, Float dy, Float dz, Float range)
    {
        last_hit.m_pBody = 0;
        pcd->RayCast( x, y, z,dx, dy, dz, range, last_hit);
        if (last_hit.m_pBody)
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    void* get_last_hit_body()
    {
        if (last_hit.m_pBody)
            return last_hit.m_pBody;
        else
            return NULL;
    }

    void get_last_hit_location(float &x, float &y, float &z)
    {
        if (last_hit.m_pBody)
        {
            palVector3 vec = last_hit.m_vHitPosition;
            x = vec[0];
            y = vec[1];
            z = vec[2];
        }
    }
}
/*********************************************************
 *                                                       *
 *               the material functions                  *
 *                                                       *
 *********************************************************/
extern "C" 
{
    palMaterialUnique * add_material(float staticfric, float kineticfric, float restitution)
    {
        char str[8];
	    palMaterialDesc desc;
        desc.m_fStatic = staticfric;
        desc.m_fKinetic = kineticfric;
        desc.m_fRestitution = restitution;

        str[0] = (char)material_index%10;
        str[1] = (char)(material_index/10)%10;
        str[2] = (char)(material_index/100)%10;
        str[3] = (char)(material_index/1000)%10;
        str[4] = (char)(material_index/10000)%10;
        str[5] = (char)(material_index/100000)%10;
        str[6] = (char)(material_index/1000000)%10;
        str[7] = '\0';
        material_index++;
        return PM->NewMaterial(std::string(str),desc);
    }
}
/*********************************************************
 *                                                       *
 *               the collision class functions           *
 *                                                       *
 *********************************************************/
extern "C"
{
    void collision_notify(palBox*b,bool enable)
    {   
        palBodyBase *body = dynamic_cast<palBodyBase*>(b);
        pcd->NotifyCollision(body,true);
    }

    palContact* get_contacts(palBody*b)
    {
        palContact* pc = new palContact;
        pcd->GetContacts(b,*pc);
        return pc;
    }

    int contacts_get_size(palContact*c)
    {
        return c->m_ContactPoints.size();
    }

    void* contacts_get_body_one(palContact*c,int pos)
    {
        return castup_bodybase(c->m_ContactPoints[pos].m_pBody1);
    }

    void* contacts_get_body_two(palContact*c,int pos)
    {
        return castup_bodybase(c->m_ContactPoints[pos].m_pBody2);
    }

    float contacts_get_distance(palContact*c,int pos)
    {
        return c->m_ContactPoints[pos].m_fDistance;
    }

    void remove_contact(palContact *p)
    {
        delete p;
    }
}
/*********************************************************
 *                                                       *
 *               the create functions                    *
 *                                                       *
 *********************************************************/
extern "C" 
{

    palPrismaticLink * create_prismatic(palBody *parent,palBody *child,Float x,Float y,
                                      Float z, Float axis_x,Float axis_y, Float axis_z, bool collide)
    {
        palPrismaticLink *ppl= PF->CreatePrismaticLink();
        ppl->Init(parent,child,x,y,z,axis_x,axis_y,axis_z,collide); //initialize it, set its location to 0,0,0 and minimum size to 50
	    return ppl;
    }

    palRevoluteLink * create_revolute(palBody *parent,palBody *child,Float x,Float y,
                                      Float z, Float axis_x,Float axis_y, Float axis_z, bool collide)
    {
        palRevoluteLink *prl= PF->CreateRevoluteLink();
        prl->Init(parent,child,x,y,z,axis_x,axis_y,axis_z,collide); //initialize it, set its location to 0,0,0 and minimum size to 50
	    return prl;
    }

    palRigidLink * create_rigid(palBody *parent,palBody *child, bool collide)
    {
        palRigidLink *prl= PF->CreateRigidLink();
        prl->Init(parent,child,collide); //initialize it, set its location to 0,0,0 and minimum size to 50
	    return prl;
    }

    palSphericalLink * create_spherical(palBody *parent,palBody *child,Float x,Float y,
                                      Float z, bool collide)
    {
        palSphericalLink *prl= PF->CreateSphericalLink();
        prl->Init(parent,child,x,y,z,collide); //initialize it, set its location to 0,0,0 and minimum size to 50
	    return prl;
    }

    palSpring * create_spring(palBody* pb1, char pbtc1, palBody* pb2, char pbtc2, Float rest, Float ks, Float kd)
    {
        palSpring *ps= dynamic_cast<palSpring*>(PF->CreateObject("palSpring"));
        //ps->Init(CASTUP(pbtc1,pb1),CASTUP(pbtc2,pb2),rest,ks,kd); //initialize it, set its location to 0,0,0 and minimum size to 50
	    return ps;
    }

    palConvexGeometry* create_geometry_convex(Float x, Float y, Float z,Float rx, Float ry, Float rz, const Float *pVertices, int nVertices, const int *pIndices, int nIndices, Float mass)
    {
        palConvexGeometry *pcg= dynamic_cast<palConvexGeometry*>(PF->CreateObject("palConvexGeometry"));
        palMatrix4x4 pos;
        mat_set_translation(&pos, x, y, z);
        mat_set_rotation(&pos, rx, ry, rz);
        pcg->Init(pos, pVertices, nVertices, pIndices, nIndices, mass);
        return pcg;
    }

    palCompassSensor* create_compass(palBody*b, Float x, Float y, Float z)
    {
        palCompassSensor *c= PF->CreateCompassSensor();
        c->Init(b,x,y,z);
        return c;
    }

    palGPSSensor* create_gps(palBody*b,char btc, int sec, Float lat, Float lon)
    {
        palGPSSensor *gps= PF->CreateGPSSensor();
        //gps->Init(CASTUP(btc,b),sec,lat,lon);
        return gps;
    }

    palInclinometerSensor* create_inclinometer(palBody*b, Float ax, Float ay, Float az
                                                   , Float ux, Float uy, Float uz
                                                   , Float gx, Float gy, Float gz)
    {
        palInclinometerSensor *i= PF->CreateInclinometerSensor();
        i->Init(b,ax,ay,az,ux,uy,uz,gx,gy,gz);
        return i;
    }

    palPSDSensor* create_psd(palBody*b, Float x, Float y, Float z
                                      , Float ax, Float ay, Float az
                                      , Float range)
    {
        palPSDSensor *p= PF->CreatePSDSensor();
        p->Init(b,x,y,z,ax,ay,az,range);
        return p;
    }

}
/*********************************************************
 *                                                       *
 *               the body_base_ functions                *
 *                                                       *
 *********************************************************/
extern "C" 
{
    void remove_object(palFactoryObject*o){
        delete o;
        o = NULL;
    }
}
/*****************************************
 *                                                       *
 *               the prismatic link functions            *
 *                                                       *
 *********************************************************/
extern "C" 
{
    void prismatic_link_set_limits(palPrismaticLink*pl,float min,float max){
        pl->SetLimits(min, max);
    }
}

/*********************************************************
 *                                                       *
 *               the spherical link functions            *
 *                                                       *
 *********************************************************/
extern "C" 
{
    void spherical_link_set_limits(palSphericalLink*sl,float cone,float twist){
        sl->SetLimits(cone, twist);
    }
}

/*********************************************************
 *                                                       *
 *               the revolute link functions             *
 *                                                       *
 *********************************************************/
extern "C" 
{
    void revolute_link_set_limits(palRevoluteLink*rl,float max, float min){
        rl->SetLimits(max,min);
    }

    void revolute_link_get_position(palRevoluteLink*rl,float&x,float&y,float&z)
    {
        palVector3 pos;
        rl->GetPosition(pos);
        x = pos[0];
        y = pos[1];
        z = pos[2];
    }

    float revolute_link_get_angle(palRevoluteLink*rl){
        return rl->GetAngle();
    }

    float revolute_link_get_angular_velocity(palRevoluteLink*rl){
        return rl->GetAngularVelocity();
    }

    void revolute_link_apply_torque(palRevoluteLink*rl, Float torque){
        rl->ApplyTorque(torque);
    }

    void revolute_link_apply_angular_impulse(palRevoluteLink*rl, Float impulse){
        rl->ApplyAngularImpulse(impulse);
    }

    void revolute_link_get_axis(palRevoluteLink*rl,float&x,float&y,float&z)
    {
        palVector3 pos;
        pos = rl->GetAxis();
        x = pos[0];
        y = pos[1];
        z = pos[2];
    }
}
/*********************************************************
 *                                                       *
 *               the Spring functions                    *
 *                                                       *
 *********************************************************/
extern "C" 
{
    void spring_run(palSpring*a){
        a->Apply();
    }
}

/*********************************************************
 *                                                       *
 *               the compass functions                   *
 *                                                       *
 *********************************************************/
extern "C" 
{
    Float compass_get_angle(palCompassSensor* c)
    {
        return c->GetAngle();
    }
}

/*********************************************************
 *                                                       *
 *               the gps functions                       *
 *                                                       *
 *********************************************************/
extern "C" 
{
    void gps_get_string(palGPSSensor* gps, char * str)
    {
        gps->GetGPSString(str); //TODO
    }

    char* gps_create_string()
    {
        char* string = new char[100];
    }
}

/*********************************************************
 *                                                       *
 *               the inclinometer functions              *
 *                                                       *
 *********************************************************/
extern "C" 
{
    Float inclinometer_get_angle(palInclinometerSensor* i)
    {
        return i->GetAngle();
    }
}

/*********************************************************
 *                                                       *
 *               the PSD functions                       *
 *                                                       *
 *********************************************************/
extern "C" 
{
    Float psd_get_distance(palPSDSensor* p)
    {
        return p->GetDistance();
    }
}

