#!/bin/env python3

from sys import argv

def main():
    parseArgs()
    print("Nope.")
    print(argv)

def parseArgs():
    if len(argv) > 1:
        time = argv[1].split('h')
        print(time)
        if 'm' not in time[0] and 'n' not in time[0]:
            hours = time[0]
        else:
            house = 0
        time = time[0].split('m')
        print(time)
        if 's' not in time[0]:
            minutes = time[0]
        else:
            minutes = 0
        time = time[0].split('s')
        if time:
            seconds = time[0]
    else:
        print("commands go here")

if __name__ == "__main__":
    main()

