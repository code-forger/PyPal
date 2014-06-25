#pragma once
#include <typeinfo>
#include <iostream>
#include <stdio.h> //for our old friend, the printf function
#include "pal/palFactory.h"
#include "pal/palCollision.h"
#include "pal/palCharacter.h"
#include <typeinfo>
#include <unistd.h>

extern palMaterials *PM;
extern palPhysics *pp;
extern palCollisionDetection *pcd;
extern int material_index;
extern palRayHit last_hit;