import sys
def _max(ls): return max(ls, default=-1)
def _score(ls, tree):
    score = 0
    for i in ls:
        score += 1
        if i >= tree: break
    return score
forest = list()
with open(sys.argv[1], "r") as f:
    for line in f.readlines(): forest.append([ int(r) for r in line.strip("\n") ])
visible, scores = 0, list()
for x in range(0, len(forest[0])):
    for y in range(0, len(forest)):
        tree = forest[x][y]
        l = list(reversed([ forest[x][j] for j in range(0, y) ]))
        r = [ forest[x][j] for j in range(y+1, len(forest)) ]
        u = list(reversed([ forest[i][y] for i in range(0, x) ]))
        d = [ forest[i][y] for i in range(x+1, len(forest[0])) ]
        if _max(l) < tree or _max(r) < tree or _max(u) < tree or _max(d) < tree: visible += 1
        scores.append(_score(l, tree) * _score(r, tree) * _score(u, tree) * _score(d, tree))
print("Visible Trees: {}".format(visible))
print("Max Scenic Score: {}".format(max(scores)))
