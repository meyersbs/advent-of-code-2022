#!/usr/bin/env python3


#### IMPORTS #######################################################################################
import sys


#### GLOBALS #######################################################################################


#### CLASSES #######################################################################################


#### FUNCTIONS #####################################################################################
def _readData(filepath):
    """
    Read data from disk, removing newlines.
    """
    data = list()
    with open(filepath, "r") as f:
        for line in f.readlines():
            # Split line into list of characters
            line_split = [ c for c in line.strip("\n") ]
            data.extend(line_split)

    return data


def _findSignal(data):
    # Start at the fourth character
    for i in range(4, len(data)):
        curr = data[i-4:i]
        # If there are duplicate characters
        if len(curr) != len(set(curr)):
            pass
        # We found the signal
        else:
            return i

def _findMessage(data):
    # Start at the 14th character
    for i in range(14, len(data)):
        curr = data[i-14:i]
        # If there are duplicate characters
        if len(curr) != len(set(curr)):
            pass
        # We found the message
        else:
            return i


#### MAIN ##########################################################################################
if __name__ == "__main__":
    args = sys.argv[1:]

    # Read data
    filepath = args[0]
    data = _readData(filepath)

    # Part 1
    signal_index = _findSignal(data)
    print("Signal Start Index: {}".format(signal_index))

    # Part 2
    message_index = _findMessage(data)
    print("Message Start Index: {}".format(message_index))
