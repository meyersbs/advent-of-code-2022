#!/usr/bin/env python3


#### IMPORTS #######################################################################################
import sys


#### GLOBALS #######################################################################################


#### CLASSES #######################################################################################
class Forest:
    """
    Forest object.
    """
    def __init__(self, data):
        """
        Forests have a grid of trees w/ upper and lower bounds, a list of visible trees, and a list
        of scenic scores for trees.
        """
        self.grid = self._makeGrid(data)
        self.row_bound = len(self.grid)
        self.col_bound = len(self.grid[0])
        self.visible_trees, self.scenic_scores = self._processTrees()


    def _makeGrid(self, data):
        """
        Create grid of trees by splitting rows by character.
        """
        grid = list()
        for row in data:
            grid.append([ int(r) for r in row ])

        return grid


    def _processTrees(self):
        """
        Process the trees to get a list of visible trees and a list of scenic scores.
        """
        scores = list()
        visible = list()
        for c in range(0, self.col_bound):
            for r in range(0, self.row_bound):
                # Get current tree
                tree = self.grid[c][r]

                # Get left, right, up, and down from current tree
                left = [ self.grid[c][j] for j in range(0, r) ]
                right = [ self.grid[c][j] for j in range(r+1, self.row_bound) ]
                up = [ self.grid[i][r] for i in range(0, c) ]
                down = [self.grid[i][r] for i in range(c+1, self.col_bound) ]

                # Determine if current tree is visible
                if max(left, default=-1) < tree or max(right, default=-1) < tree or \
                        max(up, default=-1) < tree or max(down, default=-1) < tree:
                    visible.append([c, r])

                # Left score
                left_score = 0
                left.reverse()
                for j in left:
                    left_score += 1
                    if j >= tree:
                        break

                # Right score
                right_score = 0
                for j in right:
                    right_score += 1
                    if j >= tree:
                        break

                # Up score
                up_score = 0
                up.reverse()
                for i in up:
                    up_score += 1
                    if i >= tree:
                        break

                # Down score
                down_score = 0
                for i in down:
                    down_score += 1
                    if i >= tree:
                        break

                # Update scores
                scores.append(left_score * right_score * up_score * down_score)

        return visible, scores


#### FUNCTIONS #####################################################################################
def _readData(filepath):
    """
    Read in data, stripping newlines.
    """
    with open(filepath, "r") as f:
        data = [ line.strip("\n") for line in f.readlines() ]

    return data


#### MAIN ##########################################################################################
if __name__ == "__main__":
    args = sys.argv[1:]
    
    # Read data
    filepath = args[0]
    data = _readData(filepath)

    # Make grid
    forest = Forest(data)

    # Part 1
    visible_count = len(forest.visible_trees)
    print("Visible Trees: {}".format(visible_count))

    # Part 2
    scenic_score = max(forest.scenic_scores)
    print("Max Scenic Score: {}".format(scenic_score))

