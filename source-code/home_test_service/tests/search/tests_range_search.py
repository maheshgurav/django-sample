'''
Created on Dec 18, 2016

@author: Mahesh.Gurav
'''

import unittest
from search.range_search import RangeSearch

class Test(unittest.TestCase):
    def setUp(self):
        self.range_search = RangeSearch()
        unittest.TestCase.setUp(self)


    def test_search_raises_exception(self):
        self.assertRaises(NotImplementedError, lambda:self.range_search.search("hotel_name", None))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()