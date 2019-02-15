#!/usr/bin/env python
# -*- coding: utf-8 -*-
from argparse import ArgumentParser
import re
import sequence_assesment.sequence_handler as sh

# parse the script parameters
parser = ArgumentParser()
parser.add_argument("filename",
                    type=str,
                    help="location of the file to be processed")
parser.add_argument("n_subseq",
                    type=int,
                    help="length of the subsequence")
parser.add_argument("behaviour",
                    type=str,
                    choices=["values", "differences"],
                    help="return sum of values ('values'), or sum of differences ('differeces')")
args = parser.parse_args()

# load the input sequence, remove anything except numbers, spaces, and -ve signs, and split into ints
with open(args.filename, "rb") as f:
	sequence = [int(el) for el in re.sub("[^-\d ]", "", f.read()).split(" ")]

# process the sequence
if args.behaviour == "values":
	
	print(sh.find_subsequence_sum_max(sequence, max_n_subseq=int(args.n_subseq)))
	
elif args.behaviour == "differences":
	
	print(sh.find_d_subsequence_sum_max(sequence, max_n_subseq=int(args.n_subseq)))
	
else:
	raise Exception("invalid behaviour argument")