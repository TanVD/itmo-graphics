#version 330 core

layout (location = 0) in vec3 a_pos;
layout (location = 1) in vec3 a_normal;
layout (location = 4) in vec2 a_tex_coords;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

uniform mat4 light_view;
uniform mat4 light_projection;

out vec3 frag_pos;
out vec3 normal;
out vec2 tex_coords;
out vec4 light_frag_pos;

//Based on examples from https://learnopengl.com/Lighting/
void main() {
    frag_pos = vec3(model * vec4(a_pos, 1.0f));
    light_frag_pos = light_projection * (light_view * vec4(frag_pos, 1.0));
    normal =  normalize(a_normal);
    tex_coords = a_tex_coords;
    gl_Position = projection * view * model * vec4(a_pos, 1.0);
}
