# advent-of-code-2022

## Goal

My goal here is to implement two solutions: good and ugly. The **good** solution will have proper code comments and use classes/functions when necessary; it should pass an intro level software engineering course. The **ugly** solution is intended to have as few lines as possible; readability doesn't matter.

## Why?

To answer a seemingly simple question: *What is the cost of readability?*

## Guidelines

- Both solutions must be implemented in python.
- Both solutions must use **only** builtin python libraries.
- Both solutions must use at least one argument (the input file).
- Both solutions must take in the same command line arguments.

## Testing

Both solutions will be tested using the `diff.py` script that I wrote, which outputs the following for each solution:

- Number of lines of code
- Number of significant lines of code (ignore spaces and comment lines)
- Number of bytes
- Average runtime of 10 runs
- Average runtime of 100 runs
- Average runtime of 1000 runs

## Results

### day01

```
$ python3 diff.py day01

Good LOC: 107
Ugly LOC: 9
Good SLOC: 69
Ugly SLOC: 9
Good Size: 2698b
Ugly Size: 314b
Good Average (10 Runs): 0.025600290298461913 secs
Ugly Average (10 Runs): 0.02128894329071045 secs
Good Average (100 Runs): 0.022914206981658934 secs
Ugly Average (100 Runs): 0.021331090927124024 secs
Good Average (1000 Runs): 0.02264577293395996 secs
Ugly Average (1000 Runs): 0.020920952558517458 secs
----------
LOC Diff: 98
SLOC Diff: 60
size Diff: 2384b
10 Runs Diff: 0.004311347007751463 secs
100 Runs Diff: 0.0015831160545349103 secs
1000 Runs Diff: 0.001724820375442502 secs
```
