from OpenGL.GL import *


class Camera:
    _speed = 0.1
    _enable_rotation = False
    _prev_x = 0
    _prev_y = 0

    @staticmethod
    def get_top_direction():
        return 0, 1, 0

    @staticmethod
    def update(x, y):
        Camera._prev_x = x
        Camera._prev_y = y

    @staticmethod
    def enable_rotation():
        Camera._enable_rotation = True

    @staticmethod
    def disable_rotation():
        Camera._enable_rotation = False

    @staticmethod
    def move_to(x, y):
        if not Camera._enable_rotation:
            return

        diff_x = x - Camera._prev_x
        diff_y = y - Camera._prev_y

        glMatrixMode(GL_MODELVIEW)

        to_the_top = Camera.get_top_direction()
        glRotate(Camera._speed * diff_x, *to_the_top)
        to_the_right = (glGetDoublev(GL_MODELVIEW_MATRIX) @ (1, 0, -1, 1))[:-1]
        glRotate(Camera._speed * diff_y, *to_the_right)

        Camera.update(x, y)
