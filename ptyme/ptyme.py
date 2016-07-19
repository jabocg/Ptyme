#!/usr/bin/env python3
# easygui doesn't work with python3, using python 2 for now
# python 3

import sys
import logging
import time

logging.basicConfig(format='%(asctime)s - %(levename)s : %(message)s',
                    dateftm='%Y-%m-%dT%H:%M:%S%z')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def main():
    # print(sys.argv)
    # logger.debug(sys.argv)
    if len(sys.argv) == 1:
        print("give a string for time, 'xhymzs' for hours, mins, secs,"
              "optional string for title")
        sys.exit()
    timetosleep = parseArgsChar(sys.argv[1])
    nap(timetosleep)


def nap(duration):
    logger.debug("napping for %d seconds", duration)
    wakeup = False
    while not wakeup:
        logger.debug("%d seconds remaining", duration)
        time.sleep(1)
        duration -= 1
        wakeup = duration <= 0
    logger.debug("you have napped")


# go through via characters
def parseArgsChar(timeStr):
    hours = minutes = seconds = 0
    head = 0
    for ind, char in enumerate(timeStr):
        # print(ind, char, head)
        logger.debug("ind: %d\nchar: %s\nhead: %d", ind, char, head)
        if char == 'h':
            logger.debug("found h")
            hours = int(timeStr[head:ind])
            head = ind + 1
        elif char == 'm':
            logger.debug("found m")
            minutes = int(timeStr[head:ind])
            head = ind + 1
        elif char == 's':
            logger.debug("found s")
            seconds = int(timeStr[head:ind])
            head = ind + 1
        elif not char.isdigit():
            logger.debug("found some other non-digit character")
            head = ind + 1
    # print(timeStr)
    logger.debug("total time: %s", timeStr)
    logger.debug("hours: %d\nmins: %d\nsecs: %d\n", hours, minutes, seconds)
    return hours * 3600 + minutes * 60 + seconds


if __name__ == "__main__":
    main()
