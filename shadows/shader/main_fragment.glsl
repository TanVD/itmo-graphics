#version 330 core

out vec4 frag_color;

in vec2 frag_texture_coord;

in vec3 frag_pos;
in vec3 normal;
in vec4 light_frag_pos;

//Based on https://learnopengl.com/Lighting/Basic-Lighting
vec3 ambient_coef = vec3(0.02, 0.02, 0.02);
vec3 diffuse_coef = vec3(0.4, 0.4, 0.4);
vec3 specular_coef = vec3(0.5, 0.5, 0.5);

vec3 color = vec3(0.2, 1, 0.5);

uniform vec3 camera_position;
uniform vec3 light_position;

uniform sampler2D shadow_map;

vec3 light_direction = normalize(light_position);

float calculate_shadows() {
    vec3 coords = (light_frag_pos.xyz / light_frag_pos.w) * 0.5 + 0.5;
    float depth_by_map = texture(shadow_map, coords.xy).r;
    float depth_by_world = coords.z;
    float shadow = 0.0;
    if (depth_by_world - 0.001 > depth_by_map) {
        shadow = 1.0;
    }
    return 1.0 - shadow;
}

vec3 calculate_ambient() {
    return ambient_coef * color;
}

vec3 calculate_diffuse() {
    float diff = max(dot(normalize(normal), light_direction), 0.0);
    return diffuse_coef * diff * color;
}

vec3 calculate_specular() {
    vec3 view_direction = normalize(camera_position - frag_pos);
    vec3 reflect_direction = reflect(-light_direction, normalize(normal));
    float spec = pow(max(dot(view_direction, reflect_direction), 0.0), 3);
    vec3 specular = specular_coef * spec * color;
    return specular;
}

void main() {
    vec3 ambient_color = calculate_ambient();
    vec3 diffuse_color = calculate_diffuse();
    vec3 specular_color = calculate_specular();
    float shadow = calculate_shadows();

    frag_color = vec4(ambient_color +  shadow * (diffuse_color + specular_color), 1);
}
