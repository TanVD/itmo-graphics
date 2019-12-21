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
    def display(vertices, normals):
        def display():
            glClearColor(20 / 255, 20 / 255, 20 / 255, 1)

            ShadowProgram.use()
            glBindFramebuffer(GL_FRAMEBUFFER, ShadowProgram.depth_buffer)
            glViewport(0, 0, ShadowProgram.width, ShadowProgram.height)

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            glDrawArrays(GL_TRIANGLES, 0, len(vertices))

            ShadowProgram.disable()

            Program.use()
            glBindFramebuffer(GL_FRAMEBUFFER, 0)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            glViewport(0, 0, Display.width, Display.height)
            glActiveTexture(GL_TEXTURE0)
            glBindTexture(GL_TEXTURE_2D, ShadowProgram.depth_texture)
            glUniform1i(glGetUniformLocation(Program.get(), "shadow_map"), 0)

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            glDrawArrays(GL_TRIANGLES, 0, len(vertices))

            Program.disable()

            glutSwapBuffers()

            # glMatrixMode(GL_PROJECTION)
            # glLoadIdentity()
            # glOrtho(-1, 1, -1, 1, -1, 1)
            # glMatrixMode(GL_MODELVIEW)
            # glLoadIdentity()
            # glActiveTexture(GL_TEXTURE0)
            # glBindTexture(GL_TEXTURE_2D, ShadowProgram.depth_texture)
            # glBegin(GL_QUADS)
            # glColor3f(1,1,1)
            # glTexCoord2f(0, 0); glVertex3f(0.5, 0.5, 0)
            # glTexCoord2f(1, 0); glVertex3f(1, 0.5, 0)
            # glTexCoord2f(1, 1); glVertex3f(1, 1, 0)
            # glTexCoord2f(0, 1); glVertex3f(0.5, 1, 0)
            # glEnd()

            # glutSwapBuffers()

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
