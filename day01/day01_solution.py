#!/usr/bin/env python3


#### IMPORTS #######################################################################################
import os
import sys


#### GLOBALS #######################################################################################
ELVES = list()


#### CLASSES #######################################################################################
class Food:
    def __init__(self, food_list):
        self.food_list = food_list
        self.calories = sum(food_list)


    def __str__(self):
        return "{}: {}".format(self.calories, self.food_list)


class Elf:
    def __init__(self, name, food_list):
        self.name = name
        self.food = Food(food_list)


    def __str__(self):
        return "{}: {}".format(self.name, self.food)


#### FUNCTIONS #####################################################################################
def _readData(filepath):
    data = list()
    with open(filepath, "r") as f:
        for line in f.readlines():
            data.append(line.strip("\n"))

    return data


def _makeElves(raw_data):
    count = 0
    temp_food_list = list()
    for line in raw_data:
        if line != "":
            temp_food_list.append(int(line))
        else:
            temp_elf = Elf(count, temp_food_list)
            ELVES.append(temp_elf)
            count += 1
            temp_food_list = list()


def _getFattestElf():
    fattest_elf = 0
    for elf in ELVES:
        if elf.food.calories > fattest_elf:
            fattest_elf = elf.food.calories

    return fattest_elf


def _getFattestNElves(n):
    calories = list()
    for elf in ELVES:
        calories.append(elf.food.calories)

    calories.sort(reverse=True)
    
    top_n_calories = 0
    for i in range(0, n):
        top_n_calories += calories[i]

    return top_n_calories


#### MAIN ##########################################################################################
if __name__ == "__main__":
    args = sys.argv[1:]
    filepath = args[0]
    raw_data = _readData(filepath)
    _makeElves(raw_data)

    # Part 1
    fattest_elf = _getFattestElf()
    print("Fattest Elf: {} Calories".format(fattest_elf))

    # Part 2
    top_n_calories = _getFattestNElves(int(args[1]))
    print("Three Fattest Elves: {} Calories".format(top_n_calories))
    

