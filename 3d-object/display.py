from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from camera import Camera
from dissolve import DissolveAnimation


class Display:
    width = 800
    height = 800

    @staticmethod
    def display(vertices):
        def display():
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glDrawArrays(GL_TRIANGLES, 0, len(vertices))
            glutSwapBuffers()

        return display

    @staticmethod
    def reshape(width, height):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glViewport(0, 0, width, height)
        gluPerspective(100, width / height, 0.1, 50)
        gluLookAt(*(10, 10, 10), *(0, 0, 0), *Camera.get_top_direction())

    @staticmethod
    def idle():
        DissolveAnimation.animate_dissolve()
        glutPostRedisplay()
