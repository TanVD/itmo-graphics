from OpenGL.GL import *

from display import DISPLAY


class Slider:
    iterations = 100
    total_num_iterations = 1000

    @staticmethod
    def length():
        return 0.5

    @staticmethod
    def height():
        return -0.9

    @staticmethod
    def paint():
        glColor3f(1.0, 1.0, 1.0)
        glLineWidth(3.0)

        Slider._paint_line()
        Slider._paint_slider()

    @staticmethod
    def update_slider_by_x(to_x):
        percent = ((to_x / DISPLAY.width) - 0.25) / 0.5
        Slider.iterations = int(percent * Slider.total_num_iterations)

    @staticmethod
    def is_in_slider(x, y):
        x, y = DISPLAY.from_display_to_app(x, y)
        top_left, top_right, bottom_right, bottom_left = Slider._slider_position()
        x_left_lim, y_top_lim = top_left
        x_right_lim, y_bot_lim = bottom_right
        return x_left_lim < x < x_right_lim and y_top_lim > y > y_bot_lim

    @staticmethod
    def _slider_position():
        percent = Slider.iterations / Slider.total_num_iterations
        width_pos = (Slider.length() * percent) - (Slider.length() / 2)

        top_left = (width_pos - 0.01, Slider.height() + 0.01)
        top_right = (width_pos + 0.01, Slider.height() + 0.01)
        bottom_right = (width_pos + 0.01, Slider.height() - 0.01)
        bottom_left = (width_pos - 0.01, Slider.height() - 0.01)

        return top_left, top_right, bottom_right, bottom_left

    @staticmethod
    def _paint_line():
        glBegin(GL_LINES)
        glVertex2f(-Slider.length() / 2, Slider.height())
        glVertex2f(Slider.length() / 2, Slider.height())
        glEnd()

    @staticmethod
    def _paint_slider():
        top_left, top_right, bottom_right, bottom_left = Slider._slider_position()

        glBegin(GL_QUADS)
        glVertex2f(*top_left)
        glVertex2f(*top_right)
        glVertex2f(*bottom_right)
        glVertex2f(*bottom_left)
        glEnd()
