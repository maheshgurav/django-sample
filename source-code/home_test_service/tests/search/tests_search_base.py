'''
Created on Dec 18, 2016

@author: Mahesh.Gurav
'''

import unittest
from search.search_base import BaseSearch

class Test(unittest.TestCase):
    def setUp(self):
        self.base_search = BaseSearch()
        unittest.TestCase.setUp(self)


    def test_search_raises_exception(self):
        self.assertRaises(NotImplementedError, lambda:self.base_search.search("hotel_name", None))
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()