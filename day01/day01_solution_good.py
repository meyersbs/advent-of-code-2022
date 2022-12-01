#!/usr/bin/env python3


#### IMPORTS #######################################################################################
import sys


#### GLOBALS #######################################################################################
ELVES = list()


#### CLASSES #######################################################################################
class Food:
    """
    You plan to eat how much?
    """
    def __init__(self, food_list):
        """
        Food objects have a list of calories for each food item and a total number of calories.
        """
        self.food_list = food_list
        self.calories = sum(food_list)


class Elf:
    """
    Just a friendly elf.
    """
    def __init__(self, name, food_list):
        """
        Elves have a name (which is actually just a number) and a Food object.
        """
        self.name = name
        self.food = Food(food_list)


#### FUNCTIONS #####################################################################################
def _readData(filepath):
    """
    Read in the input data, stripping newlines.
    """
    data = list()
    with open(filepath, "r") as f:
        for line in f.readlines():
            data.append(line.strip("\n"))

    return data


def _makeElves(raw_data):
    """
    Parse the input data to create elves.
    """
    count = 0
    temp_food_list = list()
    for line in raw_data:
        # If not a new elf
        if line != "":
            # Add their food to the list
            temp_food_list.append(int(line))
        # If new elf
        else:
            # Create old elf
            temp_elf = Elf(count, temp_food_list)
            ELVES.append(temp_elf)
            # Start over
            count += 1
            temp_food_list = list()


def _getFattestNElves(n):
    """
    Get the total calories of the N fattest elves.
    """
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

    if len(args) < 2:
        sys.exit("Usage: python3 day01_solution_good.py <input_filepath> <n>")

    filepath = args[0]
    n = int(args[1])

    raw_data = _readData(filepath)
    _makeElves(raw_data)

    # Part 1
    fattest_elf = _getFattestNElves(1)
    print("Fattest Elf: {} Calories".format(fattest_elf))

    # Part 2
    top_n_calories = _getFattestNElves(n)
    print("Three Fattest Elves: {} Calories".format(top_n_calories))
