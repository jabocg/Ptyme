#!/usr/bin/env python
# easygui doesn't work with python3, using python 2 for now
# python 3

import sys
# import logging
import time
import easygui as gui

# logging.baseConfig(format='%(asctime)s %(message)s',
#                    dateftm='%Y-%m-%dT%H:%M:%S')

def main():
    # print(sys.argv)
    if len(sys.argv) == 1:
        print("give a string for time, _h_m_s for hours, mins, secs, optional"
              "string for title")
        sys.exit()
    timetosleep = parseArgsChar(sys.argv[1])
    nap(timetosleep)

def nap(duration):
    # print("napping for " + str(duration) + " seconds")
    wakeup = False
    while not wakeup:
        # print(duration)
        time.sleep(1)
        duration -= 1
        wakeup = duration <= 0
    # print("you have napped")
    gui.msgbox("wake up")

# go through via characters
def parseArgsChar(timeStr):
    hours = minutes = seconds = 0
    head = 0
    for ind, char in enumerate(timeStr):
        # print(ind, char, head)
        if char == 'h':
            # print("found h")
            hours = int(timeStr[head:ind])
            head = ind + 1
        elif char == 'm':
            # print("found m")
            minutes = int(timeStr[head:ind])
            head = ind + 1
        elif char == 's':
            # print("found s")
            seconds = int(timeStr[head:ind])
            head = ind + 1
        elif char.isalpha():
            head = ind + 1
    # print(timeStr)
    # print('hours:' + str(hours))
    # print('mins: ' + str(minutes))
    # print('sec: ' + str(seconds))
    return hours * 3600 + minutes * 60 + seconds


if __name__ == "__main__":
    main()
