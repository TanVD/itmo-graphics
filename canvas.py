from OpenGL.GL import *

from display import DISPLAY


class Canvas:
    @staticmethod
    def paint():
        glBegin(GL_QUADS)

        Canvas._set_vertex(-DISPLAY.width / 2, -DISPLAY.height / 2)
        Canvas._set_vertex(-DISPLAY.width / 2, DISPLAY.height / 2)
        Canvas._set_vertex(DISPLAY.width / 2, DISPLAY.height / 2)
        Canvas._set_vertex(DISPLAY.width / 2, -DISPLAY.height / 2)

        glEnd()

    @staticmethod
    def _set_vertex(w, h):
        glTexCoord2f(w, h)
        glVertex2f(w, h)
