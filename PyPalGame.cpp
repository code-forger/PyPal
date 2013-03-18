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

/*********************************************************
 *                                                       *
 *               the pal functions                       *
 *                                                       *
 *********************************************************/
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

    palCollisionDetection* pal_get_collision()
    {
        palPhysics*ppp = PF->GetActivePhysics();
	    palCollisionDetection *pcd = dynamic_cast<palCollisionDetection *>(ppp);
        return pcd;
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
    void physics_init(palPhysics* pp, float x, float y, float z)
    {
	    palPhysicsDesc desc;
        desc.m_vGravity[0] = x; 
        desc.m_vGravity[1] = y; 
        desc.m_vGravity[2] = z; 
        pp->Init(desc);
    }

    void physics_update(palPhysics* pp, float step)
    {
	    pp->Update(step);
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
        return *(int*)b->GetUserData();
    }
}



