from OpenGL.raw.GLUT import *

from display import *
from slider import Slider


class Controls:
    _last_btn = None

    _last_position_x = Display.center_x
    _last_position_y = Display.center_y

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
            if Slider.is_in_slider(Controls._last_position_x, Controls._last_position_y):
                Slider.update_slider_by_x(position_x, position_y)
            else:
                Display.center_x -= (position_x - Controls._last_position_x) * Display.mouse_force
                Display.center_y += (position_y - Controls._last_position_y) * Display.mouse_force

        Controls._last_position_x = position_x
        Controls._last_position_y = position_y

        glutPostRedisplay()

    @staticmethod
    def key_up(key, x, y):
        char = key.decode("utf-8")
        if char == "+":
            Display.scale *= Display.scale_divider
            Display.mouse_force *= Display.scale_divider
        elif char == "-":
            Display.scale /= Display.scale_divider
            Display.mouse_force /= Display.scale_divider

        glutPostRedisplay()
