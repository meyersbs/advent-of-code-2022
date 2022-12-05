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
- If one solution is serial, the other must be as well. Same goes for parallel.
- Lines must be no more than 100 characters; multiple statements on the same line with `;` is not allowed.

## Testing

Both solutions will be tested using the `diff.py` script that I wrote, which outputs the following for each solution:

- Number of lines of code
- Number of significant lines of code (ignore spaces and comment lines)
- Number of bytes
- Average runtime of 10 runs
- Average runtime of 100 runs
- Average runtime of 1000 runs

### Environment

Benchmarks will be run on the same machine with the following specs:

- **Machine:** Lenovo ThinkPad T14s Gen 3 AMD
- **OS:** RHEL 9.1 64-bit
- **RAM:** 32GB LPDDR5-6400MHz (Soldered)
- **CPU:** AMD Ryzen 7 PRO 6850U
- **GPU:** Integrated AMD Radeon 680M
- **Python:** Python 3.9.14

## Results

### day01

```
$ python3 diff.py day01

Good LOC: 107
Ugly LOC: 9
Good SLOC: 69
Ugly SLOC: 9
Good Size: 2698 bytes
Ugly Size: 314 bytes
Good Average (10 Runs): 0.008161807060241699 secs
Ugly Average (10 Runs): 0.007584166526794433 secs
Good Average (100 Runs): 0.008351330757141113 secs
Ugly Average (100 Runs): 0.00788471221923828 secs
Good Average (1000 Runs): 0.008363399028778076 secs
Ugly Average (1000 Runs): 0.007947054386138916 secs
----------
LOC Diff: 98
SLOC Diff: 60
size Diff: 2384 bytes
10 Runs Diff: 0.0005776405334472655 secs
100 Runs Diff: 0.0004666185379028319 secs
1000 Runs Diff: 0.0004163446426391597 secs
```

### day02

```
$ python3 diff.py day02

Good LOC: 216
Ugly LOC: 20
Good SLOC: 139
Ugly SLOC: 20
Good Size: 5468 bytes
Ugly Size: 1025 bytes
Good Average (10 Runs): 0.01151123046875 secs
Ugly Average (10 Runs): 0.00920562744140625 secs
Good Average (100 Runs): 0.011668229103088379 secs
Ugly Average (100 Runs): 0.009198606014251709 secs
Good Average (1000 Runs): 0.011655337333679199 secs
Ugly Average (1000 Runs): 0.009312718629837036 secs
----------
LOC Diff: 196
SLOC Diff: 119
size Diff: 4443 bytes
10 Runs Diff: 0.0023056030273437503 secs
100 Runs Diff: 0.0024696230888366696 secs
1000 Runs Diff: 0.002342618703842163 secs
```

### day03

```
$ python3 diff.py day03

Good LOC: 132
Ugly LOC: 14
Good SLOC: 93
Ugly SLOC: 14
Good Size: 3650 bytes
Ugly Size: 835 bytes
Good Average (10 Runs): 0.010353922843933105 secs
Ugly Average (10 Runs): 0.00890953540802002 secs
Good Average (100 Runs): 0.010407536029815674 secs
Ugly Average (100 Runs): 0.008786406517028809 secs
Good Average (1000 Runs): 0.010371868133544921 secs
Ugly Average (1000 Runs): 0.008914975166320801 secs
----------
LOC Diff: 118
SLOC Diff: 79
size Diff: 2815 bytes
10 Runs Diff: 0.0014443874359130852 secs
100 Runs Diff: 0.0016211295127868657 secs
1000 Runs Diff: 0.0014568929672241198 secs
```
