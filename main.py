from OpenGL.GL import *
from OpenGL.GLUT import *

from canvas import Canvas
from display import *
from program import Program
from shader.shader import Shader
from texture import Texture


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    Program.use()

    Program.forward_float("center_x", center_x)
    Program.forward_float("center_y", center_y)

    Canvas.paint()

    glutSwapBuffers()


def main():
    # Will use GLUT https://compgraphics.info/OpenGL/template_glut.php,
    # but on Python https://wiki.python.org/moin/PyOpenGL

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowSize(width, height)
    glutCreateWindow("HW1, Mandelbrot, Tankov Vladislav")

    Texture.create_1d()
    Program.create()
    Program.attach_shader(Shader.load_fragment("shader/shader_frag.glsl"))
    Program.link()

    glutDisplayFunc(display)

    glutMainLoop()


if __name__ == '__main__':
    main()
