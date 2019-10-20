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
    def _forward_location(name):
        return glGetUniformLocation(Program.get(), name)

    @staticmethod
    def forward_int(name, value):
        glProgramUniform1i(Program.get(), Program._forward_location(name), value)

    @staticmethod
    def forward_float(name, value):
        glProgramUniform1f(Program.get(), Program._forward_location(name), value)

    @staticmethod
    def attach_shader(shader):
        glAttachShader(Program.get(), shader)
