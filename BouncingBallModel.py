#!/usr/bin/env python

import math

objects = {}

def addObjects(objName, position, time, velocity):
    obj = {'position':position,'time':time,'velocity':velocity}
    objects[objName] = obj
    
def updateObject(obj,t):
    # set new time
    objects[obj]['time'] = t
    
    # calculate new velocity
    v = objects[obj]['velocity']
    
    #calculate new position based on velocity
    g =  9.8
    
    z = objects[obj]['position'][2] - (0.5 * 0 * math.pow(t,2))
    x = objects[obj]['position'][0] - (0.5 * 0 * math.pow(t,2))
    y = objects[obj]['position'][1] - (0.5 * g * math.pow(t,2))
    
    if y < 0:
        y =  -y
    
    objects[obj]['position'] = [x,y,z]
    
    return objects[obj]['position']
    
def getObjectPostion(obj):
    return objects[obj]['position']
    
'''        
if __name__ == '__main__':
    addObjects('sphere',[3,4,5],0,9.8)
    print objects['sphere']['position']
    print objects['sphere']['position'][0]
    print objects['sphere']['position'][1]
    print objects['sphere']['position'][2]
'''
    
    


    

