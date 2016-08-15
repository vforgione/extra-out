from enum import Enum

FOREGROUND_BASE_CODE = 30
BACKGROUND_BASE_CODE = 40


class Color(Enum):
    """color codes including ``default`` and the rarely supported ``rgb`` code
    """

    black = 0
    red = 1
    green = 2
    yellow = 3
    blue = 4
    magenta = 5
    cyan = 6
    white = 7
    rgb = 8
    default = 9

    @property
    def as_foreground(self):
        return FOREGROUND_BASE_CODE + self.value

    @property
    def as_background(self):
        return BACKGROUND_BASE_CODE + self.value
