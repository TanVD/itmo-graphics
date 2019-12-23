#version 330 core

in vec4 gl_Vertex;
in vec3 gl_Normal;
in vec2 texture_coord;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

uniform mat4 light_view;
uniform mat4 light_projection;

out vec3 color;
out vec3 frag_pos;
out vec3 normal;
out vec2 tex_coords;
out vec4 light_frag_pos;

out vec2 frag_texture_coord;

//Based on examples from https://learnopengl.com/Lighting/
void main() {
    frag_texture_coord = texture_coord;
    frag_pos = vec3(model * gl_Vertex);
    light_frag_pos = light_projection * (light_view * vec4(frag_pos, 1.0f));
    normal = gl_Normal;
    gl_Position = projection * (view * (model * vec4(vec3(gl_Vertex), 1.0f)));
}
