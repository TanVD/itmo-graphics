#version 130

uniform sampler2D noiseTexture;
uniform float noise_level = 1;

in vec2 fragTexCoord;

void main() {
    if (texture(noiseTexture, fragTexCoord)[0] > noise_level) {
        discard;
    }
    gl_FragColor += texture(noiseTexture, fragTexCoord);
}
