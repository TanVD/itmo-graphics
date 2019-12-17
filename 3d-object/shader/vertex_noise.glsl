#version 130

varying vec3 normal;
varying vec3 eye_position;

in vec2 texture_coord;
out vec2 frag_texture_coord;

void main() {
    // based on lightning tutorial
    eye_position = normalize(vec3(gl_ModelViewMatrix * gl_Vertex));
    normal = normalize(gl_NormalMatrix * gl_Normal);

    gl_Position = ftransform();
    frag_texture_coord = texture_coord;
}
