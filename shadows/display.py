from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from lightning import Lightning
from program import Program
from shadow.shadow_program import ShadowProgram


class Display:
    width = 800
    height = 800

    @staticmethod
    def display(vertices):
        def display():
            glClearColor(20 / 255, 20 / 255, 20 / 255, 1)

            ShadowProgram.use()
            glViewport(0, 0, ShadowProgram.width, ShadowProgram.height)
            glBindFramebuffer(GL_FRAMEBUFFER, ShadowProgram.depth_buffer)
            glClear(GL_DEPTH_BUFFER_BIT)
            glDrawArrays(GL_TRIANGLES, 0, len(vertices))
            glBindFramebuffer(GL_FRAMEBUFFER, 0)

            Program.use()
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glViewport(0, 0, Display.width, Display.height)
            glActiveTexture(GL_TEXTURE0)
            glBindTexture(GL_TEXTURE_2D, ShadowProgram.depth_texture())
            glDrawArrays(GL_TRIANGLES, 0, len(vertices))

            glutSwapBuffers()

        return display

    @staticmethod
    def reshape(width, height):
        Program.use()
        glViewport(0, 0, width, height)
        gluPerspective(100, width / height, 0.1, 50)
        gluLookAt(*(10, 10, 10), *(0, 0, 0), *(0, 1, 0))
        Display.width = width
        Display.height = height
        return

    @staticmethod
    def idle():
        Lightning.update_angle()
        glutPostRedisplay()
