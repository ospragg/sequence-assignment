#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import responses

import sys
sys.path.append('../')
import sequence_assesment.sequence_handler as sh

input_1 = [3, -5, 1, 2, -1, 4, -3, 1, -2]
input_2 = [9, 5, -10, 7, -8, 3, -8, 6, 6, 3, 4, 8, -6, -2, 3, -8, -1, -8, -4, -9]

class TestBasicFunction(unittest.TestCase):
	
	def setUp(self):
		pass
 
	def test_1(self):
		self.assertTrue(1 == 1)
	
	def test_2(self):
		self.assertTrue(sh.find_subsequence_sum_max(input_1, max_n_subseq=4) == 6)
	
	def test_3(self):
		self.assertFalse(sh.find_subsequence_sum_max(input_1, max_n_subseq=9) == 12)
	
	def test_4(self):
		self.assertTrue(sh.find_subsequence_sum_max(input_2, max_n_subseq=10) == 27)
	
	def test_5(self):
		self.assertFalse(sh.find_subsequence_sum_max(input_2, max_n_subseq=10) == 99)
	
	def test_6(self):
		self.assertTrue(sh.find_subsequence_sum_max(input_1, max_n_subseq=9) == 6)
	
	def test_7(self):
		self.assertTrue(sh.find_d_subsequence_sum_max(input_1, max_n_subseq=4) == 16)
	
	def test_8(self):
		self.assertFalse(sh.find_d_subsequence_sum_max(input_1, max_n_subseq=4) == 99)
	
	def test_9(self):
		self.assertTrue(sh.find_d_subsequence_sum_max(input_2, max_n_subseq=5) == 58)
	
	def test_10(self):
		self.assertFalse(sh.find_d_subsequence_sum_max(input_2, max_n_subseq=6) == 58)
 
if __name__ == '__main__':
	unittest.main()