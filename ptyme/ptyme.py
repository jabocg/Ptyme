#!/usr/bin/env python3
# python 3

import sys
import logging

logging.baseConfig(format='%(asctime)s %(message)s',
                   dateftm='%Y-%m-%dT%H:%M:%S')

def main():
    print(sys.argv)
    if len(sys.argv) == 1:
        print("give a string for time, _h_m_s for hours, mins, secs, optional"
              "string for title")
        sys.exit()
    parseArgsChar(sys.argv[1])


# go through via characters
def parseArgsChar(timeStr):
    hours = minutes = seconds = 0
    head = 0
    for ind, char in enumerate(timeStr):
        print(ind, char, head)
        if char == 'h':
            print("found h")
            hours = timeStr[head:ind]
            head = ind + 1
        if char == 'm':
            print("found m")
            minutes = timeStr[head:ind]
            head = ind + 1
        if char == 's':
            print("found s")
            seconds = timeStr[head:ind]
            head = ind + 1
    print(timeStr)
    print('hours:', hours)
    print('mins: ', minutes)
    print('sec: ', seconds)


if __name__ == "__main__":
    main()
