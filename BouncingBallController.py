#!/usr/bin/env python

import BouncingBallModel
from OpenGL.GLUT import *

pause = False

def keyEvent(key, x, y):
    #Press the space bar to pause or unpause the boucning ball
    if key == chr(32):
        BouncingBallModel.setPause(not BouncingBallModel.pause)
        
def specialKeyEvent(key,x,y):    
    #Left arrow to increase x velocity
    if key == GLUT_KEY_LEFT:
        BouncingBallModel.changeVelocity('glutSolidSphere', BouncingBallModel.objects['glutSolidSphere']['velocity'][0] + .01, 0)
    #Right arrow to decrease x velocity
    elif key == GLUT_KEY_RIGHT:
        BouncingBallModel.changeVelocity('glutSolidSphere', BouncingBallModel.objects['glutSolidSphere']['velocity'][0] - .01, 0)
    #Up arrow to increase y velocity
    elif key == GLUT_KEY_UP:
        BouncingBallModel.changeVelocity('glutSolidSphere', BouncingBallModel.objects['glutSolidSphere']['velocity'][1] + .01, 1)
    #Down arrow to decrease y velocity
    elif key == GLUT_KEY_DOWN:
        BouncingBallModel.changeVelocity('glutSolidSphere', BouncingBallModel.objects['glutSolidSphere']['velocity'][1] - .01, 1)
        