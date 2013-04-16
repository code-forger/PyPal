#include <typeinfo>
#include <iostream>
#include <stdio.h> //for our old friend, the printf function
#include "pal/palFactory.h"
#include "pal/palCollision.h"
/* This is the c++ -> c bindings:
 * the pal_ prefix relates to any function that uses PF excluding all the create functions
 * the create_ prefix relates to any function that creats and adds an object to the world
 * all other prefixes relate to the class that should be passed in as its first parameter
 *
 *
 *
 *
 *
 *
 *
 *
 */

/*********************************************************
 *                                                       *
 *               the pal functions                       *
 *                                                       *
 *********************************************************/

palPhysics *pp = NULL;
palCollisionDetection *pcd = NULL;
extern "C" 
{
    palPhysics* pal_init(char[])
    {
        PF->LoadPALfromDLL("/home/m/Python/PyPalGame/libs/");
        PF->SelectEngine("Bullet");
        pp = PF->CreatePhysics();
        if (pp == NULL) 
        {
		    printf("Failed to create the physics engine. Check to see if you spelt the engine name correctly, or that the engine DLL is in the right location\n");
		    return NULL;
        }
	    pcd = dynamic_cast<palCollisionDetection *>(pp);
        return pp;
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

    palBodyBase* contacts_get_body_one(palContact*c,int pos)
    {
        palBodyBase* p = c->m_ContactPoints[pos].m_pBody1;
        return p;
    }

    palBodyBase* contacts_get_body_two(palContact*c,int pos)
    {
        return c->m_ContactPoints[pos].m_pBody2;
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
    palBox * create_box(Float x, Float y, Float z, Float width, Float height, Float depth, Float mass)
    {
        palBox *pb = PF->CreateBox(); //create a box
	    pb->Init(x,y,z,width,height,depth,mass);
        return pb;
    }

    palStaticBox * create_static_box(Float x, Float y, Float z, Float width, Float height, Float depth)
    {
        palStaticBox *pb = dynamic_cast<palStaticBox *>(PF->CreateObject("palStaticBox")); //create a box
	    pb->Init(x,y,z,width,height,depth);
        return pb;
    }

    palCapsule * create_capsule(Float x, Float y, Float z, Float radius, Float length, Float mass)
    {
        palCapsule *pc = PF->CreateCapsule(); //create a box
	    pc->Init(x, y, z, radius, length, mass);
        return pc;
    }

    palCompoundBody * create_compound(Float x, Float y, Float z)
    {
        palCompoundBody *pcb = PF->CreateCompoundBody(); //create a box
	    pcb->Init(x, y, z);
        return pcb;
    }

    palSphere * create_sphere(Float x, Float y, Float z, Float radius, Float mass)
    {
        palSphere *ps = PF->CreateSphere(); //create a box
	    ps->Init(x, y, z, radius, mass);
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

    palDCMotor * create_dcmotor(palRevoluteLink *revolute_link, Float torque, Float EMF, Float resistance)
    {
        palDCMotor *pm= dynamic_cast<palDCMotor*>(PF->CreateObject("palDCMotor"));
        pm->Init(revolute_link,torque,EMF,resistance); //initialize it, set its location to 0,0,0 and minimum size to 50
	    return pm;
    }

    palBoxGeometry * create_geometry_box(Float x, Float y, Float z, Float width, Float height, Float depth, Float mass)
    {
        palBoxGeometry *bg= PF->CreateBoxGeometry ();

        palMatrix4x4 pos;
        mat_set_translation(&pos, x, y, z);
        bg->Init (pos, width, height, depth, mass);
        return bg;
    }

    palVelocimeterSensor * create_velocimeter(palBody *b, Float x, Float y, Float z)
    {
        palVelocimeterSensor *pvs= PF->CreateVelocimeterSensor();
        pvs->Init(b,x,y,z); //initialize it, set its location to 0,0,0 and minimum size to 50
	    return pvs;
    }
}
/*********************************************************
 *                                                       *
 *               the body_base_ functions                *
 *                                                       *
 *********************************************************/
extern "C" 
{
    void body_get_position(palBody*b,float&x,float&y,float&z)
    {
        palVector3 pos;
        b->GetPosition(pos);
        x = pos[0];
        y = pos[1];
        z = pos[2];
    }

    void body_set_material(palBody*b,palMaterial *material)
    {
        b->SetMaterial(material);
    }

    int body_get_group(palBody*b)
    {
        return b->GetGroup();
    }

    void body_set_group(palBody*b,int group)
    {
        b->SetGroup(group);
    }

    void body_set_data(palBody*b,int data)
    {
        int* i = new int;
        *i = data;
        b->SetUserData(i);
    }

    int body_get_data(palBody*b)
    {
        int i = *((int*)b->GetUserData());
        return i;
    }

    int body_base_get_data(palBodyBase*b)
    {
        int i = *((int*)b->GetUserData());
        return i;
    }

    int body_clear_data(palBody*b)
    {
        int*i = (int*)b->GetUserData();
        delete i;
    }

    void body_get_primative_location(palBody*b,float&x,float&y,float&z,float&x1,float&y1,float&z1)
    {
        palMatrix4x4 const *m = &b->m_Geometries.front()->GetLocationMatrix();//->GetBaseBody();
        palVector3 v;
        mat_get_translation(m, &v);
        x = v[0];
        y = v[1];
        z = v[2];
        //mat_get_rotation((palMatrix4x4*)m,&x1,&y1,&z1);
    }
}

/*********************************************************
 *                                                       *
 *               the box functions                       *
 *                                                       *
 *********************************************************/
extern "C" 
{
    void box_remove(palBox*b){
        delete b;
        b = NULL;
    }

    void box_get_size(palBox*b,float&width,float&height,float&depth)
    {
        width = b->GetWidth();
        height = b->GetHeight();
        depth = b->GetDepth();
    }

    void box_set_position(palBox*b,float x,float y,float z)
    {
        b->SetPosition(x,y,z);
    }

    void box_apply_impulse(palBox*b,float ix, float iy, float iz){
        b->ApplyImpulse(ix,iy,iz);
    }

    void box_set_active(palBox*b,bool active)
    {
        b->SetActive(active);
    }

    bool box_is_active(palBox*b)
    {
        return b->IsActive();
    }

    Float box_get_velocity_x(palBox*b)
    {
        palVector3 p;
        b->GetLinearVelocity(p);
        return p[0];
    }

    Float box_get_velocity_y(palBox*b)
    {
        palVector3 p;
        b->GetLinearVelocity(p);
        return p[1];
    }

    Float box_get_velocity_z(palBox*b)
    {
        palVector3 p;
        b->GetLinearVelocity(p);
        return p[2];
    }
}

/*********************************************************
 *                                                       *
 *               the static box functions                *
 *                                                       *
 *********************************************************/
extern "C" 
{
    void static_box_remove(palStaticBox*b){
        delete b;
        b = NULL;
    }

    void static_box_get_size(palStaticBox*b,float&width,float&height,float&depth)
    {
        width = b->GetWidth();
        height = b->GetHeight();
        depth = b->GetDepth();
    }
}

/*********************************************************
 *                                                       *
 *               the Capsule functions                   *
 *                                                       *
 *********************************************************/
extern "C" 
{
    void capsule_remove(palCapsule*b){
        delete b;
        b = NULL;
    }

    void capsule_set_position(palSphere*b,float x,float y,float z)
    {
        b->SetPosition(x,y,z);
    }

    void capsule_apply_impulse(palCapsule*c,float ix, float iy, float iz){
        c->ApplyImpulse(ix,iy,iz);
    }

    void capsule_set_active(palCapsule*c,bool active)
    {
        c->SetActive(active);
    }

    bool capsule_is_active(palCapsule*c)
    {
        return c->IsActive();
    }

    Float capsule_get_velocity_x(palBox*b)
    {
        palVector3 p;
        b->GetLinearVelocity(p);
        return p[0];
    }

    Float capsule_get_velocity_y(palBox*b)
    {
        palVector3 p;
        b->GetLinearVelocity(p);
        return p[1];
    }

    Float capsule_get_velocity_z(palBox*b)
    {
        palVector3 p;
        b->GetLinearVelocity(p);
        return p[2];
    }
}

/*********************************************************
 *                                                       *
 *               the compound functions                  *
 *                                                       *
 *********************************************************/
extern "C" 
{
    void compound_remove(palCompoundBody*s)
    {
        delete s;
        s = NULL;
    }

    void compound_set_position(palCompoundBody*s,float x,float y,float z)
    {
        s->SetPosition(x,y,z);
    }

    void compound_apply_impulse(palCompoundBody*s,float ix, float iy, float iz)
    {
        s->ApplyImpulse(ix,iy,iz);
    }

    void compound_set_active(palCompoundBody*s,bool active)
    {
        s->SetActive(active);
    }

    bool compound_is_active(palCompoundBody*s)
    {
        return s->IsActive();
    }

    void compound_add_box(palCompoundBody*c, Float x, Float y, Float z, Float width, Float height, Float depth, Float mass)
    {
        palBoxGeometry*pbg = c->AddBox();

        palMatrix4x4 pos;
        mat_set_translation(&pos, x, y, z);
        mat_set_rotation(&pos, 0,0,0);
        pbg->Init (pos, width, height, depth, mass);
    }
    
    void compound_add_sphere(palCompoundBody*c, Float x, Float y, Float z, Float radius, Float mass)
    {
        palSphereGeometry*psg = c->AddSphere();

        palMatrix4x4 pos;
        mat_set_translation(&pos, x, y, z);
        mat_set_rotation(&pos, 0,0,0);
        psg->Init (pos, radius, mass);
    }
    
    void compound_add_capsule(palCompoundBody*c, Float x, Float y, Float z, Float radius, Float height, Float mass)
    {
        palCapsuleGeometry*pcg = c->AddCapsule();

        palMatrix4x4 pos;
        mat_set_translation(&pos, x, y, z);
        mat_set_rotation(&pos, 0,0,0);
        pcg->Init (pos, radius, height, mass);
    }

    void compound_finalize(palCompoundBody*c)
    {
        c->Finalize();
    }

    Float compound_get_velocity_x(palBox*b)
    {
        palVector3 p;
        b->GetLinearVelocity(p);
        return p[0];
    }

    Float compound_get_velocity_y(palBox*b)
    {
        palVector3 p;
        b->GetLinearVelocity(p);
        return p[1];
    }

    Float compound_get_velocity_z(palBox*b)
    {
        palVector3 p;
        b->GetLinearVelocity(p);
        return p[2];
    }
}

/*********************************************************
 *                                                       *
 *               the Sphere functions                    *
 *                                                       *
 *********************************************************/
extern "C" 
{
    void sphere_remove(palSphere*s){
        delete s;
        s = NULL;
    }

    void sphere_set_position(palSphere*s,float x,float y,float z)
    {
        s->SetPosition(x,y,z);
    }

    void sphere_apply_impulse(palSphere*s,float ix, float iy, float iz){
        s->ApplyImpulse(ix,iy,iz);
    }

    void sphere_set_active(palSphere*s,bool active)
    {
        s->SetActive(active);
    }

    bool sphere_is_active(palSphere*s)
    {
        return s->IsActive();
    }

    Float sphere_get_velocity_x(palBox*b)
    {
        palVector3 p;
        b->GetLinearVelocity(p);
        return p[0];
    }

    Float sphere_get_velocity_y(palBox*b)
    {
        palVector3 p;
        b->GetLinearVelocity(p);
        return p[1];
    }

    Float sphere_get_velocity_z(palBox*b)
    {
        palVector3 p;
        b->GetLinearVelocity(p);
        return p[2];
    }
}

/*********************************************************
 *                                                       *
 *               the terrain functions                   *
 *                                                       *
 *********************************************************/
extern "C" 
{
    void terrain_remove(palTerrainPlane*b){
        delete b;
        b = NULL;
    }
}

/*********************************************************
 *                                                       *
 *               the terrain heightmap functions         *
 *                                                       *
 *********************************************************/
extern "C" 
{
    void terrain_heightmap_remove(palTerrainHeightmap*b){
        delete b;
        b = NULL;
    }
}

/*********************************************************
 *                                                       *
 *               the prismatic link functions            *
 *                                                       *
 *********************************************************/
extern "C" 
{
    void prismatic_link_remove(palPrismaticLink*pl){
        delete pl;
        pl = NULL;
    }

    void prismatic_link_set_limits(palPrismaticLink*pl,float min,float max){
        pl->SetLimits(min, max);
    }
}

/*********************************************************
 *                                                       *
 *               the revolute link functions             *
 *                                                       *
 *********************************************************/
extern "C" 
{
    void revolute_link_remove(palRevoluteLink*rl){
        delete rl;
        rl = NULL;
    }

    float revolute_link_get_angle(palRevoluteLink*rl){
        return rl->GetAngle();
    }

    void revolute_set_limits(palRevoluteLink*rl,float max, float min){
        rl->SetLimits(max,min);
    }
}

/*********************************************************
 *                                                       *
 *               the rigid link functions                *
 *                                                       *
 *********************************************************/
extern "C" 
{
    void rigid_link_remove(palRigidLink*pl){
        delete pl;
        pl = NULL;
    }
}

/*********************************************************
 *                                                       *
 *               the DCMotor functions                   *
 *                                                       *
 *********************************************************/
extern "C" 
{
    void dcmotor_remove(palDCMotor*m){
        delete m;
        m = NULL;
    }

    void dcmotor_run(palDCMotor*a){
        a->Apply();
    }

    void dcmotor_set_voltage(palDCMotor*m,float voltage){
        m->SetVoltage(voltage);
    }
}

/*********************************************************
 *                                                       *
 *               the velocimeter functions               *
 *                                                       *
 *********************************************************/
extern "C" 
{
    void velocimeter_remove(palVelocimeterSensor*vs){
        delete vs;
        vs = NULL;
    }

    float velocimeter_get_velocity(palVelocimeterSensor*vs){
        return vs->GetVelocity();
    }
}
