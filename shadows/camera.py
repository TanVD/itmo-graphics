import math

import glm

from display import Display
from program import Program


class Camera:
    _yaw = -90.0
    _pitch = 0.0
    _field_of_view = 50.0

    _camera_up = glm.vec3(0.0, 1.0, 0.0)

    _speed = 0.1
    _enable_rotation = False
    _prev_x = 0
    _prev_y = 0

    @staticmethod
    def update_gl():
        camera_front = -glm.normalize(glm.vec3(
            math.cos(math.radians(Camera._yaw)) * math.cos(math.radians(Camera._pitch)),
            math.sin(math.radians(Camera._pitch)),
            math.sin(math.radians(Camera._yaw)) * math.cos(math.radians(Camera._pitch))
        ))

        Program.forward_mat4("projection",
                             glm.perspective(math.radians(Camera._field_of_view), Display.width / Display.height, 0.1, 100))
        Program.forward_mat4("view",
                             glm.lookAt(camera_front, glm.vec3(), Camera._camera_up))
        Program.forward_vec3("camera_position", camera_front)

    @staticmethod
    def get_top_direction():
        return 0, 1, 0

    @staticmethod
    def scroll(force):
        Camera._field_of_view -= force
        Camera.update_gl()

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

        Camera._yaw += diff_x
        Camera._pitch += diff_y

        Camera.update_gl()

        Camera.update(x, y)
