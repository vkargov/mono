#!/usr/bin/env python3

import sys
import re

argv = sys.argv[1:]

if argv[0][0] == '-' and argv[0][1:].isdigit():
    remaining_diffs = int(argv[0][1:])
    limited_diffs = True
    argv = argv[1:]
else:
    limited_diffs = False

if argv[0] == '--':
    argv = argv[1:]

assert(len(argv) == 2)

left_file = open(argv[0], 'r')
right_file = open(argv[1], 'r')
lineno = 0
files_match = True

nopref_regexp = re.compile('\[[^]]*\]\s*')
nohex_regexp = re.compile('0x[0-9A-Fa-f]+|\(nil\)')

while True:
    lines = {}
    lines[0] = left_file.readline()
    lines[1] = right_file.readline()
    for i in range(2):
        lines[i] = nopref_regexp.sub('', lines[i])
        lines[i] = nohex_regexp.sub('', lines[i])
    if lines[0] != lines[1]:
        print('Line {0} differs!'.format(lineno))
        print('< {0}'.format(lines[0]), end='')
        print('> {0}'.format(lines[1]), end='')
        files_match = False
        if limited_diffs:
            remaining_diffs -= 1
            if remaining_diffs <= 0:
                break
    if lines[0] == '' or lines[1] == '':
        break
    lineno += 1

sys.exit(0 if files_match else 1)
