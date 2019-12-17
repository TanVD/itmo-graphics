#version 130

uniform sampler2D noise;
uniform float noise_level = 1;

varying vec3 normal;
varying vec3 eye_position;
uniform vec4 red = vec4(1, 0, 0, 0);

in vec2 frag_texture_coord;

void main() {
    if (texture(noise, frag_texture_coord)[0] > noise_level) {
        discard;
    }
    float light_force = 0.5 * dot(normal, eye_position);
    gl_FragColor += red * light_force;
}
