#!/usr/bin/env python3

import sys

ELVES = list()

if __name__ == "__main__":
    args = sys.argv[1:]
    with open(args[0], "r") as f:
        raw_data = [line.strip("\n") for line in f.readlines()]
    
    calories = 0
    for line in raw_data:
        if line != "":
            calories += int(line)
        else:
            ELVES.append(calories)
            calories = 0

    ELVES.sort(reverse=True)
    print("Fattest Elf: {} Calories".format(sum(ELVES[:1])))
    print("{} Fattest Elves: {} Calories".format(int(args[1]), sum(ELVES[:int(args[1])])))
