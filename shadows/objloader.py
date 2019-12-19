# Based ob PyGame tutorial for Obj loading
import numpy as np


def normalize(v):
    norm = np.linalg.norm(v)
    if norm:
        v = np.divide(v, norm)
    return v


class ObjLoader:
    def __init__(self, filename, swapyz=False):
        """Loads a Wavefront OBJ file. """
        self.vertices = []
        self.normals = []
        self.texcoords = []
        self.faces = []

        self.prepared_vertices = []
        self.prepared_normals = []
        self.prepared_tex_coords = []

        material = None
        for line in open(filename, "r"):
            if line.startswith('#'): continue
            values = line.split()
            if not values:
                continue
            if values[0] == 'v':
                v = (float(values[1]), float(values[2]), float(values[3]))
                if swapyz:
                    v = v[0], v[2], v[1]
                self.vertices.append(v)
            elif values[0] == 'vn':
                v = (float(values[1]), float(values[2]), float(values[3]))
                if swapyz:
                    v = v[0], v[2], v[1]
                self.normals.append(v)
            elif values[0] == 'vt':
                v = (float(values[1]), float(values[2]))
                self.texcoords.append(v)
            elif values[0] == 'f':
                face = []
                texcoords = []
                norms = []
                for v in values[1:]:
                    w = v.split('/')
                    face.append(int(w[0]))
                    if len(w) >= 2 and len(w[1]) > 0:
                        texcoords.append(int(w[1]))
                    else:
                        texcoords.append(0)
                    if len(w) >= 3 and len(w[2]) > 0:
                        norms.append(int(w[2]))
                    else:
                        norms.append(0)
                self.faces.append((face, norms, texcoords, material))
        self.prepare()

    def prepare(self):
        for (face, norms, texcoords, material) in self.faces:
            for i in [0, 1, 2]:
                vert_index = face[i] - 1
                self.prepared_vertices.append(self.vertices[vert_index])
            if len(face) > 3:
                for i in [0, 2, 3]:
                    vert_index = face[i] - 1
                    self.prepared_vertices.append(self.vertices[vert_index])

            if self.texcoords:
                for i in [0, 1, 2]:
                    tex_index = texcoords[i] - 1
                    self.prepared_tex_coords.append(self.texcoords[tex_index])
                if len(texcoords) > 3:
                    for i in [0, 2, 3]:
                        tex_index = texcoords[i] - 1
                        self.prepared_tex_coords.append(self.texcoords[tex_index])

        if not self.texcoords:
            self.prepared_tex_coords = self.prepared_vertices

        for i in range(0, len(self.prepared_vertices), 3):
            mat = [self.prepared_vertices[i + j] for j in range(3)]
            ab = np.subtract(mat[1], mat[0])
            ac = np.subtract(mat[2], mat[0])
            self.prepared_normals.extend([list(normalize(np.cross(ab, ac)))] * 3)

    def add_plane(self, plane):
        self.prepared_tex_coords.extend(plane)
        self.prepared_vertices.extend(plane)
        for i in range(0, len(plane), 3):
            mat = [plane[i + j].copy() for j in range(3)]
            ab = np.subtract(mat[1], mat[0])
            ac = np.subtract(mat[2], mat[0])
            self.prepared_normals.extend([list(normalize(np.cross(ab, ac)))] * 3)
