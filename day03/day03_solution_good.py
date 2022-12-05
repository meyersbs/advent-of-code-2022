#!/usr/bin/env python3


#### IMPORTS #######################################################################################
import sys


#### GLOBALS #######################################################################################
PRIORITY_MAP = {
    "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11,
    "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21,
    "v": 22, "w": 23, "x": 24, "y": 25, "z": 26, "A": 27, "B": 28, "C": 29, "D": 30, "E": 31,
    "F": 32, "G": 33, "H": 34, "I": 35, "J": 36, "K": 37, "L": 38, "M": 39, "N": 40, "O": 41,
    "P": 42, "Q": 43, "R": 44, "S": 45, "T": 46, "U": 47, "V": 48, "W": 49, "X": 50, "Y": 51,
    "Z": 52
}


#### CLASSES #######################################################################################
class Group:
    """
    Group object.
    """
    def __init__(self, rucksacks):
        """
        Groups contain three rucksacks.
        """
        self.rucksacks = [Rucksack(r) for r in rucksacks]


    def getShared(self):
        """
        Get the shared item across all three rucksacks.
        """
        contents = [r.contents for r in self.rucksacks]
        shared = set(contents[0])
        for c in contents[1:]:
            shared.intersection_update(c)

        return list(shared)[0]


class Rucksack:
    """
    Rucksack object.
    """
    def __init__(self, contents):
        """
        Rucksacks contain a list of contents, a left compartment, and a right compartment.
        """
        self.contents = [c for c in contents]
        self.left_compartment = self.contents[:len(self.contents)//2]
        self.right_compartment = self.contents[len(self.contents)//2:]


    def getShared(self):
        """
        Get the shared item across the two compartments.
        """
        left_set = set(self.left_compartment)
        right_set = set(self.right_compartment)

        return list(left_set & right_set)[0]


#### FUNCTIONS #####################################################################################
def _readData(filepath):
    """
    Read in the data.
    """
    data = list()
    with open(filepath, "r") as f:
        for line in f.readlines():
            data.append(line.strip("\n"))

    return data


def _getPriorities(rucksacks):
    """
    Get a list of priorities for each rucksack.
    """
    priorities = list()
    for sack in rucksacks:
        priorities.append(PRIORITY_MAP[sack.getShared()])

    return priorities


def _getGroups(data, group_size):
    """
    Get a list of groups of three.
    """
    return [data[pos:pos + group_size] for pos in range(0, len(data), group_size)]


def _makeGroups(data):
    """
    Create group objects.
    """
    groups = list()
    temp_groups = _getGroups(data, 3)
    for group in temp_groups:
        groups.append(Group(group))

    return groups


#### MAIN ##########################################################################################
if __name__ == "__main__":
    args = sys.argv[1:]
    filepath = args[0]

    # Read data
    raw_data = _readData(filepath)

    # Part 1
    rucksacks = list()
    for row in raw_data:
        rucksacks.append(Rucksack(row))
    priorities = _getPriorities(rucksacks)
    sum_priorities = sum(priorities)
    print("Priority Sum: {}".format(sum_priorities))

    # Part 2
    groups = _makeGroups(raw_data)
    priorities = list()
    for group in groups:
        badge = group.getShared()
        priorities.append(PRIORITY_MAP[badge])
    sum_priorities = sum(priorities)
    print("Badge Priority Sum: {}".format(sum_priorities))
