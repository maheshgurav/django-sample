'''
Created on Dec 18, 2016

@author: Mahesh.Gurav
'''

import unittest
from models.hotel_details import Hotel
from data.data_operations import insert_value
from search.boolean_search import BooleanSearch

class Test(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.boolean_search = BooleanSearch()

    
    def test_search_correct_result(self):
        self.assertEqual(len(self.boolean_search.search("hotel_name", "park AND estique")), 1)


    def test_search_raises_exception(self):
        self.assertRaises(AttributeError, lambda:self.boolean_search.search("hotel_name", None))


    def test_search_no_result(self):
        self.assertNotEqual(len(self.boolean_search.search("hotel_name", "park AND estique")), 0)
        

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