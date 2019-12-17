#version 130

in vec2 texCoord;
out vec2 fragTexCoord;

void main() {
    gl_Position = ftransform();
    fragTexCoord = texCoord;
}
