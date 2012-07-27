#!/usr/bin/env python

import math
import BouncingBallView

objects = {}

def addObjects(objName, position, time, velocity):
    obj = {'position':position,'time':time,'velocity':velocity}
    objects[objName] = obj
    
def setScreenBoundries(l,r,b,t):
    global left,right,bottom,top
    
    left = l
    right = r
    bottom = b
    top = t
    
    print left
    print right
    print bottom
    print top
    
def updateObject(obj,t):
    global left,right,bottom,top
    
    # set new time
    objects[obj]['time'] = t
    
    v = objects[obj]['velocity']
    
    #calculate new position based on velocity
    g = 9.8
    
    z = objects[obj]['position'][2] + (0.5 * 0 * math.pow(t,2))
    x = objects[obj]['position'][0] + (0.5 * 0 * math.pow(t,2))
    y = objects[obj]['position'][1] + v[1]
    
    if x > right:
        #x = right
        v[0] = -v[0]
    elif x < left:
        #x = left
        v[0] = -v[0]
        
    if y > top:
        #y = top
        ov[1] = -v[1]
    elif y < bottom:
        #y = bottom
        v[1] = -v[1]
        
    objects[obj]['position'] = [x,y,z]
    
    return objects[obj]['position']
    
def getObjectPostion(obj):
    return objects[obj]['position']
