#!/usr/bin/sh

import sys
import re

left_file = open(sys.argv[1], 'r')
right_file = open(sys.argv[2], 'r')
lineno = 0

nopref_regexp = re.compile('\[[^]]*\]\s*')
nohex_regexp = re.compile('0x[0-9A-Fa-f]*|\(nil\)')

while True:
    lines = {}
    lines[0] = left_file.readline()
    lines[1] = right_file.readline()
    if lines[0] == '' or lines[1] == '':
        sys.exit(1)
    for i in range(2):
        lines[i] = nopref_regexp.sub('', lines[i])
        lines[i] = nohex_regexp.sub('', lines[i])
    if lines[0] != lines[1]:
        print('Line {0} differs!'.format(lineno))
        print('< {0}'.format(lines[0]), end='')
        print('> {0}'.format(lines[1]), end='')
    lineno += 1

sys.exit(0)
