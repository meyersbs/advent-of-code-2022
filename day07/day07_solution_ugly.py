#!/usr/bin/env python3


#### IMPORTS #######################################################################################
import sys


#### GLOBALS #######################################################################################


#### CLASSES #######################################################################################
class Node:
    """
    Node object.
    """
    def __init__(self, name, parent, size=0):
        """
        Nodes have a name, a parent, a list of children, and a size.
        """
        self.name = name
        self.parent = parent
        self.children = list()
        self.size = int(size)


class Tree:
    """
    Tree object.
    """
    def __init__(self):
        """
        Trees have a root node, a pwd, and a list of subdirectories.
        """
        self.root = Node("/", None)
        self.pwd = self.root
        self.directories = list()


    def addNode(self, name, size=0):
        """
        Add a node to the tree.
        """
        # If node is a directory
        if size == 0:
            # Create node
            node = Node(name, self.pwd)
            # Update tree
            self.pwd.children.append(node)
            self.directories.append(node)
            # Set pwd
            self.pwd = node
        # If node is a file
        else:
            # Create node
            node = Node(name, self.pwd, size)
            # Update tree
            self.pwd.children.append(node)


    def cdUp(self):
        """
        Simulate `$ cd ..`
        """
        self.pwd = self.pwd.parent


    def updateSizes(self):
        """
        Update size of immediate children nodes.
        """
        for child in self.root.children:
            self.root.size += self._updateChildrenSizes(child)


    def _updateChildrenSizes(self, node):
        """
        Update size of children nodes recursively.
        """
        for child in node.children:
            node.size += self._updateChildrenSizes(child)

        return node.size


#### FUNCTIONS #####################################################################################
def _readData(filepath):
    """
    Read in input data, removing newlines and `ls` lines.
    """
    data = list()
    with open(filepath, "r") as f:
        for line in f.readlines():
            if not line.startswith("$ ls"):
                data.append(line.strip("\n"))

    return data


def _makeNodes(tree, data):
    """
    Parse the input into a tree structure.
    """
    for line in data:
        # cd line
        if line[0] == "$":
            directory = line.split()[-1]
            if directory == "..":
                tree.cdUp()
            else:
                tree.addNode(directory)
        # file/dir line
        else:
            size, name = line.split()
            if size != "dir":
                tree.addNode(name, int(size))


def _sumSizes(directories, cutoff):
    """
    Get the sum of all directory sizes (duplicates included) less than the cutoff.
    """
    size_sum = 0
    for d in directories:
        if d.size <= cutoff:
            size_sum += d.size

    return size_sum


def _findDirToDelete(tree, disk_size, unused_needed):
    """
    Find the smallest directory we can delete to free up space.
    """
    dirs = list()
    unused = disk_size - tree.root.size
    missing = unused_needed - unused
    for d in tree.directories:
        if d.size >= missing:
            dirs.append(d.size)

    return min(dirs)


#### MAIN ##########################################################################################
if __name__ == "__main__":
    args = sys.argv[1:]

    # Read data
    filepath = args[0]
    data = _readData(filepath)

    # Make filesystem
    tree = Tree()
    _makeNodes(tree, data)
    tree.updateSizes()

    # Part 1
    size = _sumSizes(tree.directories, 100000)
    print("Sum <= 100000: {}".format(size))

    # Part 2
    size = _findDirToDelete(tree, 70000000, 30000000)
    print("Smallest Dir Size: {}".format(size))
