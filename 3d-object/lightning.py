import math
import time

import glm

from config import Config
from program import Program


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
        Program.forward_mat4("model",
                             glm.scale(glm.mat4(), glm.vec3(Config.scale, Config.scale, Config.scale)))
        Program.forward_vec3("light_position", glm.vec3(*Lightning._light_pos()))
