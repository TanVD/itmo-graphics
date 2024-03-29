import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from config import Config
from lightning import Lightning
from model import Model
from program import Program
from shadow.shadow_map import ShadowMap
from shadow.shadow_program import ShadowProgram


class Display:
    _is_debug = False
    _shadow_map_size = ShadowMap.width * ShadowMap.height  # Здесь надо брать размер текстуры по хорошему
    _show_shadow_map = False

    @staticmethod
    def _check_map():
        if not Display._is_debug:
            return
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, ShadowMap.depth_texture)
        arr = np.zeros((Display._shadow_map_size, 1), dtype=np.float32)
        glGetTexImage(GL_TEXTURE_2D, 0, GL_DEPTH_COMPONENT, GL_FLOAT, arr)
        non_one = [i for i in arr if i < 0.99]
        debug = 1

    @staticmethod
    def display(vertices, normals):
        def display():
            glClearColor(20 / 255, 20 / 255, 20 / 255, 1)

            ShadowProgram.use()
            glClear(GL_DEPTH_BUFFER_BIT)

            if not Display._show_shadow_map:
                glBindFramebuffer(GL_FRAMEBUFFER, ShadowMap.depth_buffer)

            glViewport(0, 0, ShadowMap.width, ShadowMap.height)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glEnableClientState(GL_VERTEX_ARRAY)
            glBindBuffer(GL_ARRAY_BUFFER, Model.vbo)
            glVertexPointer(3, GL_FLOAT, 0, None)
            glBindBuffer(GL_ARRAY_BUFFER, 0)
            glDrawArrays(GL_TRIANGLES, 0, len(vertices))
            glDisableClientState(GL_VERTEX_ARRAY)

            if glCheckFramebufferStatus(GL_FRAMEBUFFER) != GL_FRAMEBUFFER_COMPLETE:
                exit(1)

            Display._check_map()

            ShadowProgram.disable()

            if Display._show_shadow_map:
                glutSwapBuffers()
                glutPostRedisplay()
                return

            Program.use()
            glBindFramebuffer(GL_FRAMEBUFFER, 0)
            glClearDepth(1)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            glViewport(0, 0, Config.width, Config.height)
            glActiveTexture(GL_TEXTURE0)
            glBindTexture(GL_TEXTURE_2D, ShadowMap.depth_texture)

            glEnableClientState(GL_VERTEX_ARRAY)
            glEnableClientState(GL_TEXTURE_COORD_ARRAY)
            glEnableClientState(GL_NORMAL_ARRAY)
            glBindBuffer(GL_ARRAY_BUFFER, Model.vbo)
            glVertexPointer(3, GL_FLOAT, 0, None)
            glBindBuffer(GL_ARRAY_BUFFER, Model.tbo)
            glTexCoordPointer(2, GL_FLOAT, 0, None)
            glBindBuffer(GL_ARRAY_BUFFER, Model.nbo)
            glNormalPointer(GL_FLOAT, 0, None)
            glDrawArrays(GL_TRIANGLES, 0, len(vertices))
            glBindBuffer(GL_ARRAY_BUFFER, 0)
            glDisableClientState(GL_VERTEX_ARRAY)
            glDisableClientState(GL_TEXTURE_COORD_ARRAY)
            glDisableClientState(GL_NORMAL_ARRAY)

            Program.disable()

            glutSwapBuffers()
            glutPostRedisplay()

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
        return
