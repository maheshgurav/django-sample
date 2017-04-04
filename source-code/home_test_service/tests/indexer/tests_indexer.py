'''
Created on Dec 19, 2016

@author: Mahesh.Gurav
'''
import unittest
from indexer.data_indexer import index_by_city
from data.data_operations import insert_value
from models.hotel_details import Hotel
from models.data_store import DataStore

class Test(unittest.TestCase):

    def test_index_by_city(self):
        self.assertEqual(len(DataStore().city_indexed_data), 0)
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
        index_by_city(hotel)
        self.assertEqual(len(DataStore().city_indexed_data), 1)


    def test_index_by_stars(self):
        self.assertEqual(len(DataStore().star_ranking_indexed_data), 0)
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
        index_by_city(hotel)
        self.assertEqual(len(DataStore().star_ranking_indexed_data), 1)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()