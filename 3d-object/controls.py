from display import *


class Controls:
    _mouse_force = 0.95
    _mouse_back_force = 1 / _mouse_force
    _glut_scroll_up = 3
    _glut_scroll_down = 4

    @staticmethod
    def mouse(btn, state, x, y):
        if state != GLUT_DOWN:
            Camera.disable_rotation()
            return

        if btn == GLUT_LEFT_BUTTON:
            Camera.enable_rotation()
            Camera.update(x, y)
            return

        Camera.disable_rotation()

        if btn == Controls._glut_scroll_up:
            glScale(Controls._mouse_back_force, Controls._mouse_back_force, Controls._mouse_back_force)
        elif btn == Controls._glut_scroll_down:
            glScale(Controls._mouse_force, Controls._mouse_force, Controls._mouse_force)

        glutPostRedisplay()

    @staticmethod
    def motion(x, y):
        Camera.move_to(x, y)
