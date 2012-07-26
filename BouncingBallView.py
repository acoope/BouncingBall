#!/usr/bin/python

import sys
import BouncingBallModel
from OpenGL.GLUT import *
from OpenGL.GL import *

timer = 0

#  Initialize material property and light source.
def init():
   light_ambient =  [0.0, 1.0, 1.0, 0.0]
   light_diffuse =  [1.0, 1.0, 1.0, 1.0]
   light_specular =  [1.0, 1.0, 1.0, 1.0]
#  light_position is NOT default value
   light_position =  [0.25, 1.0, 1.0, 0.0]

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
   global timer
   
   glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
   #if timer < 5:
      #print BouncingBallModel.getObjectPostion('glutSolidSphere')

   #spherePos = BouncingBallModel.updateObject('glutSolidSphere',timer)
   
   #planePos = BouncingBallModel.updateObject('glClipPlane',timer)
   
   glPushMatrix()
   glutSolidSphere(0.8, 40, 40)
   glPopMatrix()
   '''   
   glPushMatrix()
   glTranslatef(spherePos[0], spherePos[1], spherePos[2])
   glutSolidSphere(0.8, 40, 40)
   glPopMatrix()
   
   
   glPushMatrix()
   DrawFloor()
   glPopMatrix()
   '''
   glFlush()
   glutPostRedisplay()
   timer =  timer + .25
   
def reshape(w, h):
   glViewport(0, 0, w, h)
   glMatrixMode (GL_PROJECTION)
   glLoadIdentity()
   if w <= h:
      glOrtho(-2.5, 2.5, -2.5*h/w, 
               2.5*h/w, -10.0, 10.0)
   else: 
      glOrtho(-2.5*w/h, 
               2.5*w/h, -2.5, 2.5, -10.0, 10.0)
   glMatrixMode(GL_MODELVIEW)
   glLoadIdentity()
   gluLookAt(0,0,-10,0,0,0,0,1,0)

   
if __name__ == '__main__':

   glutInit(sys.argv)
   glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
   glutInitWindowSize (500, 1000)
   glutCreateWindow('Bouncing Ball')
   init()
   glutReshapeFunc(reshape)
   BouncingBallModel.addObjects('glutSolidSphere', [0,0,0], 0, 1.0)
   BouncingBallModel.addObjects('glClipPlane', [0,-1,0], 0, 0.0)
   glutDisplayFunc(display)
   glutMainLoop()
