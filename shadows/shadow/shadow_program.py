import glm
from OpenGL.GL import *


class ShadowProgram:
    _instance = None

    @staticmethod
    def create():
        assert ShadowProgram._instance is None
        ShadowProgram._instance = glCreateProgram()

    @staticmethod
    def get():
        assert ShadowProgram._instance is not None
        return ShadowProgram._instance

    @staticmethod
    def link():
        glLinkProgram(ShadowProgram.get())

    @staticmethod
    def use():
        glUseProgram(0)
        glUseProgram(ShadowProgram.get())

    @staticmethod
    def disable():
        glUseProgram(0)

    @staticmethod
    def _forward_location(name):
        return glGetUniformLocation(ShadowProgram.get(), name)

    @staticmethod
    def forward_int(name, value):
        glProgramUniform1i(ShadowProgram.get(), ShadowProgram._forward_location(name), value)

    @staticmethod
    def forward_float(name, value):
        glProgramUniform1f(ShadowProgram.get(), ShadowProgram._forward_location(name), value)

    @staticmethod
    def forward_vec3(name, value):
        glProgramUniform3fv(ShadowProgram.get(), ShadowProgram._forward_location(name), 1, glm.value_ptr(value))

    @staticmethod
    def forward_mat4(name, value):
        glProgramUniformMatrix4fv(ShadowProgram.get(), ShadowProgram._forward_location(name), 1, GL_FALSE,
                                  glm.value_ptr(value))

    @staticmethod
    def forward_2d_texture(index, name, coords):
        glBindAttribLocation(ShadowProgram.get(), index, name)
        glEnableVertexAttribArray(index)
        glVertexAttribPointer(index, 2, GL_FLOAT, False, 0, coords)
        return index

    @staticmethod
    def get_location(name):
        return glGetUniformLocation(ShadowProgram.get(), name)

    @staticmethod
    def attach_shader(shader):
        glAttachShader(ShadowProgram.get(), shader)

