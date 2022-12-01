#!/usr/bin/env python3

import os
import sys

ELVES = list()

def _readData(filepath):
    data = list()
    with open(filepath, "r") as f:
        for line in f.readlines():
            data.append(line.strip("\n"))

    return data

def _makeElves(raw_data):
    calories = 0
    for line in raw_data:
        if line != "":
            calories += int(line)
        else:
            ELVES.append(calories)
            calories = 0

def _getFattestNElves(n):
    ELVES.sort(reverse=True)
    return sum(ELVES[:n])

if __name__ == "__main__":
    args = sys.argv[1:]
    _makeElves(_readData(args[0]))
    print("Fattest Elf: {} Calories".format(_getFattestNElves(1)))
    print("{} Fattest Elves: {} Calories".format(int(args[1]), _getFattestNElves(int(args[1]))))
    

