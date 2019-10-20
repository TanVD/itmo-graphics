uniform sampler1D texture;
uniform float center_x;
uniform float center_y;

void main() {
    vec2 mandelbrot_point;
    center_x = gl_TexCoord[0].x - center_x;
    center_y = gl_TexCoord[0].y - center_y;

    mandelbrot_point.x = center_x;
    mandelbrot_point.y = center_y;

    int iter;
    for (iter = 0; iter < 100; iter++) {
        float new_x = mandelbrot_point.x * mandelbrot_point.x - mandelbrot_point.y * mandelbrot_point.y + center_x;
        float new_y = 2 * mandelbrot_point.y * mandelbrot_point.x + center_y;

        mandelbrot_point.x = new_x;
        mandelbrot_point.y = new_y;

        float abs = new_x * new_x + new_y * new_y;

        //See Wikipedia: it says we can use last iteration before > 4 as a determinator
        if (abs > 4.0) break;
    }

    gl_FragColor = texture1D(texture, float(iter) / 100);
}