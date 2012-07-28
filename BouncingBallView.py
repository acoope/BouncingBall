#!/usr/bin/python

import sys
import BouncingBallModel
import BouncingBallController
from OpenGL.GLUT import *
from OpenGL.GL import *

refresh = 30
time = 0
screenWidth = 500
screenHeight = 800
radius = 0.8
left = 0.0
right = 0.0
bottom = 0.0
top = 0.0

# Initialize material property and light source.
def init():
   light_ambient = [0.0, 1.0, 1.0, 0.0]
   light_diffuse = [1.0, 1.0, 1.0, 1.0]
   light_specular = [1.0, 1.0, 1.0, 1.0]
   # light_position is NOT default value
   light_position = [0.25, 1.0, 1.0, 0.0]
   
   glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
   glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
   glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
   glLightfv(GL_LIGHT0, GL_POSITION, light_position)
   
   glEnable(GL_LIGHTING)
   glEnable(GL_LIGHT0)
   glEnable(GL_DEPTH_TEST)
   
def DrawFloor():
   glBegin(GL_QUADS)
   glVertex3f(-2.0, 0.0, 2.0)
   glVertex3f(-2.0, 0.0,-2.0)
   glVertex3f( 2.0, 0.0,-2.0)
   glVertex3f( 2.0, 0.0, 2.0)
   glEnd()
   
def display():
   global time
   
   glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
   
   glLoadIdentity()
   
   spherePos = BouncingBallModel.updateObject('glutSolidSphere',time)
   planePos = BouncingBallModel.updateObject('glClipPlane',time)
   
   #print str(spherePos) + " - " + str(time) 
   
   glPushMatrix()
   glTranslatef(spherePos[0], spherePos[1], spherePos[2])
   glutSolidSphere(radius, 40, 40)
   glPopMatrix()
   glPushMatrix()
   DrawFloor()
   glPopMatrix()
   
   '''
   glPushMatrix()
   glTranslatef(0, 5, 0)
   glutSolidSphere(0.8, 40, 40)
   glPopMatrix()
   
   glPushMatrix()
   glTranslatef(0, 4.694, 0)
   glutSolidSphere(0.8, 40, 40)
   glPopMatrix()
   
   glPushMatrix()
   glTranslatef(0, 3.469, 0)
   glutSolidSphere(0.8, 40, 40)
   glPopMatrix()
   
   glPushMatrix()
   glTranslatef(0, 0.712, 0)
   glutSolidSphere(0.8, 40, 40)
   glPopMatrix()
   '''
   
   glutSwapBuffers()
   
   glFlush()
   time = time + .25
   
def reshape(w, h):
   global left,right,bottom,top
   
   glViewport(0, 0, w, h)
   glMatrixMode (GL_PROJECTION)
   glLoadIdentity()
   
   if w <= h:
      left = -2.5
      right = 2.5
      bottom = -2.5 * h/w
      top = 2.5 * h/w
   else:
      left = 2.5 * w/h
      right = 2.5 * w/h
      bottom = -2.5 
      top = 2.5
      
   glOrtho(left,right,bottom,top, -1.0, 1.0)
   
   BouncingBallModel.setScreenBoundries(left + radius, right - radius, bottom + radius, top - radius)   
   glMatrixMode(GL_MODELVIEW)
   glLoadIdentity()
   
def Timer(value):
   glutPostRedisplay()
   glutTimerFunc(refresh, Timer, 0)
   
if __name__ == '__main__':
   
   glutInit(sys.argv)
   glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
   glutInitWindowSize (screenWidth, screenHeight)
   glutCreateWindow('Bouncing Ball')
   init()
   glutReshapeFunc(reshape)
   glutDisplayFunc(display)
   BouncingBallModel.addObjects('glutSolidSphere', [0,5,0], 0, [0.0,0.1,0])
   BouncingBallModel.addObjects('glClipPlane', [0,-1,0], 0, [0,0,0])
   glutTimerFunc(0, Timer, 0)
   glutKeyboardFunc(BouncingBallController.keyEvent)
   glutMainLoop()
   