from .colors import Color

ESCAPE_SEQUENCE = '\x1b[{}m'
RESET_FORMATTING = ESCAPE_SEQUENCE.format('0')


def colorize(text, foreground=None, background=None, font=None, reset=True):
    """Applies color and font transforms to the text

    :param text: the text to be formatted
    :type text: str

    :param foreground: selected foreground color value
    :type foreground: Color

    :param background: selected background color value
    :type background: Color

    :param font: selected font face value
    :type font: Font or InverseFont or AlternativeFont or UncommonFont or InverseUncommonFont or IdeogramFont or list

    :param reset: should we reset all formatting transformations at the end of the text (default = True)
    :type reset: bool

    :return: text with applicable formatting escape strings
    :rtype: str
    """

    codes = []
    if foreground:
        codes.append(foreground)
    if background:
        codes.append(background)
    if font:
        if hasattr(font, '__iter__'):
            font = ';'.join(str(f.value) for f in font)
        codes.append(font)

    output = ''
    if len(codes):
        codes = ';'.join(str(c) for c in codes)
        output = ESCAPE_SEQUENCE.format(codes)

    output += text

    if reset:
        output += RESET_FORMATTING

    return output
