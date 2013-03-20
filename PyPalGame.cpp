#include <typeinfo>
#include <iostream>
#include <stdio.h> //for our old friend, the printf function
#include "pal/palFactory.h"
#include "pal/palCollision.h"
/* This is the c++ -> c bindings:
 * the pal_ prefix relates to any function that uses PF excluding all the create functions
 * the create_ prefix relates to any function that creats and adds an object to the wor;d
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
int run() {
    PF->LoadPALfromDLL("/usr/local/lib/"); //use this if you wish to load PAL from .dll or .so
    //otherwise, we can staticly link in an implementation by include the pal_i files
    //eg: tokamak_pal.cpp and tokamak_pal.h


    PF->SelectEngine("Bullet");		 // Here is the name of the physics engine you wish to use. You could replace DEFAULT_ENGINE with "Tokamak", "ODE", etc...
    palPhysics *pp = PF->CreatePhysics(); //create the main physics class
    if (pp == NULL) {
      std::cout << "Failed to create the physics engine. Check to see if you spelt the engine name correctly, or that the engine DLL is in the right location\n";
      return 0;
    }
    palPhysicsDesc desc;
    pp->Init(desc); //initialize it, set the main gravity vector
    palTerrainPlane *pt= PF->CreateTerrainPlane(); //create the ground
    pt->Init(0,0,0,50.0f); //initialize it, set its location to 0,0,0 and minimum size to 50
    pt->SetGroup(2);
    palBox *pb = PF->CreateBox(); //create a box
    pb->Init(0,1.5f ,0, 1,1,1, 1); //initialize it, set its location to 0,1.5,0 (one and a half units up in the air), set dimensions to 1x1x1 and its mass to 1
	pb->SetGroup(0);
    palBox *pb1 = PF->CreateBox(); //create a box
    pb1->Init(0,3.0f ,0, 1,1,1, 1); //initialize it, set its location to 0,1.5,0 (one and a half units up in the air), set dimensions to 1x1x1 and its mass to 1
	pb1->SetGroup(1);
    palPhysics*ppp = PF->GetActivePhysics();
    palCollisionDetection *pcd = dynamic_cast<palCollisionDetection *>(ppp);
    pcd->SetGroupCollision(0,1,true);
    pcd->SetGroupCollision(2,1,true);
    pcd->NotifyCollision(pb,true);
    pcd->NotifyCollision(pb1,true);
    palContact pc;
    float x,x1;
    int y,y1;
    for (int i=0;i < 40;i++) { //run 25 steps of the simulation
      pp->Update(0.02f); //update the physics engine. advance the simulation time by 0.02

      pcd->GetContacts(pb,pc);
      y = pc.m_ContactPoints.size();
      pcd->GetContacts(pb1,pb,pc);
      y1 = pc.m_ContactPoints.size();
      palVector3 pos;
      pb->GetPosition(pos); //get the location of the box
      x = pos.y;     
      pb1->GetPosition(pos); //get the location of the box  
      x1 = pos.y;       
      printf("position is %6.5f,%6.5f at time %d with %d,%d collisions\n",x,x1,i,y,y1);
    }
    delete pb;
    pb = NULL;
    
    for (int i=0;i < 12;i++) { //run 25 steps of the simulation
      pp->Update(0.02f); //update the physics engine. advance the simulation time by 0.02

      pcd->GetContacts(pb1,pc);
      palVector3 pos;
      pb1->GetPosition(pos); //get the location of the box

      printf("Current box position is %6.5f at time %d with %d collisions\n",pos.y,i,pc.m_ContactPoints.size());
    }
    PF->Cleanup(); //we are done with the physics. clean up.
}
extern "C"{void runner(){run();}}

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
        PF->LoadPALfromDLL("/usr/local/lib/");
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
    palTerrainPlane * create_terrain_plane(Float x, Float y, Float z, Float min_size)
    {
        palTerrainPlane *pt= PF->CreateTerrainPlane(); //create the ground
        pt->Init(x,y,z,min_size); //initialize it, set its location to 0,0,0 and minimum size to 50
	    return pt;
    }

    palBox * create_box(Float x, Float y, Float z, Float width, Float height, Float depth, Float mass)
    {
        palBox *pb = PF->CreateBox(); //create a box
	    pb->Init(x,y,z,width,height,depth,mass);
        return pb;
    }

    palSphere * create_sphere(Float x, Float y, Float z, Float radius, Float mass)
    {
        palSphere *ps = PF->CreateSphere(); //create a box
	    ps->Init(x, y, z, radius, mass);
        return ps;
    }

    palCapsule * create_capsule(Float x, Float y, Float z, Float radius, Float length, Float mass)
    {
        palCapsule *pc = PF->CreateCapsule(); //create a box
	    pc->Init(x, y, z, radius, length, mass);
        return pc;
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

    void body_set_data(palBody*b,int* data)
    {
        b->SetUserData(data);
    }

    int body_get_data(palBody*b)
    {
        return b->GetUserData();
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
        PF->Remove(b);
        delete b;
        b = NULL;
    }

    void box_get_size(palBox*b,float&width,float&height,float&depth)
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
        PF->Remove(b);
        delete b;
        b = NULL;
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
        PF->Remove(b);
        delete b;
        b = NULL;
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
        PF->Remove(b);
        delete b;
        b = NULL;
    }
}



