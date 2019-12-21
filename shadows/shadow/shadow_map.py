from OpenGL.GL import *


class ShadowMap:
    width = 1024
    height = 1024
    _instance = None

    depth_buffer = 0
    depth_texture = 0

    @staticmethod
    def create():
        glBindTexture(GL_TEXTURE_2D, 0)
        glBindFramebuffer(GL_FRAMEBUFFER, 0)
        ShadowMap.depth_texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, ShadowMap.depth_texture)

        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_DEPTH_COMPONENT, ShadowMap.width, ShadowMap.height, 0,
                     GL_DEPTH_COMPONENT, GL_FLOAT, None)

        ShadowMap.depth_buffer = glGenFramebuffers(1)
        glBindFramebuffer(GL_FRAMEBUFFER, ShadowMap.depth_buffer)
        glFramebufferTexture2D(GL_FRAMEBUFFER, GL_DEPTH_ATTACHMENT, GL_TEXTURE_2D, ShadowMap.depth_texture, 0)
        glBindFramebuffer(GL_FRAMEBUFFER, 0)
        glBindTexture(GL_TEXTURE_2D, 0)

        if glCheckFramebufferStatus(GL_FRAMEBUFFER) != GL_FRAMEBUFFER_COMPLETE:
            exit(1)

        return
