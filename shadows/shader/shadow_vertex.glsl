#version 130

uniform mat4 model;
uniform mat4 light_view;
uniform mat4 light_projection;

void main() {
    gl_Position = light_projection * (light_view * (model * gl_Vertex));
}