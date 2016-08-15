from enum import Enum


class Font(Enum):
    """most common font codes - note not all are widely supported
    """

    bold = 1
    dim = 2
    italic = 3
    underlined = 4
    blink = 5
    fast_blink = 6
    negative = 7
    concealed = 8
    strike_through = 9


class InverseFont(Enum):
    """turns off common fonts - think of them as ``not`` operators
    """

    bold = 21
    dim = 22
    italic = 23
    underlined = 24
    blink = 25
    negative = 27
    concealed = 28
    strike_through = 29


class AlternativeFont(Enum):
    """uses system set alternative font faces
    """

    primary = 10
    first = 11
    second = 12
    third = 13
    fourth = 14
    fifth = 15
    sixth = 16
    seventh = 17
    eighth = 18
    ninth = 19
    fraktur = 20


class UncommonFont(Enum):
    """rarely supported fonts
    """

    framed = 51
    circled = 52
    overlined = 53


class InverseUncommonFont(Enum):
    """turns off uncommon fonts - think of these as ``not`` operators for ``UncommonFont`` values
    """

    framed = 54
    overlined = 55


class IdeogramFont(Enum):
    """very rarely supported fonts
    """

    underlined = 60
    double_underlined = 61
    overlined = 62
    double_overlined = 63
    stressed = 64
    off = 65
