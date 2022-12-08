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
- Debugging code (e.g. print statements) must be removed from both solutions.

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

Notes:

- `day05`: The ugly solution takes ever so slightly longer than the good solution. My gut says that's a result of the deepcopy on Line 19.
- `day07`: The ugly solution is not as ugly as it could be. I absolutely could replace the two classes with horribly-ugly nested lists, but implementing that would give me a headache, so I'm not doing it.
- `day08`: Once again, the ugly solution takes longer than the good solution. I had to wrap the `max(...)` function on Line 2 to get a `default=-1`, which saved a lot of space on Line 20. Even still, I'm surprised the object-based solution outperformed the list-based solution, given that the object-based solution kind of just wraps around the same list structure.

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

### day04

```
$ python3 diff.py day04

Good LOC: 86
Ugly LOC: 13
Good SLOC: 47
Ugly SLOC: 13
Good Size: 2394 bytes
Ugly Size: 725 bytes
Good Average (10 Runs): 0.015279936790466308 secs
Ugly Average (10 Runs): 0.013196420669555665 secs
Good Average (100 Runs): 0.014889199733734131 secs
Ugly Average (100 Runs): 0.012997281551361085 secs
Good Average (1000 Runs): 0.01482330870628357 secs
Ugly Average (1000 Runs): 0.012953681707382201 secs
----------
LOC Diff: 73
SLOC Diff: 34
size Diff: 1669 bytes
10 Runs Diff: 0.002083516120910643 secs
100 Runs Diff: 0.0018919181823730466 secs
1000 Runs Diff: 0.0018696269989013688 secs
```

### day05

```
$ python3 diff.py day05

Good LOC: 150
Ugly LOC: 28
Good SLOC: 88
Ugly SLOC: 28
Good Size: 4738 bytes
Ugly Size: 1260 bytes
Good Average (10 Runs): 0.01407322883605957 secs
Ugly Average (10 Runs): 0.014457488059997558 secs
Good Average (100 Runs): 0.013995096683502198 secs
Ugly Average (100 Runs): 0.014390790462493896 secs
Good Average (1000 Runs): 0.014303854703903197 secs
Ugly Average (1000 Runs): 0.014884650230407715 secs
----------
LOC Diff: 122
SLOC Diff: 60
size Diff: 3478 bytes
10 Runs Diff: -0.0003842592239379876 secs
100 Runs Diff: -0.0003956937789916983 secs
1000 Runs Diff: -0.0005807955265045173 secs
```

### day06

```
$ python3 diff.py day06

Good LOC: 66
Ugly LOC: 8
Good SLOC: 33
Ugly SLOC: 8
Good Size: 1800 bytes
Ugly Size: 348 bytes
Good Average (10 Runs): 0.010797739028930664 secs
Ugly Average (10 Runs): 0.010644483566284179 secs
Good Average (100 Runs): 0.0107415771484375 secs
Ugly Average (100 Runs): 0.010459516048431396 secs
Good Average (1000 Runs): 0.010688895702362061 secs
Ugly Average (1000 Runs): 0.010569647550582886 secs
----------
LOC Diff: 58
SLOC Diff: 25
size Diff: 1452 bytes
10 Runs Diff: 0.00015325546264648507 secs
100 Runs Diff: 0.0002820611000061042 secs
1000 Runs Diff: 0.00011924815177917492 secs
```

### day07

```
$ python3 diff.py day07

Good LOC: 163
Ugly LOC: 45
Good SLOC: 110
Ugly SLOC: 45
Good Size: 4028 bytes
Ugly Size: 1634 bytes
Good Average (10 Runs): 0.010244131088256836 secs
Ugly Average (10 Runs): 0.01030113697052002 secs
Good Average (100 Runs): 0.010449507236480714 secs
Ugly Average (100 Runs): 0.010250954627990723 secs
Good Average (1000 Runs): 0.010330363750457764 secs
Ugly Average (1000 Runs): 0.010288910627365113 secs
----------
LOC Diff: 118
SLOC Diff: 65
size Diff: 2394 bytes
10 Runs Diff: -5.700588226318325e-05 secs
100 Runs Diff: 0.00019855260848999044 secs
1000 Runs Diff: 4.145312309265098e-05 secs
```

### day08

```
$ python3 diff.py day08

Good LOC: 124
Ugly LOC: 23
Good SLOC: 78
Ugly SLOC: 23
Good Size: 3749 bytes
Ugly Size: 968 bytes
Good Average (10 Runs): 0.14207961559295654 secs
Ugly Average (10 Runs): 0.1543668746948242 secs
Good Average (100 Runs): 0.14473127126693724 secs
Ugly Average (100 Runs): 0.15994340419769287 secs
Good Average (1000 Runs): 0.15166287755966187 secs
Ugly Average (1000 Runs): 0.16136717343330384 secs
----------
LOC Diff: 101
SLOC Diff: 55
size Diff: 2781 bytes
10 Runs Diff: -0.012287259101867676 secs
100 Runs Diff: -0.015212132930755629 secs
1000 Runs Diff: -0.009704295873641966 secs
```
