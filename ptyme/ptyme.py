#!/bin/env python3
# python 3

import sys


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


# while this works, it only works when _h_m_s format
# might want to not do that
def parseArgs(timeStr):
    time = timeStr.split('h')
    if 'm' not in time[0] and 'n' not in time[0]:
        hours = time[0]
    else:
        hours = 0
    print(time)
    print(hours)
    time = time[1].split('m')
    if 's' not in time[0]:
        minutes = time[0]
    else:
        minutes = 0
    print(time)
    print(minutes)
    time = time[1].split('s')
    if time:
        seconds = time[0]
    else:
        seconds = 0
    print(time)
    print(seconds)

if __name__ == "__main__":
    main()
