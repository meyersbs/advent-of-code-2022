import copy
import re
import sys
RE_ALPHA = re.compile("[^0-9 ]")
RE_SPACES = re.compile("\s+")
RE_COLUMNS = re.compile("[\[\]\s]")
data, columns, columns1, columns2, rules = [], [], [], [], []
with open(sys.argv[1], "r") as f:
    for line in f.readlines(): data.append(line.strip("\n"))
for i in range(0, data.index("")-1):
    col = [ RE_COLUMNS.sub("", data[i][c:c+4]) for c in range(0, len(data[i]), 4) ]
    columns.append([ "-" if c=="" else c for c in col ])
for i in range(data.index("")+1, len(data)):
    rules.append([int(r) for r in RE_SPACES.sub(" ", RE_ALPHA.sub("", data[i]).strip()).split(" ")])
columns1 = [ [] for c in range(0, len(columns[0])) ]
for r in range(len(columns)-1, -1, -1):
    for c in range(0, len(columns[0])):
        if columns[r][c] != "-": columns1[c].append(columns[r][c])
columns2 = copy.deepcopy(columns1)
for rule in rules:
    crates = list()
    for i in range(0, rule[0]):
        columns1[rule[2]-1].append(columns1[rule[1]-1].pop(-1))
        crates.append(columns2[rule[1]-1].pop(-1))
    crates.reverse()
    for crate in crates: columns2[rule[2]-1].append(crate)
print("Top Crates: {}".format("".join([ col[-1] for col in columns1 ])))
print("Top Crates: {}".format("".join([ col[-1] for col in columns2 ])))
