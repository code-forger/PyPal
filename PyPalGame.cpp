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

    palBoxGeometry * create_geometry_box(Float x, Float y, Float z, Float width, Float height, Float depth, Float mass)
    {
        palBoxGeometry *bg= PF->CreateBoxGeometry ();

        palMatrix4x4 pos;
        mat_set_translation(&pos, x, y, z);
        bg->Init (pos, width, height, depth, mass);
        return bg;
    }

    palTransponderReciever* create_transponder_reciever(palBody *b)
    {
        palTransponderReciever *pts= (palTransponderReciever*)PF->CreateObject("palTransponderReciever");
        pts->Init(b); //initialize it, set its location to 0,0,0 and minimum size to 50
	    return pts;
    }

    palTransponderSender* create_transponder_sender(palBody *b, Float max_distance)
    {
        palTransponderSender *pts= (palTransponderSender*)PF->CreateObject("palTransponderSender");
        pts->Init(b,max_distance); //initialize it, set its location to 0,0,0 and minimum size to 50
	    return pts;
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

    void body_set_position(palBody*b,float x,float y,float z)
    {
        b->SetPosition(x,y,z);
    }

    void body_set_orientation(palBody*b,float x,float y,float z)
    {
        b->SetOrientation(x,y,z);
    }

    void body_set_material(palBody*b,palMaterial *material)
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

    void body_get_primative_location(palBody*b,float&x,float&y,float&z,float&x1,float&y1,float&z1)
    {
        palMatrix4x4 const *m = &b->m_Geometries.front()->GetLocationMatrix();//->GetBaseBody();
        palVector3 v;
        mat_get_translation(m, &v);
        x = v[0];
        y = v[1];
        z = v[2];
        //mat_get_rotation((palMatrix4x4*)m,&x1,&y1,&z1);TODO
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

    void box_apply_impulse(palBox*b,float ix, float iy, float iz){
        b->ApplyImpulse(ix,iy,iz);
    }

    void box_apply_impulse_at_pos(palBox*b,float x,float y,float z
                                 ,float px,float py,float pz)
    {
        b->ApplyImpulseAtPosition(x,y,z,pz,py,pz);
    }

    void box_apply_angular_impulse(palBox*b,float ix, float iy, float iz){
        b->ApplyAngularImpulse(ix,iy,iz);
    }

    void box_apply_force(palBox*b,float x,float y,float z)
    {
        b->ApplyForce(x,y,z);
    }

    void box_apply_force_at_pos(palBox*b,float x,float y,float z
                                 ,float px,float py,float pz)
    {
        b->ApplyForceAtPosition(x,y,z,pz,py,pz);
    }

    void box_apply_torque(palBox*b,float x,float y,float z)
    {
        b->ApplyTorque(x,y,z);
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

    Float box_get_angular_velocity_x(palBox*b)
    {
        palVector3 p;
        b->GetAngularVelocity(p);
        return p[0];
    }

    Float box_get_angular_velocity_y(palBox*b)
    {
        palVector3 p;
        b->GetAngularVelocity(p);
        return p[1];
    }

    Float box_get_angular_velocity_z(palBox*b)
    {
        palVector3 p;
        b->GetAngularVelocity(p);
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
    {//TODO
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

    void capsule_apply_impulse(palCapsule*c,float ix, float iy, float iz){
        c->ApplyImpulse(ix,iy,iz);
    }

    void capsule_apply_impulse_at_pos(palCapsule*c,float x,float y,float z
                                 ,float px,float py,float pz)
    {
        c->ApplyImpulseAtPosition(x,y,z,pz,py,pz);
    }

    void capsule_apply_angular_impulse(palCapsule*c,float ix, float iy, float iz){
        c->ApplyAngularImpulse(ix,iy,iz);
    }

    void capsule_set_active(palCapsule*c,bool active)
    {
        c->SetActive(active);
    }

    void capsule_apply_force(palCapsule*c,float x,float y,float z)
    {
        c->ApplyForce(x,y,z);
    }

    void capsule_apply_force_at_pos(palCapsule*c,float x,float y,float z
                                 ,float px,float py,float pz)
    {
        c->ApplyForceAtPosition(x,y,z,pz,py,pz);
    }

    void capsule_apply_torque(palCapsule*c,float x,float y,float z)
    {
        c->ApplyTorque(x,y,z);
    }

    bool capsule_is_active(palCapsule*c)
    {
        return c->IsActive();
    }

    Float capsule_get_velocity_x(palCapsule*c)
    {
        palVector3 p;
        c->GetLinearVelocity(p);
        return p[0];
    }

    Float capsule_get_velocity_y(palCapsule*c)
    {
        palVector3 p;
        c->GetLinearVelocity(p);
        return p[1];
    }

    Float capsule_get_velocity_z(palCapsule*c)
    {
        palVector3 p;
        c->GetLinearVelocity(p);
        return p[2];
    }

    Float capsule_get_angular_velocity_x(palCapsule*c)
    {
        palVector3 p;
        c->GetAngularVelocity(p);
        return p[0];
    }

    Float capsule_get_angular_velocity_y(palCapsule*c)
    {
        palVector3 p;
        c->GetAngularVelocity(p);
        return p[1];
    }

    Float capsule_get_angular_velocity_z(palCapsule*c)
    {
        palVector3 p;
        c->GetAngularVelocity(p);
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

    Float compound_get_velocity_x(palCompoundBody*c)
    {
        palVector3 p;
        c->GetLinearVelocity(p);
        return p[0];
    }

    Float compound_get_velocity_y(palCompoundBody*c)
    {
        palVector3 p;
        c->GetLinearVelocity(p);
        return p[1];
    }

    Float compound_get_velocity_z(palCompoundBody*c)
    {
        palVector3 p;
        c->GetLinearVelocity(p);
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

    void sphere_apply_impulse(palSphere*s,float ix, float iy, float iz){
        s->ApplyImpulse(ix,iy,iz);
    }

    void sphere_apply_impulse_at_pos(palSphere*s,float x,float y,float z
                                 ,float px,float py,float pz)
    {
        s->ApplyImpulseAtPosition(x,y,z,pz,py,pz);
    }

    void sphere_apply_angular_impulse(palSphere*s,float ix, float iy, float iz){
        s->ApplyAngularImpulse(ix,iy,iz);
    }

    void sphere_apply_force(palSphere*s,float x,float y,float z)
    {
        s->ApplyForce(x,y,z);
    }

    void sphere_apply_force_at_pos(palSphere*s,float x,float y,float z
                                 ,float px,float py,float pz)
    {
        s->ApplyForceAtPosition(x,y,z,pz,py,pz);
    }

    void sphere_apply_torque(palSphere*s,float x,float y,float z)
    {
        s->ApplyTorque(x,y,z);
    }

    void sphere_set_active(palSphere*s,bool active)
    {
        s->SetActive(active);
    }

    bool sphere_is_active(palSphere*s)
    {
        return s->IsActive();
    }

    Float sphere_get_velocity_x(palSphere*s)
    {
        palVector3 p;
        s->GetLinearVelocity(p);
        return p[0];
    }

    Float sphere_get_velocity_y(palSphere*s)
    {
        palVector3 p;
        s->GetLinearVelocity(p);
        return p[1];
    }

    Float sphere_get_velocity_z(palSphere*s)
    {
        palVector3 p;
        s->GetLinearVelocity(p);
        return p[2];
    }

    Float sphere_get_angular_velocity_x(palSphere*s)
    {
        palVector3 p;
        s->GetAngularVelocity(p);
        return p[0];
    }

    Float sphere_get_angular_velocity_y(palSphere*s)
    {
        palVector3 p;
        s->GetAngularVelocity(p);
        return p[1];
    }

    Float sphere_get_angular_velocity_z(palSphere*s)
    {
        palVector3 p;
        s->GetAngularVelocity(p);
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
 *               the spherical link functions            *
 *                                                       *
 *********************************************************/
extern "C" 
{
    void spherical_link_remove(palSphericalLink*sl){
        delete sl;
        sl = NULL;
    }

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
    void revolute_link_remove(palRevoluteLink*rl){
        delete rl;
        rl = NULL;
    }

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
 *               the transponder reciever functions      *
 *                                                       *
 *********************************************************
extern "C" 
{
    void transponder_reciever_remove(palTransponderReciever*tr){
        delete tr;
        tr = NULL;
    }

    int transponder_reciever_get_num_of_senders(palTransponderReciever *t)
    {
        std::cout << t->GetNumTransponders() << "\n";
        return t->GetNumTransponders();
    }

    float transponder_reciever_distance(palTransponderReciever *t,int id)
    {
        return t->GetDistance(id);
    }

}

/*********************************************************
 *                                                       *
 *               the transponder sender functions        *
 *                                                       *
 *********************************************************
extern "C" 
{
    void transponder_sender_remove(palTransponderSender*ts){
        delete ts;
        ts = NULL;
    }
}

/*********************************************************
 *                                                       *
 *               the velocimeter functions               *
 *                                                       *
 *********************************************************
extern "C" 
{
    void velocimeter_remove(palVelocimeterSensor*vs){
        delete vs;
        vs = NULL;
    }

    float velocimeter_get_velocity(palVelocimeterSensor*vs){
        return vs->GetVelocity();
    }
}*/
