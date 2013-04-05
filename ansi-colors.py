#!/usr/bin/env python

import sys

FOREGROUNDS = [
    '0m',  '1m',     # none, bold
    '30m', '1;30m',  # black
    '31m', '1;31m',  # red
    '32m', '1;32m',  # green
    '33m', '1;33m',  # yellow
    '34m', '1;34m',  # blue
    '35m', '1;35m',  # magenta
    '36m', '1;36m',  # cyan
    '37m', '1;37m'   # white
]

BACKGROUNDS = [
    '40m',  # black
    '41m',  # red
    '42m',  # green
    '43m',  # yellow
    '44m',  # blue
    '45m',  # magenta
    '46m',  # cyan
    '47m',  # white
    '49m',  # default
]

if __name__ == "__main__":

    text = ' abc123 '
    template = "\x1b[{0}\x1b[{1}{2}\x1b[0m"

    sys.stdout.write(' ' * len(text))

    print(''.join([
        bg.center(len(text))
        for bg in BACKGROUNDS]))

    for fg in FOREGROUNDS:
        sys.stdout.write(fg.rjust(len(text)))

        print(''.join([
            template.format(fg, bg, text)
            for bg in BACKGROUNDS]))
