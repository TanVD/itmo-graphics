import glm
from OpenGL.GL import *

from shadow.shadow_program import ShadowProgram


class Program:
    _instance = None

    @staticmethod
    def prepare():
        return

    @staticmethod
    def create():
        assert Program._instance is None
        Program._instance = glCreateProgram()

    @staticmethod
    def after_create(vertices, normals):
        glEnable(GL_DEPTH_TEST)
        glClearColor(20 / 255, 20 / 255, 20 / 255, 1)

        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointer(3, GL_FLOAT, 0, vertices)
        glEnableClientState(GL_NORMAL_ARRAY)
        glNormalPointer(GL_FLOAT, 0, normals)


    @staticmethod
    def get():
        assert Program._instance is not None
        return Program._instance

    @staticmethod
    def link():
        glLinkProgram(Program.get())

    @staticmethod
    def use():
        glUseProgram(0)
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
        glProgramUniform3fv(Program.get(), Program._forward_location(name), 1, glm.value_ptr(value))

    @staticmethod
    def forward_mat4(name, value):
        glProgramUniformMatrix4fv(Program.get(), Program._forward_location(name), 1, GL_FALSE, glm.value_ptr(value))

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
