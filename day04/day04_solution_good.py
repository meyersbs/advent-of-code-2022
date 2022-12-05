#!/usr/bin/env python3


#### IMPORTS #######################################################################################
import sys


#### GLOBALS #######################################################################################


#### CLASSES #######################################################################################


#### FUNCTIONS #####################################################################################
def _expandSection(section):
    sec = list()
    endpoint = section.split("-")
    for i in range(int(endpoint[0]), int(endpoint[1])+1):
        sec.append(i)

    return sec


def _readData(filepath):
    """
    Read in the data
    """
    data = list()
    with open(filepath, "r") as f:
        for line in f.readlines():
            # Split section assignments
            sections = line.strip("\n").split(",")
            # Expand section assignments
            section_a = _expandSection(sections[0])
            section_b = _expandSection(sections[1])
            # Update data list
            data.append([section_a, section_b])

    return data


def _countFullOverlaps(data):
    """
    Count full overlaps (if one section fully contains the other).
    """
    overlaps = 0
    for pair in data:
        # If the first section contains the second section
        if pair[0][0] <= pair[1][0] and pair[0][-1] >= pair[1][-1]:
            overlaps += 1
        # If the second section contains the first section
        elif pair[1][0] <= pair[0][0] and pair[1][-1] >= pair[0][-1]:
            overlaps += 1

    return overlaps


def _countSemiOverlaps(data):
    """
    Count semi overlaps (if there is any overlap in section assignments).
    """
    overlaps = 0
    for pair in data:
        # If the length of the set intersection for each section is not zero
        if len(list(set(pair[0]).intersection(set(pair[1])))) != 0:
            overlaps += 1

    return overlaps


#### MAIN ##########################################################################################
if __name__ == "__main__":
    # Get filepath
    args = sys.argv[1:]
    filepath = args[0]

    # Read data
    data = _readData(filepath)
    
    # Part 1
    overlaps = _countFullOverlaps(data)
    print("Full Overlaps: {}".format(overlaps))

    # Part 2
    overlaps = _countSemiOverlaps(data)
    print("Semi Overlaps: {}".format(overlaps))
