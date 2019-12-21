from config import Config
from camera import Camera
from controls import Controls
from display import *
from lightning import Lightning
from model import Model
from objloader import ObjLoader
from program import Program
from shader.shader import Shader
from shadow.shadow_map import ShadowMap
from util import plane


def cb_dbg_msg(source, msg_type, msg_id, severity, length, raw, user):
    msg = raw[0:length]
    print('debug', source, msg_type, msg_id, severity, msg)


def main():
    # Will use GLUT https://compgraphics.info/OpenGL/template_glut.php,
    # but on Python https://wiki.python.org/moin/PyOpenGL

    obj_file = ObjLoader(f"models/{Config.model}.obj")
    obj_file.add_plane(plane(0.2, 0.1))

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(Config.width, Config.height)
    glutCreateWindow("HW3, Shadows, Tankov Vladislav")

    # glEnable(GL_DEBUG_OUTPUT)
    # glDebugMessageCallback(GLDEBUGPROC(cb_dbg_msg), None)
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_DEPTH_TEST)

    Model.create_buffers(obj_file.prepared_vertices, obj_file.prepared_tex_coords, obj_file.prepared_normals)
    ShadowMap.create()

    ShadowProgram.create()
    ShadowProgram.attach_shader(Shader.load("shader/shadow_vertex.glsl", GL_VERTEX_SHADER))
    ShadowProgram.attach_shader(Shader.load("shader/shadow_fragment.glsl", GL_FRAGMENT_SHADER))
    ShadowProgram.link()
    ShadowProgram.use()

    Program.create()
    Program.attach_shader(Shader.load("shader/main_vertex.glsl", GL_VERTEX_SHADER))
    Program.attach_shader(Shader.load("shader/main_fragment.glsl", GL_FRAGMENT_SHADER))
    Program.link()
    Program.use()

    Camera.update_gl()
    Lightning.update_gl()

    glutDisplayFunc(Display.display(obj_file.prepared_vertices, obj_file.prepared_normals))
    glutReshapeFunc(Display.reshape)

    glutIdleFunc(Display.idle)

    glutMouseFunc(Controls.mouse)
    glutMotionFunc(Controls.motion)

    glutMainLoop()


if __name__ == '__main__':
    main()
