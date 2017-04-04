'''
Created on Dec 18, 2016

@author: Mahesh.Gurav
'''

import unittest
from data.data_operations import insert_value
from models.hotel_details import Hotel
from search.fuzzy_search import FuzzySearch

class Test(unittest.TestCase):
    def setUp(self):
        self.fuzzy_search = FuzzySearch()
        unittest.TestCase.setUp(self)

        
    def test_search_correct_result(self):
        self.assertEqual(len(self.fuzzy_search.search("hotel_name", "ark~0.5")), 1)
        self.assertEqual(len(self.fuzzy_search.search("hotel_name", "estique~1")), 1) 


    def test_search_raises_exception(self):
        self.assertRaises(AttributeError, lambda:self.fuzzy_search.search("hotel_name", None))
        

    def test_search_no_result(self):
        self.assertEqual(len(self.fuzzy_search.search("hotel_name", "sheritan")), 0)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    hotel = Hotel()
    hotel.name = 'Park Estique'
    hotel.country = 'India'
    hotel.city = 'Mumbai'
    hotel.street = 'Bajirao Road'
    hotel.description = 'This is a very good hotel'
    hotel.telephone_number = 12345
    hotel.star_ranking = 4.0
    hotel.number_of_rooms = 10
    insert_value(hotel)    
    unittest.main()