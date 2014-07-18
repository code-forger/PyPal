#include "globals.h"

palMaterials *PM = NULL;
palPhysics *pp = NULL;
palCollisionDetection *pcd = NULL;
int material_index;
palRayHit last_hit;
extern "C" 
{
    void pal_init(char[])
    {
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
    }

    void pal_cleanup()
    {
        PF->Cleanup();
    }

    palMaterialUnique * pal_add_material(float staticfric, float kineticfric, float restitution)
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

    float physics_get_time()
    {
        return pp->GetTime();
    }

    float physics_get_last_timestep()
    {
        return pp->GetLastTimestep();
    }

    void physics_set_group_collision(palGroup a, palGroup b, bool enabled)
    {
        pp->SetGroupCollision(a, b, enabled);
    }

    void physics_get_gravity(float vec[3])
    {
        palVector3 v;
        pp->GetGravity(v);
        for (int i = 0; i < 3; i++)
            vec[i] = v._vec[i];
    }

    int physics_get_up_axis()
    {
        return pp->GetUpAxis();
    }

    void remove_object(palFactoryObject*o){
        delete o;
        o = NULL;
    }
}