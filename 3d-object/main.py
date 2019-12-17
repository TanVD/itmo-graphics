from controls import Controls
from display import *
from objloader import ObjLoader
from program import Program
from shader.shader import Shader
from texture import Texture


def main():
    # Will use GLUT https://compgraphics.info/OpenGL/template_glut.php,
    # but on Python https://wiki.python.org/moin/PyOpenGL

    obj_file = ObjLoader("models/flash.obj")

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(Display.width, Display.height)
    glutCreateWindow("HW2, Object, Tankov Vladislav")

    Program.prepare(obj_file.prepared_vertices)

    Program.create()
    # forward tex coord to fragment
    Program.attach_shader(Shader.load("shader/vertex_noise.glsl", GL_VERTEX_SHADER))
    # apply noise
    Program.attach_shader(Shader.load("shader/fragment_noise.glsl", GL_FRAGMENT_SHADER))
    Program.link()

    Texture.create_2d(obj_file.prepared_tex_coords)

    Program.use()

    glutDisplayFunc(Display.display(obj_file.prepared_vertices))
    glutReshapeFunc(Display.reshape)

    glutIdleFunc(Display.idle)

    glutMouseFunc(Controls.mouse)
    glutMotionFunc(Controls.motion)

    glutMainLoop()


if __name__ == '__main__':
    main()
