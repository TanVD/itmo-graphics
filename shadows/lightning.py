import math
import time

import glm

from config import Config
from program import Program
from shadow.shadow_program import ShadowProgram


class Lightning:
    _light_angle = 0

    @staticmethod
    def _light_pos():
        return math.cos(math.radians(Lightning._light_angle)), 1, math.sin(math.radians(Lightning._light_angle))

    @staticmethod
    def update_angle():
        Lightning._light_angle = (time.time() % 360) * 5
        Lightning.update_gl()

    @staticmethod
    def update_gl():
        light_position = glm.vec3(*Lightning._light_pos())
        light_projection = glm.ortho(-1.0, 1.0, -1.0, 1.0, 0.5, 6.0)
        light_view = glm.lookAt(glm.vec3(*Lightning._light_pos()), glm.vec3(0.0, 0.0, 0.0), glm.vec3(0, 1, 0))

        Program.use()
        Program.forward_vec3("light_position", light_position)
        Program.forward_mat4("light_projection", light_projection)
        Program.forward_mat4("light_view", light_view)

        ShadowProgram.use()
        ShadowProgram.forward_vec3("light_position", light_position)
        ShadowProgram.forward_mat4("light_projection", light_projection)
        ShadowProgram.forward_mat4("light_view", light_view)


