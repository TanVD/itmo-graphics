import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class Model:
    vbo = None
    tbo = None
    nbo = None

    @staticmethod
    def create_buffers(vertices, tex_coords, normals):
        vertices = np.array(vertices, dtype=np.float32).flatten()
        tex_coords = np.array(tex_coords, dtype=np.float32).flatten()
        normals = np.array(normals, dtype=np.float32).flatten()
        """
        Creates vertex buffer objects for the vertices, texCoords, and normals.
        Binds the ids to the vertex data.
        """
        vbo, tbo, nbo = glGenBuffers(3)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, len(vertices) * 4, vertices, GL_STATIC_DRAW)
        glBindBuffer(GL_ARRAY_BUFFER, tbo)
        glBufferData(GL_ARRAY_BUFFER, len(tex_coords) * 4, tex_coords, GL_STATIC_DRAW)
        glBindBuffer(GL_ARRAY_BUFFER, nbo)
        glBufferData(GL_ARRAY_BUFFER, len(normals) * 4, normals, GL_STATIC_DRAW)
        glBindBuffer(GL_ARRAY_BUFFER, 0)

        Model.vbo = vbo
        Model.tbo = tbo
        Model.nbo = nbo
