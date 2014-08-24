#include "globals.h"

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
    else if (palStaticConvex* obj = dynamic_cast<palStaticConvex*>(in))
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