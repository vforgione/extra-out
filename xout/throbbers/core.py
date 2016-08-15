import random
import sys
import time

from .patterns import braille

REST = 0.1


def throb(callback, output=None, rest=REST, values=braille, randomize=False, wait_for=True):

    kwargs = {'throbber': None, 'output': output}
    if output:
        template = '\r{throbber} {output}'
    else:
        template = '\r{throbber}'

    iteration = 0
    while callback() != wait_for:
        if randomize:
            kwargs['throbber'] = random.choice(values)
        else:
            kwargs['throbber'] = values[iteration]
            iteration += 1
            if iteration >= len(values):
                iteration = 0

        sys.stdout.write(template.format(**kwargs))
        sys.stdout.flush()
        time.sleep(rest)

    sys.stdout.write('\n')
