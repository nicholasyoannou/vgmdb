# -*- coding: UTF-8 -*-
import os
import unittest

from vgmdb import utils

base = os.path.dirname(__file__)

class TestUtils(unittest.TestCase):
	def setUp(self):
		pass

	def test_date_parse(self):
		date = "Aug 3, 2006 01:33 AM"
		self.assertEqual("2006-08-03T01:33", utils.parse_date_time(date))
		date = "Oct 04, 2000"
		self.assertEqual("2000-10-04", utils.parse_date_time(date))
		date = "November 11, 2011"
		self.assertEqual("2011-11-11", utils.parse_date_time(date))

	def test_dotted_year(self):
		""" Make sure that weird dates with unknown month and days work """
		date = utils.normalize_dotted_date("2007.??.??")
		self.assertEqual("2007", date)
	def test_dotted_month(self):
		""" Make sure that weird dates with unknown days work """
		date = utils.normalize_dotted_date("2007.02.??")
		self.assertEqual("2007-02", date)
	def test_dotted_day(self):
		""" Make sure that conversion from YYYY.MM.DD to YYYY-MM-DD works """
		date = utils.normalize_dotted_date("2007.02.20")
		self.assertEqual("2007-02-20", date)
	def test_dotted_shortday(self):
		""" Make sure that conversion from YYYY.M.D to YYYY-MM-DD works """
		date = utils.normalize_dotted_date("2007.2.9")
		self.assertEqual("2007-02-09", date)
