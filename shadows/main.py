from camera import Camera
from controls import Controls
from display import *
from lightning import Lightning
from objloader import ObjLoader
from program import Program
from shader.shader import Shader


def main():
    # Will use GLUT https://compgraphics.info/OpenGL/template_glut.php,
    # but on Python https://wiki.python.org/moin/PyOpenGL

    obj_file = ObjLoader("models/box/box.obj")

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(Display.width, Display.height)
    glutCreateWindow("HW3, Shadows, Tankov Vladislav")

    Program.prepare(obj_file.prepared_vertices)

    Program.create()
    Program.attach_shader(Shader.load("shader/vertex.glsl", GL_VERTEX_SHADER))
    Program.attach_shader(Shader.load("shader/fragment.glsl", GL_FRAGMENT_SHADER))
    Program.link()

    Program.use()

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
