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


extern "C"
{
    int run() {
        #ifndef PAL_STATIC
        std::cout << "this shit again";
        PF->LoadPhysicsEngines("/home/m/Python/PyPalGame/");
        //use this if you wish to load PAL from .dll or .so
        //otherwise, we can staticly link in an implementation by include the pal_i files
        //eg: tokamak_pal.cpp and tokamak_pal.h
        #endif
        std::cout << PF->SelectEngine("bullet");

        palPhysics *pp = PF->CreatePhysics(); //create the main physics class
        if (pp == NULL) {
            printf("Failed to create the physics engine. Check to see if you spelt the engine name correctly, or that the engine DLL is in the right location\n");
            return 0;
        }
        palPhysicsDesc desc;
        pp->Init(desc); //initialize it, set the main gravity vector
        palTerrainPlane *pt= PF->CreateTerrainPlane(); //create the ground
        pt->Init(0,0,0,50.0f); //initialize it, set its location to 0,0,0 and minimum size to 50
        palBox *pb = PF->CreateBox(); //create a box
        pb->Init(0,1.5f ,0, 1,1,1, 1); //initialize it, set its location to 0,1.5,0 (one and a half units up in the air), set dimensions to 1x1x1 and its mass to 1
        palVector3 pos;
        pb->GetPosition(pos); //get the location of the box
        printf("Current box position is %6.5f at time %4.2f\n",pos.y,pp->GetTime());
        for (int i=0;i<25;i++) { //run 25 steps of the simulation
            pp->Update(0.02f); //update the physics engine. advance the simulation time by 0.02
            pb->GetPosition(pos); //get the location of the box
            printf("Current box position is %6.5f at time %4.2f\n",pos.y,pp->GetTime());
        }
        PF->Cleanup(); //we are done with the physics. clean up.
    } 
}


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
        PF->LoadPALfromDLL("/home/m/Python/PyPalGame/");
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
        std::cout << "notify" << enable;
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
        return c->m_ContactPoints[pos].m_pBody1;
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
        std::cout << "run\n";
        palDCMotor *pm= dynamic_cast<palDCMotor*>(PF->CreateObject("palDCMotor"));
        pm->Init(revolute_link,torque,EMF,resistance); //initialize it, set its location to 0,0,0 and minimum size to 50
	    return pm;
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
        return *((int*)b->GetUserData());
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
        std::cout << "fire\n";
    }

    void box_set_active(palBox*b,bool active)
    {
        b->SetActive(active);
    }

    bool box_is_active(palBox*b)
    {
        return b->IsActive();
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

    void cpasule_set_position(palSphere*b,float x,float y,float z)
    {
        b->SetPosition(x,y,z);
    }
}

/*********************************************************
 *                                                       *
 *               the Sphere functions                    *
 *                                                       *
 *********************************************************/
extern "C" 
{
    void sphere_remove(palSphere*b){
        delete b;
        b = NULL;
    }

    void sphere_set_position(palSphere*b,float x,float y,float z)
    {
        b->SetPosition(x,y,z);
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

