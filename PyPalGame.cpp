#include <stdio.h> //for our old friend, the printf function
#include "pal/palFactory.h"
#include "pal/palCollision.h"
int run() {
	PF->LoadPALfromDLL("/usr/local/lib/"); //use this if you wish to load PAL from .dll or .so
	//otherwise, we can staticly link in an implementation by include the pal_i files
	//eg: tokamak_pal.cpp and tokamak_pal.h

	PF->SelectEngine("Bullet");		 // Here is the name of the physics engine you wish to use. You could replace DEFAULT_ENGINE with "Tokamak", "ODE", etc...
	palPhysics *pp = PF->CreatePhysics(); //create the main physics class
	if (pp == NULL) 
    {
		printf("Failed to create the physics engine. Check to see if you spelt the engine name correctly, or that the engine DLL is in the right location\n");
		return 0;
	}
	palPhysicsDesc desc;
	pp->Init(desc); //initialize it, set the main gravity vector
	palTerrainPlane *pt= PF->CreateTerrainPlane(); //create the ground
	pt->Init(0,0,0,50.0f); //initialize it, set its location to 0,0,0 and minimum size to 50
	palBox *pb = PF->CreateBox(); //create a box
	pb->Init(0,1.5f ,0, 1,1,1, 1); //initialize it, set its location to 0,1.5,0 (one and a half units up in the air), set dimensions to 1x1x1 and its mass to 1
	
    palPhysics*ppp = PF->GetActivePhysics();
	palCollisionDetection *pcd = dynamic_cast<palCollisionDetection *>(ppp);

    pcd->NotifyCollision(pb,true);
    palContact pc;
    for (int i=0;i < 26;i++) 
    { //run 25 steps of the simulation
		pp->Update(0.02f); //update the physics engine. advance the simulation time by 0.02

        pcd->GetContacts(pb,pc);
		palVector3 pos;
		pb->GetPosition(pos); //get the location of the box

		printf("Current box position is %6.5f at time %d with %d collisions\n",pos.y,i,pc.m_ContactPoints.size());
	}
	PF->Cleanup(); //we are done with the physics. clean up.
}
extern "C" { int runner(){run();}}
extern "C" 
{
    palPhysics* pal_init(char[])
    {
        PF->LoadPALfromDLL("/usr/local/lib/");
        PF->SelectEngine("Bullet");
        palPhysics *pp = PF->CreatePhysics();
        if (pp == NULL) 
        {
		    printf("Failed to create the physics engine. Check to see if you spelt the engine name correctly, or that the engine DLL is in the right location\n");
		    return NULL;
        }
        return pp;
    }
}
extern "C" 
{
    void physics_init(palPhysics* pp, float x, float y, float z)
    {
	    palPhysicsDesc desc;
        desc.m_vGravity[0] = x; 
        desc.m_vGravity[1] = y; 
        desc.m_vGravity[2] = z; 
        pp->Init(desc);
    }
}
extern "C" 
{
    void physics_update(palPhysics* pp, float step)
    {
	    pp->Update(step);
    }
}
extern "C" 
{
    palTerrainPlane * create_terrain_plane(Float x, Float y, Float z, Float min_size)
    {
        palTerrainPlane *pt= PF->CreateTerrainPlane(); //create the ground
        pt->Init(x,y,z,min_size); //initialize it, set its location to 0,0,0 and minimum size to 50
	    return pt;
    }
}
extern "C" 
{
    palBox * create_box(Float x, Float y, Float z, Float width, Float height, Float depth, Float mass)
    {
        palBox *pb = PF->CreateBox(); //create a box
	    pb->Init(x,y,z,width,height,depth,mass);
        return pb;
    }
}

extern "C" 
{
    void get_position(palBox* pb,float&x,float&y,float&z)
    {
        palVector3 pos;
        pb->GetPosition(pos);
        x = pos[0];
        y = pos[1];
        z = pos[2];
    }
}



