from OpenGL.GL import *


class Shader:
    @staticmethod
    def load_fragment(path):
        with open(path) as file:
            shader = glCreateShader(GL_FRAGMENT_SHADER)
            glShaderSource(shader, file.read())
            glCompileShader(shader)
            return shader
