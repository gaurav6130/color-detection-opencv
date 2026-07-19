COLOR_RANGES = {
    "red": (
        (0, 120, 70),
        (10, 255, 255)
    ),

    "green": (
        (40, 40, 40),
        (80, 255, 255)
    ),

    "blue": (
        (100, 150, 0),
        (140, 255, 255)
    ),

    "yellow": (
        (20, 100, 100),
        (30, 255, 255)
    ),

    "black": (
        (0, 0, 0),
        (179, 255, 50)
    )
}


def get_hsv_range(color_name):
    return COLOR_RANGES[color_name.lower()]