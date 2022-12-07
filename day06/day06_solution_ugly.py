import sys
def _findMarker(data, size):
    for i in range(size, len(data)):
        if len(set(data[i-size:i])) == size: return i
with open(sys.argv[1], "r") as f:
    data = [ c for c in f.readline().strip("\n") ]
    print("Signal Start Index: {}".format(_findMarker(data, 4)))
    print("Message Start Index: {}".format(_findMarker(data, 14)))
