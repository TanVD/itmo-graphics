from OpenGL.GL import *


class DISPLAY:
    width = 800
    height = 800

    center_x = 0
    center_y = 0

    scale = 4.0

    @staticmethod
    def reshape(width, height):
        DISPLAY.width = width
        DISPLAY.height = height

        glViewport(0, 0, width, height)

        glOrtho(-width / 2, width / 2, -height / 2, height / 2, 0, width)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
