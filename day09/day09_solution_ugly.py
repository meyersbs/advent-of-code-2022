import sys
MOVE_MAP ={ "R": [0, 1], "L": [0, -1], "U": [1, 1], "D": [1, -1] } 
def _isTouching(t, h): return (abs(t[0] - h[0]) in [0, 1]) and (abs(t[1] - h[1]) in [0, 1])
def _move(rope, direction): rope[MOVE_MAP[direction][0]] += MOVE_MAP[direction][1]
def _completeMove(visited, rps, direction, count):
    for c in range(count):
        for r in range(len(rps)):
            if r == 0: _move(rps[r], direction)
            elif not _isTouching(rps[r], rps[r-1]):
                if rps[r][1] != rps[r-1][1]: _move(rps[r], "U" if rps[r][1] < rps[r-1][1] else "D")
                if rps[r][0] != rps[r-1][0]: _move(rps[r], "R" if rps[r][0] < rps[r-1][0] else "L")
            if [rps[-1][0], rps[-1][1]] not in visited: visited.append([rps[-1][0], rps[-1][1]])
with open(sys.argv[1], "r") as f:
    moves = [ line.strip("\n").split(" ") for line in f.readlines() ]
visited, ropes = list(), [ [0, 0] for i in range(0, 2) ]
[ _completeMove(visited, ropes, move[0], int(move[1])) for move in moves ]
print("# Positions: {}".format(len(visited)))
visited, ropes = list(), [ [0, 0] for i in range(0, 10) ]
[ _completeMove(visited, ropes, move[0], int(move[1])) for move in moves ]
print("# Positions: {}".format(len(visited)))
