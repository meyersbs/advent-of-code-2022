#!/usr/bin/env python3


#### IMPORTS #######################################################################################
import re
import sys


#### GLOBALS #######################################################################################
RE_ALPHA = re.compile("[^0-9 ]")
RE_SPACES = re.compile("\s+")
RE_COLUMNS = re.compile("[\[\]\s]")


#### CLASSES #######################################################################################
class Shipyard:
    """
    Shipyard object.
    """
    def __init__(self, columns):
        """
        Shipyards contain a list of columns.
        """
        self.columns = self._makeColumns(columns)


    def _makeColumns(self, columns):
        """
        Rearrange the columns to actually be columns so my brain doesn't hurt so much.
        """
        temp_columns = [ [] for c in range(0, len(columns[0])) ]

        # In reverse order through the list of rows
        for r in range(len(columns)-1, -1, -1):
            # In forward order through each row element
            for c in range(0, len(columns[0])):
                # If there is actually a crate
                if columns[r][c] != "-":
                    # Add the crate to the column
                    temp_columns[c].append(columns[r][c])
        
        return temp_columns


    def moveCrates(self, num_crates, src_column, dest_column, crane_version):
        """
        Move crates according to the given rule.
        """
        # For Part 1
        if crane_version == 9000:
            # For each crate
            for i in range(0, num_crates):
                # Pick up the crate from the source column
                crate = self.columns[src_column-1].pop(-1)
                # Put the crate in the destination column
                self.columns[dest_column-1].append(crate)
        # For Part 2
        elif crane_version == 9001:
            crates_list = list()
            # For each crate
            for i in range(0, num_crates):
                # Grab the crates and move them to the side
                crate = self.columns[src_column-1].pop(-1)
                crates_list.append(crate)

            # Reverse the order of the crates we set to the side
            crates_list.reverse()
            for crate in crates_list:
                # Put the crates in the destination column
                self.columns[dest_column-1].append(crate)


    def getTopCrates(self):
        """
        Get a string representation of the crates on top of each column.
        """
        tops = [ col[-1] for col in self.columns ]
        return "".join(tops)



#### FUNCTIONS #####################################################################################
def _readData(filepath):
    """
    Read in the input data.
    """
    data = list()
    with open(filepath, "r") as f:
        for line in f.readlines():
            data.append(line.strip("\n")) # Strip newlines

    return data


def _parseData(data):
    """
    Parse the input data into columns and rules.
    """
    columns = list()
    rules = list()

    # Find the empty line denoting the end of the columns and beginning of the rules
    break_index = data.index("")

    # For each line until the empty line, grab the columns
    for i in range(0, break_index-1):
        column = data[i]
        # Split the line into 4 character chunks, removing square brackets and spaces
        column = [ RE_COLUMNS.sub("", column[i:i+4]) for i in range(0, len(column), 4) ]
        # Give a marker to empty crates
        column = [ "-" if c=="" else c for c in column ]
        columns.append(column)

    # For each line after the empty line, grab the rules
    for i in range(break_index+1, len(data)):
        # Remove non-numeric characters
        rule = RE_ALPHA.sub("", data[i]).rstrip().lstrip()
        # Remove duplicate whitespace
        rule = RE_SPACES.sub(" ", rule)
        # Convert values to ints
        rule = [ int(r) for r in rule.split(" ") ]
        rules.append(rule)

    return columns, rules


#### MAIN ##########################################################################################
if __name__ == "__main__":
    args = sys.argv[1:]

    # Read data
    filepath = args[0]
    data = _readData(filepath)

    # Parse data
    columns, rules = _parseData(data)
    
    # Part 1
    shipyard = Shipyard(columns)
    for rule in rules:
        shipyard.moveCrates(rule[0], rule[1], rule[2], 9000)
    tops = shipyard.getTopCrates()
    print("Top Crates: {}".format(tops))

    # Part 2
    shipyard = Shipyard(columns)
    for rule in rules:
        shipyard.moveCrates(rule[0], rule[1], rule[2], 9001)
    tops = shipyard.getTopCrates()
    print("Top Crates: {}".format(tops))
