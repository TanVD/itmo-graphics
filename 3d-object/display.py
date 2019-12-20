from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from dissolve import DissolveAnimation
from lightning import Lightning


class Display:
    @staticmethod
    def display(vertices):
        def display():
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glDrawArrays(GL_TRIANGLES, 0, len(vertices))
            glutSwapBuffers()

        return display

    @staticmethod
    def reshape(width, height):
        glViewport(0, 0, width, height)
        gluPerspective(100, width / height, 0.1, 50)
        gluLookAt(*(10, 10, 10), *(0, 0, 0), *(0, 1, 0))

    @staticmethod
    def idle():
        Lightning.update_gl()
        DissolveAnimation.update_gl()
        glutPostRedisplay()
