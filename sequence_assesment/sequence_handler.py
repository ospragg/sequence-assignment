#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pprint

def find_subsequence_sum_max(sequence, max_n_subseq=None):
	
	# make sure our sequnce is in the right format
	assert(type(sequence) == list and all(type(el) == int for el in sequence))
	
	# define the max length of the subsequence if it isn't already
	# defined, or is larger than the length of the sequence
	max_n_subseq = len(sequence) - 1 if max_n_subseq == None or max_n_subseq >= len(sequence) else max_n_subseq
	
	# reduce the max length of the subsequence by one, since we assume
	# that the length of the subsequence < length of sequence
	max_n_subseq -= 1
	
	# create a numpy array from our list, so we don't have to convert multiple times
	np_seq = np.array(sequence, dtype=int)
	
	# convolve the sequence with filters with length of all possible subsequences
	# the convolution with the highest value represents the sequence with the largest sum
	# find the max of each convolution imediately - rather than keeping the resulting convolution - to save memory
	max_sums = [np.max(np.convolve(np_seq, np.ones(k + 2, dtype=int), mode="valid")) for k in xrange(0, max_n_subseq)]
	
	# return the largest result
	return max(max_sums)

def find_d_subsequence_sum_max(sequence, max_n_subseq=None):
	
	# reduce max_n_subseq by 1, since we are differencing so the sequence length is shorter
	max_n_subseq = len(sequence) - 1 if max_n_subseq == None else max_n_subseq - 1
	
	# calculate the d sequence
	d_sequence = [abs(a - b) for a, b in zip(sequence[0 : -1], sequence[1 : None])]
	
	return find_subsequence_sum_max(d_sequence, max_n_subseq)
	

if __name__ == '__main__':
	pass
	print(find_subsequence_sum_max([3, -5, 1, 2, -1, 4, -3, 1, -2], max_n_subseq=4))
	print(find_subsequence_sum_max([9, 5, -10, 7, -8, 3, -8, 6, 6, 3, 4, 8, -6, -2, 3, -8, -1, -8, -4, -9]))
	print(find_d_subsequence_sum_max([3, -5, 1, 2, -1, 4, -3, 1, -2], max_n_subseq=4))



