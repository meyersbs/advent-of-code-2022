#!/usr/bin/env python3


#### IMPORTS #######################################################################################
import sys


#### GLOBALS #######################################################################################


#### CLASSES #######################################################################################


#### FUNCTIONS #####################################################################################
def _readData(filepath):
    """
    Read in the input data, stripping newlines.
    """
    data = list()
    with open(filepath, "r") as f:
        for line in f.readlines():
            temp_line = line.strip("\n").split(" ")
            data.append([temp_line[0], int(temp_line[1])])

    return data


def _isTouching(tail, head):
    """
    Determine if the head and tail are touching.
    """
    return (abs(tail[0] - head[0]) in [0, 1]) and (abs(tail[1] - head[1]) in [0, 1])


def _move(rope, direction):
    """
    Update the tail count based on direction.
    """
    if direction == "R":
        rope[0] += 1
    elif direction == "L":
        rope[0] -= 1
    elif direction == "U":
        rope[1] += 1
    elif direction == "D":
        rope[1] -= 1


def _completeMove(visited, ropes, direction, count):
    """
    Complete a single move for every rope.
    """
    # For however many moves
    for c in range(count):
        # For each rope
        for r in range(len(ropes)):
            # If this is the first rope, update the head
            if r == 0:
                _move(ropes[r], direction)
            # If the head and tail for this rope and the previous rope aren't touching
            elif not _isTouching(ropes[r], ropes[r-1]):
                # Move vertically
                if ropes[r][1] != ropes[r-1][1]:
                    vertical = "D"
                    if ropes[r][1] < ropes[r-1][1]:
                        vertical = "U"
                    _move(ropes[r], vertical)
                # Move horizontally
                if ropes[r][0] != ropes[r-1][0]:
                    horizontal = "L"
                    if ropes[r][0] < ropes[r-1][0]:
                        horizontal = "R"
                    _move(ropes[r], horizontal)
            # Update the list of visits with the last tail
            if [ ropes[-1][0], ropes[-1][1] ] not in visited:
                visited.append([ ropes[-1][0], ropes[-1][1] ])



#### MAIN ##########################################################################################
if __name__ == "__main__":
    args = sys.argv[1:]

    # Read data
    filepath = args[0]
    moves = _readData(filepath)
    
    # Part 1
    visited = list()
    ropes = [ [0, 0], [0, 0] ]
    for move in moves:
        _completeMove(visited, ropes, move[0], move[1])
    print("# Positions: {}".format(len(visited)))


    # Part 2
    visited = list()
    ropes = [ [0, 0] for i in range(0, 10) ]
    for move in moves:
        _completeMove(visited, ropes, move[0], move[1])
    print("# Positions: {}".format(len(visited)))
