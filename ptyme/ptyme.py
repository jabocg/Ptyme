#!/bin/env python3

from sys import argv

def main():
    parseArgs()
    print("Nope.")
    print(argv)

# go through via characters
def parseArgsChar():
    pass()

# while this works, it only works when _h_m_s format
# might want to not do that
def parseArgs():
    if len(argv) > 1:
        time = argv[1].split('h')
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
    else:
        print("commands go here")

if __name__ == "__main__":
    main()

