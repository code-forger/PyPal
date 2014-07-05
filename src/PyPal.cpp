#include "globals.h"
/* This is the c++ -> c bindings:
 * the pal_ prefix relates to any function that uses PF excluding all the create functions
 * the create_ prefix relates to any function that creats and adds an object to the world
 * all other prefixes relate to the class that should be passed in as its first parameter
 *
 *
 *
 */

#define CASTUP(char,in) (int)char >91?(char=='b') ? reinterpret_cast<palBox*>(in):\
                        (char=='s') ? reinterpret_cast<palSphere*>(in):\
                        (char=='c') ? reinterpret_cast<palCapsule*>(in):\
                        (char=='o') ? reinterpret_cast<palCompoundBody*>(in):\
                        (char=='x') ? reinterpret_cast<palConvex*>(in):\
                        (char=='g') ? reinterpret_cast<palGenericBody*>(in):in:in
                        //(char=='B') ? dynamic_cast<palStaticBox*>(static_cast<palBodyBase*>(in)):\
                        //(char=='S') ? dynamic_cast<palStaticSphere*>(static_cast<palBodyBase*>(in)):\
                        //(char=='S') ? dynamic_cast<palStaticCapsule*>(static_cast<palBodyBase*>(in)):reinterpret_cast<palStatic*>(in)
                        //(dynamic_cast<palTerrainPlane*>(in))           ? dynamic_cast<palTerrainPlane*>(in):\
                        //(dynamic_cast<palTerrainHeightmap*>(in))       ? dynamic_cast<palTerrainHeightmap*>(in):\
                        //(dynamic_cast<palTerrainMesh*>(in))            ? dynamic_cast<palTerrainMesh*>(in):\
                        //(dynamic_cast<palOrientatedTerrainPlane*>(in)) ? dynamic_cast<palOrientatedTerrainPlane*>(in):in

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

palMaterials *PM = NULL;
palPhysics *pp = NULL;
palCollisionDetection *pcd = NULL;
int material_index;
palRayHit last_hit;
extern "C" 
{
    palPhysics* pal_init(char[])
    {
        std::cout << "PAL INTERNAL DEBUG MODE SELECTED\n";
        PF->LoadPALfromDLL("/usr/local/lib64/x86_64-linux-gnu/");
        PF->SelectEngine("Bullet");
        PM = new palMaterials();
        material_index = 0;
        pp = PF->CreatePhysics();
        if (pp == NULL) 
        {
		    printf("Failed to create the physics engine. Check to see if you spelt the engine name correctly, or that the engine DLL is in the right location\n");
		    return NULL;
        }
	    pcd = dynamic_cast<palCollisionDetection *>(pp);
        return pp;
    }

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

    void pal_cleanup(){
	    PF->Cleanup();
    }

    float pal_get_time(){
        return pp->GetTime();
    }
}
/*********************************************************
 *                                                       *
 *               the physics class functions             *
 *                                                       *
 *********************************************************/
