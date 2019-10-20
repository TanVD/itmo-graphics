from OpenGL.GL import *


class Display:
    mouse_force = 0.01

    width = 800
    height = 800

    center_x = 0
    center_y = 0

    scale = 4.0
    scale_divider = 0.5

    @staticmethod
    def from_display_to_app(x, y):
        new_y = (-y + Display.height / 2) / (Display.height / 2)
        new_x = (x - Display.width / 2) / (Display.width / 2)
        return new_x, new_y

    @staticmethod
    def reshape(width, height):
        Display.width = width
        Display.height = height

        glViewport(0, 0, width, height)

        glOrtho(-1, 1, -1, 1, 0, width)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
