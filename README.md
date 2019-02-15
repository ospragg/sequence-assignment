# sequence-assignment
Basic library to find the size of the largest subsequence within a sequence of integers, or the largest subsequence of absolute differences within a sequence of integers.

## Getting started

Install requirements:
```
pip install -r requirements.txt
```

Run tests:
```
python -m unittest discover -v
```

Process a file containing a sequence:
```
python find_subsequence.py data/input_3.txt 30 values
python find_subsequence.py data/input_3.txt 30 differences
```

Note that input files must contain only integer numbers, eg.:
```
4 6 -2 4 22 74 2 5 33 1
```