from OpenGL.GL import *


class Shader:
    @staticmethod
    def load(path, type):
        with open(path) as file:
            shader = glCreateShader(type)
            glShaderSource(shader, file.read())
            glCompileShader(shader)

            if not glGetShaderiv(shader, GL_COMPILE_STATUS):
                print(f"OpenGL shader error: {str(glGetShaderInfoLog(shader))}")
                exit(1)
            return shader
