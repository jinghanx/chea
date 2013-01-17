#! /usr/bin/env python

import sys

def lcs(string1, string2):
    if not string1 or not string2:
        return []
    elif string1[-1] == string2[-1]:
        return lcs(string1[:-1], string2[:-1]) + [string1[-1]]
    else:
        res1 = lcs(string1[:-1], string2)
        res2 = lcs(string1, string2[:-1])
        if len(res1) > len(res2):
            return res1
        else:
            return res2

def main():
    file = sys.argv[1]
    with open(file, 'r') as f:
        for line in f:
            if line[-1] == '\n':
                line = line[:-1]
            strings = line.split(';')
            if len(strings) == 2:
                print ''.join(lcs(strings[0], strings[1]))

if __name__ == '__main__':
    main()
