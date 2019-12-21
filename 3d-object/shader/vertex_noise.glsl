#version 130

in vec2 texture_coord;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

out vec3 frag_pos;
out vec3 normal;
out vec2 frag_texture_coord;

//Based on examples from https://learnopengl.com/Lighting/
void main() {
    frag_texture_coord = texture_coord;
    normal = gl_Normal;

    frag_pos = vec3(model * gl_Vertex);
    gl_Position = projection * (view * (model * vec4(vec3(gl_Vertex), 1.0f)));
}
