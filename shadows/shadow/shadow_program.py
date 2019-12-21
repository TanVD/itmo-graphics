import glm
from OpenGL.GL import *


class ShadowProgram:
    width = 1024
    height = 1024
    _instance = None

    depth_buffer = 0
    _depth_texture = 0

    @staticmethod
    def prepare(vertices, normals):
        glEnable(GL_DEPTH_TEST)
        glBindFramebuffer(GL_FRAMEBUFFER, 0)

        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointer(3, GL_FLOAT, 0, vertices)
        glEnableClientState(GL_NORMAL_ARRAY)
        glNormalPointer(GL_FLOAT, 0, normals)
        return

    @staticmethod
    def after_create():
        glEnable(GL_DEPTH_TEST)

        ShadowProgram.depth_buffer = glGenFramebuffers(1)
        glBindFramebuffer(GL_FRAMEBUFFER, ShadowProgram.depth_buffer)

        ShadowProgram._depth_texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, ShadowProgram._depth_texture)

        glTexImage2D(GL_TEXTURE_2D, 0, GL_DEPTH_COMPONENT16, ShadowProgram.width, ShadowProgram.height, 0,
                     GL_DEPTH_COMPONENT, GL_FLOAT, 0)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

        glFramebufferTexture(GL_FRAMEBUFFER, GL_DEPTH_ATTACHMENT, ShadowProgram._depth_texture, 0)
        glDrawBuffer(GL_NONE)
        if glCheckFramebufferStatus(GL_FRAMEBUFFER) != GL_FRAMEBUFFER_COMPLETE:
            exit(1)

        return

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

    @staticmethod
    def depth_texture():
        return ShadowProgram._depth_texture
