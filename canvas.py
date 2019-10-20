from OpenGL.GL import *


class Canvas:
    @staticmethod
    def paint():
        glBegin(GL_QUADS)

        Canvas._set_vertex(-1, -1)
        Canvas._set_vertex(-1, 1)
        Canvas._set_vertex(1, 1)
        Canvas._set_vertex(1, -1)

        glEnd()

    @staticmethod
    def _set_vertex(w, h):
        glTexCoord2f(w, h)
        glVertex2f(w, h)
