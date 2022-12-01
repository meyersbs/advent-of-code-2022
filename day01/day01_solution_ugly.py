import sys
ELVES = [0]
with open(sys.argv[1], "r") as f:
    for line in f.readlines():
        if line.strip("\n") != "": ELVES[-1] += int(line.strip("\n"))
        else: ELVES.append(0)
ELVES.sort(reverse=True)
print("Part 1: {}".format(sum(ELVES[:1])))
print("Part 2: {}".format(sum(ELVES[:int(sys.argv[2])])))
