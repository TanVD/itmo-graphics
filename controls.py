from OpenGL.raw.GLUT import *

from display import *


class Controls:
    _last_btn = None
    _last_state = None
    _last_position_x = DISPLAY.center_x
    _last_position_y = DISPLAY.center_y

    @staticmethod
    def mouse(btn, state, x, y):
        if state == GLUT_UP:
            Controls._last_btn = None
        else:
            Controls._last_btn = btn

        Controls._last_position_x = x
        Controls._last_position_y = y

    @staticmethod
    def motion(x, y):
        position_x = x
        position_y = y

        if Controls._last_btn == GLUT_LEFT_BUTTON:
            DISPLAY.center_x -= (position_x - Controls._last_position_x) * DISPLAY.mouse_force
            DISPLAY.center_y += (position_y - Controls._last_position_y) * DISPLAY.mouse_force

        Controls._last_position_x = position_x
        Controls._last_position_y = position_y

        glutPostRedisplay()

    @staticmethod
    def key_up(key, x, y):
        char = key.decode("utf-8")
        print(char)
        if char == "+":
            print("Incrementing")
            DISPLAY.scale *= DISPLAY.scale_divider
            DISPLAY.mouse_force *= DISPLAY.scale_divider
        elif char == "-":
            print("Decrementing")
            DISPLAY.scale /= DISPLAY.scale_divider
            DISPLAY.mouse_force /= DISPLAY.scale_divider

        glutPostRedisplay()

