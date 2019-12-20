from noise import pnoise2
from OpenGL.GL import *
from OpenGL.GLUT import *

from program import Program


class Texture:
    size = 256

    @staticmethod
    def _norm(value, min, max):
        return (value - min) / (max - min)

    @staticmethod
    def create_2d(texture_coords):
        # thanks to https://open.gl/textures
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        id = Program.forward_2d_texture(1, "texture_coord", texture_coords)

        texture = glGenTextures(id)
        glBindTexture(GL_TEXTURE_2D, texture)

        # use noise library as pyglet does https://pypi.org/project/noise/
        noise = [
            pnoise2(1 / Texture.size * i, 1 / Texture.size * j, octaves=5, lacunarity=2, repeatx=1, repeaty=1)
            for i in range(Texture.size)
            for j in range(Texture.size)
        ]

        noise_min = min(noise)
        noise_max = max(noise)
        noise = [Texture._norm(x, noise_min, noise_max) for x in noise]

        # Use just RED for noise (also may use Depth)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RED, Texture.size, Texture.size, 0, GL_RED, GL_FLOAT, noise)

        glGenerateMipmap(GL_TEXTURE_2D)