extern "C" 
{
    void physics_init(float x, float y, float z)
    {
	    palPhysicsDesc desc;
        desc.m_vGravity[0] = x; 
        desc.m_vGravity[1] = y; 
        desc.m_vGravity[2] = z;
        pp->Init(desc);
    }

    void physics_update(float step)
    {
	    pp->Update(step);
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

    palStaticCapsule * create_static_capsule(Float x, Float y, Float z, Float radius, Float length)
    {
        palStaticCapsule *pc = dynamic_cast<palStaticCapsule*>(PF->CreateObject("palStaticCapsule"));
	    pc->Init(x, y, z, radius, length);
        return pc;
    }

    palStaticSphere * create_static_sphere(Float x, Float y, Float z, Float radius)
    {
        palStaticSphere *ps = dynamic_cast<palStaticSphere*>(PF->CreateObject("palStaticSphere"));
	    ps->Init(x, y, z, radius);
        return ps;
    }

    palTerrainPlane * create_terrain_plane(Float x, Float y, Float z, Float min_size)
    {
        palTerrainPlane *pt= PF->CreateTerrainPlane(); //create the ground
        pt->Init(x,y,z,min_size); //initialize it, set its location to 0,0,0 and minimum size to 50
	    return pt;
    }

    palTerrainHeightmap * create_terrain_heightmap(Float x, Float y, Float z, Float width, Float depth, int terrain_data_width, int terrain_data_depth, const Float *pHeightmap)
    {
        palTerrainHeightmap *pth= PF->CreateTerrainHeightmap(); //create the ground
        pth->Init(x,y,z,width,depth,terrain_data_width,terrain_data_depth,pHeightmap); //initialize it, set its location to 0,0,0 and minimum size to 50
	    return pth;
    }

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

    palDCMotor * create_dcmotor(palRevoluteLink *revolute_link, Float torque, Float EMF, Float resistance)
    {
        palDCMotor *pm= dynamic_cast<palDCMotor*>(PF->CreateObject("palDCMotor"));
        pm->Init(revolute_link,torque,EMF,resistance); //initialize it, set its location to 0,0,0 and minimum size to 50
	    return pm;
    }

    palImpulseActuator * create_impulse(palBody* pb, char pbtc, Float px, Float py, Float pz, Float ax, Float ay, Float az)
    {
        palImpulseActuator *pi= dynamic_cast<palImpulseActuator*>(PF->CreateObject("palImpulseActuator"));
        pi->Init(CASTUP(pbtc,pb),px,py,pz,ax,ay,az); //initialize it, set its location to 0,0,0 and minimum size to 50
	    return pi;
    }

    palForceActuator * create_force(palBody* pb, char pbtc, Float px, Float py, Float pz, Float ax, Float ay, Float az)
    {
        palForceActuator *pf= dynamic_cast<palForceActuator*>(PF->CreateObject("palForceActuator"));
        pf->Init(CASTUP(pbtc,pb),px,py,pz,ax,ay,az); //initialize it, set its location to 0,0,0 and minimum size to 50
	    return pf;
    }

    palFakeBuoyancy * create_fake_buoyancy(palBody* pb, char pbtc, Float density)
    {
        palFakeBuoyancy *pf= dynamic_cast<palFakeBuoyancy*>(PF->CreateObject("palFakeBuoyancy"));
        pf->Init(CASTUP(pbtc,pb),density); //initialize it, set its location to 0,0,0 and minimum size to 50
	    return pf;
    }

    palLiquidDrag * create_liqid_drag(palBody* pb, char pbtc, Float area, Float CD, Float density)
    {
        palLiquidDrag *pl= dynamic_cast<palLiquidDrag*>(PF->CreateObject("palLiquidDrag"));
        pl->Init(CASTUP(pbtc,pb),area,CD,density); //initialize it, set its location to 0,0,0 and minimum size to 50
	    return pl;
    }

    palHydrofoil * create_hydrofoil(palBody* pb, char pbtc, Float px, Float py, Float pz,
                                                            Float ax, Float ay, Float az,
                                                            Float lx, Float ly, Float lz,
                                                            Float af,
                                                            Float a, Float b, Float c,
                                                            Float density)
    {
        palHydrofoil *ph= dynamic_cast<palHydrofoil*>(PF->CreateObject("palHydrofoil"));
        ph->Init(CASTUP(pbtc,pb), px, pz, px,
                                  ax, az, ax,
                                  lx, lz, lx,
                                  af,
                                  a, b,  c,
                                  density);
	    return ph;
    }

    palPropeller * create_propeller(palBody* pb, char pbtc, Float px, Float py, Float pz,
                                                            Float ax, Float ay, Float az,
                                                            Float l)
    {
        palPropeller *ph= dynamic_cast<palPropeller*>(PF->CreateObject("palPropeller"));
        ph->Init(CASTUP(pbtc,pb), px, pz, px,
                                  ax, az, ax,
                                  l);
	    return ph;
    }

    palSpring * create_spring(palBody* pb1, char pbtc1, palBody* pb2, char pbtc2, Float rest, Float ks, Float kd)
    {
        palSpring *ps= dynamic_cast<palSpring*>(PF->CreateObject("palSpring"));
        ps->Init(CASTUP(pbtc1,pb1),CASTUP(pbtc2,pb2),rest,ks,kd); //initialize it, set its location to 0,0,0 and minimum size to 50
	    return ps;
    }
    
    palSphereGeometry * create_geometry_sphere(Float x, Float y, Float z,Float rx, Float ry, Float rz, Float radius, Float mass)
    {
        palSphereGeometry *sg= PF->CreateSphereGeometry ();
        palMatrix4x4 pos;
        mat_set_translation(&pos, x, y, z);
        mat_set_rotation(&pos, rx, ry, rz);
        sg->Init (pos, radius, mass);
        return sg;
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
        gps->Init(CASTUP(btc,b),sec,lat,lon);
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
    void body_get_position(palBody*b,char typechar,float&x,float&y,float&z)
    {
        palVector3 pos;
        (CASTUP(typechar,b))->GetPosition(pos);
        x = pos[0];
        y = pos[1];
        z = pos[2];
    }

    void body_set_position(palBody*b,char typechar,float x,float y,float z)
    {
        (CASTUP(typechar,b))->SetPosition(x,y,z);
    }

    void body_set_orientation(palBody*b,float x,float y,float z)
    {
        b->SetOrientation(x,y,z);
    }

    void body_set_material(palBody*b,palMaterialUnique * material)
    {
        b->SetMaterial(material);
    }

    int body_get_group(palBody*b)
    {
        return b->GetGroup();
    }

    void body_set_group(palBody*b, int group)
    {
        b->SetGroup(group);
    }

    Float body_get_skin_width(palBody*b)
    {
        return b->GetSkinWidth();
    }

    bool body_set_skin_width(palBody*b, Float width)
    {
        b->SetSkinWidth(width);
    }

    void body_get_primative_location(palBody*b,char typechar,float&x,float&y,float&z,float&x1,float&y1,float&z1)
    {
        palMatrix4x4 const *m = &(CASTUP(typechar,b))->m_Geometries.front()->GetLocationMatrix();//->GetBaseBody();
        palVector3 v;
        mat_get_translation(m, &v);
        x = v[0];
        y = v[1];
        z = v[2];
        mat_get_rotation((palMatrix4x4*)m,&x1,&y1,&z1);
    }

    void body_get_matrix_location(palBody*b,char typechar,float&m1, float&m2, float&m3, float&m4,
                                                          float&m5, float&m6, float&m7, float&m8,
                                                          float&m9, float&m10,float&m11,float&m12,
                                                          float&m13,float&m14,float&m15,float&m16)
    {
        palMatrix4x4 const *m = &(CASTUP(typechar,b))->GetLocationMatrix();//->GetBaseBody();
        m1 = m->_11;
        m2 = m->_12;
        m3 = m->_13;
        m4 = m->_14;
        m5 = m->_21;
        m6 = m->_22;
        m7 = m->_23;
        m8 = m->_24;
        m9 = m->_31;
        m10 = m->_32;
        m11 = m->_33;
        m12 = m->_34;
        m13 = m->_41;
        m14 = m->_42;
        m15 = m->_43;
        m16 = m->_44;
    }
}

/*********************************************************
 *                                                       *
 *               the geometry_base functions             *
 *                                                       *
 *********************************************************/
extern "C" 
{
    /*void remove_object(palFactoryObject*o){
        delete o;
        o = NULL;
    }
    void body_get_position(palBody*b,char typechar,float&x,float&y,float&z)
    {
        palVector3 pos;
        (CASTUP(typechar,b))->GetPosition(pos);
        x = pos[0];
        y = pos[1];
        z = pos[2];
    }

    void body_set_position(palBody*b,char typechar,float x,float y,float z)
    {
        (CASTUP(typechar,b))->SetPosition(x,y,z);
    }

    void body_set_orientation(palBody*b,float x,float y,float z)
    {
        b->SetOrientation(x,y,z);
    }

    void body_set_material(palBody*b,palMaterialUnique * material)
    {
        b->SetMaterial(material);
    }

    int body_get_group(palBody*b)
    {
        return b->GetGroup();
    }

    void body_set_group(palBody*b, int group)
    {
        b->SetGroup(group);
    }

    Float body_get_skin_width(palBody*b)
    {
        return b->GetSkinWidth();
    }

    bool body_set_skin_width(palBody*b, Float width)
    {
        b->SetSkinWidth(width);
    }*/

    void geometry_get_primative_location(palGeometry*b,char typechar,float&x,float&y,float&z,float&x1,float&y1,float&z1)
    {
        palMatrix4x4 const *m = &(GEOMCASTUP(typechar,b))->GetLocationMatrix();//->GetBaseBody();
        palVector3 v;
        mat_get_translation(m, &v);
        x = v[0];
        y = v[1];
        z = v[2];
        mat_get_rotation((palMatrix4x4*)m,&x1,&y1,&z1);
    }
}
/*********************************************************
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
 *               the DCMotor functions                   *
 *                                                       *
 *********************************************************/
extern "C" 
{
    void dcmotor_run(palDCMotor*a){
        a->Apply();
    }

    void dcmotor_set_voltage(palDCMotor*m,float voltage){
        m->SetVoltage(voltage);
    }
}

/*********************************************************
 *                                                       *
 *               the liquid drag functions               *
 *                                                       *
 *********************************************************/
extern "C" 
{
    void liquid_drag_run(palLiquidDrag*a){
        a->Apply();
    }
}

/*********************************************************
 *                                                       *
 *               the Impulse functions                   *
 *                                                       *
 *********************************************************/
extern "C" 
{
    void impulse_set_impulse(palImpulseActuator*i,float impulse){
        i->SetImpulse(impulse);
    }

    void impulse_run(palImpulseActuator*a){
        a->Apply();
    }
}

/*********************************************************
 *                                                       *
 *               the Force functions                     *
 *                                                       *
 *********************************************************/
extern "C" 
{
    void force_set_force(palForceActuator*f,float force){
        f->SetForce(force);
    }

    void force_run(palForceActuator*a){
        a->Apply();
    }
}

/*********************************************************
 *                                                       *
 *               the hydrofoil functions                 *
 *                                                       *
 *********************************************************/
extern "C" 
{
    void hydrofoil_set_angle(palHydrofoil*f,float angle){
        f->SetAngle(angle);
    }

    void hydrofoil_run(palHydrofoil*a){
        a->Apply();
    }
}

/*********************************************************
 *                                                       *
 *               the propeller functions                 *
 *                                                       *
 *********************************************************/
extern "C" 
{
    void propeller_set_voltage(palPropeller*f,float voltage){
        f->SetVoltage(voltage);
    }

    void propeller_run(palPropeller*a){
        a->Apply();
    }
}

/*********************************************************
 *                                                       *
 *               the FakeBuoyancy functions              *
 *                                                       *
 *********************************************************/
extern "C" 
{
    void fake_buoyancy_run(palFakeBuoyancy*a){
        a->Apply();
    }
}

/*********************************************************
 *                                                       *
 *               the Spring functions                   *
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

