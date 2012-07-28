#!/usr/bin/env python

import BouncingBallModel

pause = False

def keyEvent(key, x, y):
    #Press the space bar to pause or unpause the boucning ball
    if key == chr(32):
        BouncingBallModel.setPause(not BouncingBallModel.pause)
    elif key == chr(62):
        BouncingBallModel.changeVelocity('glutSolidSphere', BouncingBallModel.objects['glutSolidSphere']['velocity'][0] + .01, 0)
    elif key == chr(60):
        BouncingBallModel.changeVelocity('glutSolidSphere', BouncingBallModel.objects['glutSolidSphere']['velocity'][0] - .01, 0)
    elif key == chr(58):
        BouncingBallModel.changeVelocity('glutSolidSphere', BouncingBallModel.objects['glutSolidSphere']['velocity'][1] - .01, 1)
    elif key == chr(34):
        BouncingBallModel.changeVelocity('glutSolidSphere', BouncingBallModel.objects['glutSolidSphere']['velocity'][1] + .01, 1)
    
    
def specialKeyEvent(key, x, y):
    print "special key pressed"
    if key == GLUT_KEY_PAGE_UP:
        BouncingBallModel.changeVelocity('glutSolidSphere', BouncingBallModel.objects['glutSolidSphere']['velocity'][0] + .01, 0)
    elif key == GLUT_KEY_LEFT:
        BouncingBallModel.changeVelocity('glutSolidSphere', BouncingBallModel.objects['glutSolidSphere']['velocity'][0] - .01, 0)
    elif key == GLUT_KEY_UP:
        BouncingBallModel.changeVelocity('glutSolidSphere', BouncingBallModel.objects['glutSolidSphere']['velocity'][1] - .01, 1)
    elif key == GLUT_KEY_DOWN:
        BouncingBallModel.changeVelocity('glutSolidSphere', BouncingBallModel.objects['glutSolidSphere']['velocity'][1] + .01, 1)
    