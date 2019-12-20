import numpy as np

from camera import Camera
from controls import Controls
from display import *
from lightning import Lightning
from objloader import ObjLoader
from program import Program
from shader.shader import Shader
from util import plane


def main():
    # Will use GLUT https://compgraphics.info/OpenGL/template_glut.php,
    # but on Python https://wiki.python.org/moin/PyOpenGL

    obj_file = ObjLoader("models/bunny.obj")
    obj_file.add_plane(plane(0.2, 0.1))

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(Display.width, Display.height)
    glutCreateWindow("HW3, Shadows, Tankov Vladislav")

    ShadowProgram.prepare()
    ShadowProgram.create()
    ShadowProgram.attach_shader(Shader.load("shader/shadow_vertex.glsl", GL_VERTEX_SHADER))
    ShadowProgram.attach_shader(Shader.load("shader/shadow_fragment.glsl", GL_FRAGMENT_SHADER))
    ShadowProgram.link()
    ShadowProgram.use()
    ShadowProgram.after_create(obj_file.prepared_vertices, obj_file.prepared_normals)

    Program.prepare()
    Program.create()
    Program.attach_shader(Shader.load("shader/main_vertex.glsl", GL_VERTEX_SHADER))
    Program.attach_shader(Shader.load("shader/main_fragment.glsl", GL_FRAGMENT_SHADER))
    Program.link()
    Program.use()
    Program.after_create(obj_file.prepared_vertices, obj_file.prepared_normals)

    Camera.update_gl()
    Lightning.update_gl()

    glutDisplayFunc(Display.display(obj_file.prepared_vertices))
    glutReshapeFunc(Display.reshape)

    glutIdleFunc(Display.idle)

    glutMouseFunc(Controls.mouse)
    glutMotionFunc(Controls.motion)

    glutMainLoop()


if __name__ == '__main__':
    main()
