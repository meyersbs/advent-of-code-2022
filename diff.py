#!/usr/bin/env python3


#### IMPORTS #######################################################################################
import os
import subprocess
import sys
import time


#### GLOBALS #######################################################################################
DAYS = {
    "day01": {
        "good": "day01/day01_solution_good.py",
        "ugly": "day01/day01_solution_ugly.py",
        "args": ["day01/day01_input.txt", "3"]
    },
    "day02": {
        "good": "day02/day02_solution_good.py",
        "ugly": "day02/day02_solution_ugly.py",
        "args": ["day02/day02_input.txt"]
    },
    "day03": {},
    "day04": {},
    "day05": {},
    "day06": {},
    "day07": {},
    "day08": {},
    "day09": {},
    "day10": {},
    "day11": {},
    "day12": {},
    "day13": {},
    "day14": {},
    "day15": {},
    "day16": {},
    "day17": {},
    "day18": {},
    "day19": {},
    "day20": {},
    "day21": {},
    "day22": {},
    "day23": {},
    "day24": {},
    "day25": {}
}

#### CLASSES #######################################################################################


#### FUNCTIONS #####################################################################################
def _loc(filepath):
    return sum(1 for line in open(filepath, "r"))


def _sloc(filepath):
    sloc = 0
    with open(filepath, "r") as f:
        for line in f.readlines():
            l = line.lstrip().rstrip().strip("\n")
            if l != "":
                if l[0] != "#":
                    sloc += 1

    return sloc


def _size(filepath):
    return os.path.getsize(filepath)


def _runOnce(args):
    time_start = time.time()
    subprocess.call(args, stdout=subprocess.DEVNULL)
    time_stop = time.time()

    return time_stop - time_start


def _runNTimes(filepath, file_args, n):
    runtimes = list()

    args = ["python3", filepath]
    if file_args is not None:
        args.extend(file_args)

    for i in range(0, n):
        t = _runOnce(args)
        runtimes.append(t)

    return sum(runtimes) / len(runtimes)


#### MAIN ##########################################################################################
if __name__ == "__main__":
    day = DAYS[sys.argv[1]]

    good_loc = _loc(day["good"])
    ugly_loc = _loc(day["ugly"])
    print("Good LOC: {}".format(good_loc))
    print("Ugly LOC: {}".format(ugly_loc))

    good_sloc = _sloc(day["good"])
    ugly_sloc = _sloc(day["ugly"])
    print("Good SLOC: {}".format(good_sloc))
    print("Ugly SLOC: {}".format(ugly_sloc))

    good_kb = _size(day["good"])
    ugly_kb = _size(day["ugly"])
    print("Good Size: {}b".format(good_kb))
    print("Ugly Size: {}b".format(ugly_kb))

    good_10 = _runNTimes(day["good"], day["args"], 10)
    ugly_10 = _runNTimes(day["ugly"], day["args"], 10)
    print("Good Average ({} Runs): {} secs".format(10, good_10))
    print("Ugly Average ({} Runs): {} secs".format(10, ugly_10))

    good_100 = _runNTimes(day["good"], day["args"], 100)
    ugly_100 = _runNTimes(day["ugly"], day["args"], 100)
    print("Good Average ({} Runs): {} secs".format(100, good_100))
    print("Ugly Average ({} Runs): {} secs".format(100, ugly_100))

    good_1000 = _runNTimes(day["good"], day["args"], 1000)
    ugly_1000 = _runNTimes(day["ugly"], day["args"], 1000)
    print("Good Average ({} Runs): {} secs".format(1000, good_1000))
    print("Ugly Average ({} Runs): {} secs".format(1000, ugly_1000))

    print("----------")

    print("LOC Diff: {}".format(good_loc - ugly_loc))
    print("SLOC Diff: {}".format(good_sloc - ugly_sloc))
    print("size Diff: {}b".format(good_kb - ugly_kb))
    print("10 Runs Diff: {} secs".format(good_10 - ugly_10))
    print("100 Runs Diff: {} secs".format(good_100 - ugly_100))
    print("1000 Runs Diff: {} secs".format(good_1000 - ugly_1000))

