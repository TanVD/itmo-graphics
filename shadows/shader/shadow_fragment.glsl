#version 130

void main() {
    gl_FragDepth = gl_FragCoord.z;
    //Needed to show shadowmap
    gl_FragColor = vec4(gl_FragCoord.z, 0, 0, 0);
}
