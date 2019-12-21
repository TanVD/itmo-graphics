import math

import glm

from config import Config
from program import Program
from shadow.shadow_program import ShadowProgram


class Camera:
    projection = None
    view = None
    model = None

    _yaw = -90.0
    _pitch = 0.0
    _field_of_view = 50.0

    camera_up = glm.vec3(0.0, 1.0, 0.0)
    position = None

    _speed = 0.1
    _enable_rotation = False
    _prev_x = 0
    _prev_y = 0

    @staticmethod
    def update_gl():
        Camera.model = glm.scale(glm.mat4(), glm.vec3(Config.scale, Config.scale, Config.scale))

        Camera.position = -glm.normalize(glm.vec3(
            math.cos(math.radians(Camera._yaw)) * math.cos(math.radians(Camera._pitch)),
            math.sin(math.radians(Camera._pitch)),
            math.sin(math.radians(Camera._yaw)) * math.cos(math.radians(Camera._pitch))
        ))

        Camera.projection = glm.perspective(math.radians(Camera._field_of_view), Config.width / Config.height, 0.1, 100)
        Camera.view = glm.lookAt(Camera.position, glm.vec3(), Camera.camera_up)

        Program.forward_mat4("model", Camera.model)
        Program.forward_mat4("projection", Camera.projection)
        Program.forward_mat4("view", Camera.view)
        Program.forward_vec3("camera_position", Camera.position)

        ShadowProgram.forward_mat4("model", Camera.model)
        ShadowProgram.forward_mat4("projection", Camera.projection)
        ShadowProgram.forward_mat4("view", Camera.view)
        ShadowProgram.forward_vec3("camera_position", Camera.position)

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
        Camera._pitch = glm.clamp(Camera._pitch, -89, 89)

        Camera.update_gl()

        Camera.update(x, y)
