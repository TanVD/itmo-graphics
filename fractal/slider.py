from OpenGL.GL import *

from display import Display


class Slider:
    iterations = 100
    total_num_iterations = 1000

    _size = 0.02

    @staticmethod
    def length():
        return 1

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
    def update_slider_by_x(to_x, to_y):
        x, y = Display.from_display_to_app(to_x, to_y)
        if x < -0.5:
            Slider.iterations = 1
        elif x > 0.5:
            Slider.iterations = Slider.total_num_iterations
        else:
            percent = x + 0.5
            Slider.iterations = int(percent * Slider.total_num_iterations)

    @staticmethod
    def is_in_slider(x, y):
        x, y = Display.from_display_to_app(x, y)
        top_left, top_right, bottom_right, bottom_left = Slider._slider_position()
        x_left_lim, y_top_lim = top_left
        x_right_lim, y_bot_lim = bottom_right
        return x_left_lim < x < x_right_lim and y_top_lim > y > y_bot_lim

    @staticmethod
    def _slider_position():
        percent = Slider.iterations / Slider.total_num_iterations
        width_pos = (Slider.length() * percent) - (Slider.length() / 2)

        top_left = (width_pos - Slider._size, Slider.height() + Slider._size)
        top_right = (width_pos + Slider._size, Slider.height() + Slider._size)
        bottom_right = (width_pos + Slider._size, Slider.height() - Slider._size)
        bottom_left = (width_pos - Slider._size, Slider.height() - Slider._size)

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
