import time
from math import cos
from display import *

from program import Program


class DissolveAnimation:
    _slow_factor = 5

    @staticmethod
    def animate_dissolve():
        glUniform1f(Program.get_location("noise_level"), abs(cos(time.time() / DissolveAnimation._slow_factor)))
