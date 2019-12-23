import glm
import numpy as np
from OpenGL.GL import *


class Program:
    _instance = None

    @staticmethod
    def create():
        assert Program._instance is None
        Program._instance = glCreateProgram()

    @staticmethod
    def get():
        assert Program._instance is not None
        return Program._instance

    @staticmethod
    def link():
        glLinkProgram(Program.get())

    @staticmethod
    def use():
        glUseProgram(Program.get())

    @staticmethod
    def disable():
        glUseProgram(0)

    @staticmethod
    def _forward_location(name):
        return glGetUniformLocation(Program.get(), name)

    @staticmethod
    def forward_int(name, value):
        glProgramUniform1i(Program.get(), Program._forward_location(name), value)

    @staticmethod
    def forward_float(name, value):
        glProgramUniform1f(Program.get(), Program._forward_location(name), value)

    @staticmethod
    def forward_vec3(name, value):
        arr = np.array(value, dtype=np.float32)
        glProgramUniform3fv(Program.get(), Program._forward_location(name), 1, arr)

    @staticmethod
    def forward_mat4(name, value):
        arr = np.array(value, dtype=np.float32)
        glProgramUniformMatrix4fv(Program.get(), Program._forward_location(name), 1, GL_FALSE, arr)

    @staticmethod
    def forward_2d_texture(index, name, coords):
        glBindAttribLocation(Program.get(), index, name)
        glEnableVertexAttribArray(index)
        glVertexAttribPointer(index, 2, GL_FLOAT, False, 0, coords)
        return index

    @staticmethod
    def get_location(name):
        return glGetUniformLocation(Program.get(), name)

    @staticmethod
    def attach_shader(shader):
        glAttachShader(Program.get(), shader)
