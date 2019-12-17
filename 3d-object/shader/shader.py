from OpenGL.GL import *


class Shader:
    @staticmethod
    def load(path, type):
        with open(path) as file:
            shader = glCreateShader(type)
            glShaderSource(shader, file.read())
            glCompileShader(shader)
            return shader
