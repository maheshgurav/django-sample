'''
Created on Dec 18, 2016

@author: Mahesh.Gurav
'''

import unittest
from search.term_boosting import BoostedSearch

class Test(unittest.TestCase):
    def setUp(self):
        self.term_boost_search = BoostedSearch()
        unittest.TestCase.setUp(self)


    def test_search_raises_exception(self):
        self.assertRaises(NotImplementedError, lambda:self.term_boost_search.search("hotel_name", None))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()