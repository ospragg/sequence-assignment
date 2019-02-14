#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import responses

import sys
sys.path.append('../')
import sequence_assesment.sequence_handler

class TestBasicFunction(unittest.TestCase):
	def setUp(self):
		pass
 
	def test_1(self):
		self.assertTrue(1 == 1)
 
if __name__ == '__main__':
	unittest.main()