#version 130

void main() {
    gl_FragDepth = gl_FragCoord.z;
}
