import sys
class Node:
    def __init__(self, name, parent, size=0):
        self.name = name
        self.parent = parent
        self.children = list()
        self.size = int(size)
class Tree:
    def __init__(self):
        self.root = Node("/", None)
        self.pwd = self.root
        self.directories = list()
    def addNode(self, name, size=0):
        if size == 0:
            node = Node(name, self.pwd)
            self.pwd.children.append(node)
            self.directories.append(node)
            self.pwd = node
        else:
            node = Node(name, self.pwd, size)
            self.pwd.children.append(node)
    def cdUp(self): self.pwd = self.pwd.parent
    def updateSizes(self):
        for child in self.root.children: self.root.size += self._updateChildrenSizes(child)
    def _updateChildrenSizes(self, node):
        for child in node.children: node.size += self._updateChildrenSizes(child)
        return node.size
tree = Tree()
with open(sys.argv[1], "r") as f:
    data = [ line.strip("\n") for line in f.readlines() if not line.startswith("$ ls") ]
for line in data:
    if line[0] == "$":
        if line.split()[-1] == "..": tree.cdUp()
        else: tree.addNode(line.split()[-1])
    else:
        if line.split()[0] != "dir": tree.addNode(line.split()[1], int(line.split()[0]))
tree.updateSizes()
size_sum = 0
for d in tree.directories:
    if d.size <= 100000: size_sum += d.size
print("Sum <= 100000: {}".format(size_sum))
dirs = list()
for d in tree.directories:
    if d.size >= 30000000 - (70000000 - tree.root.size): dirs.append(d.size)
print("Smallest Dir Size: {}".format(min(dirs)))
