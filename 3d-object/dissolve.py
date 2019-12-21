import time
from math import cos
from display import *

from program import Program


class DissolveAnimation:
    _slow_factor = 5
    _enabled = True

    @staticmethod
    def enable():
        DissolveAnimation._enabled = True
        DissolveAnimation.update_gl()

    @staticmethod
    def disable():
        DissolveAnimation._enabled = False
        DissolveAnimation.update_gl()

    @staticmethod
    def update_gl():
        if not DissolveAnimation._enabled:
            glUniform1f(Program.get_location("noise_level"), 2)
        else:
            glUniform1f(Program.get_location("noise_level"), abs(cos(time.time() / DissolveAnimation._slow_factor)))
