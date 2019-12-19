def plane(scale, z=-0.3):
    return [
        [scale * v for v in x] for x in [
            (-1, z, -1), (-1, z, 1), (1, z, -1),
            (-1, z, 1), (1, z, -1), (1, z, 1)
        ]
    ]
