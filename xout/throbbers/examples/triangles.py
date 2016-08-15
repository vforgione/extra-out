from datetime import datetime

from xout.throbbers import throb
from xout.throbbers.patterns import triangles


def _callback():
    return datetime.now().second == 30


if __name__ == '__main__':
    throb(_callback, output='waiting for the current time to be at 30 seconds', values=triangles, rest=0.3)
