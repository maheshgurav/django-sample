'''
Created on Dec 18, 2016

@author: Mahesh.Gurav
'''
import unittest
from data.data_operations import insert_value
from models.hotel_details import Hotel
from models.data_store import DataStore
import search

class Test(unittest.TestCase):
    
    def test_insert_value_correct_result(self):
        pass
    
    
    def test_insert_value_incorrect_result(self):
        pass
    
        
    def test_delete_value_correct_result(self):
        pass
    
        
    def test_delete_value_incorrect_result(self):
        pass
        
        
    def test_update_value_correct_result(self):
        pass
    
            
    def test_update_value_incorrect_result(self):
        pass
    
            
    def test_search_correct_result(self):
        pass
    
    
    def test_search_incorrect_result(self):
        pass
    
    
    def setUp(self):
        self.hotel = Hotel()
        self.hotel.name = 'Park Estique'
        self.hotel.country = 'India'
        self.hotel.city = 'Mumbai'
        self.hotel.street = 'Bajirao Road'
        self.hotel.description = 'This is a very good hotel'
        self.hotel.telephone_number = 12345
        self.hotel.star_ranking = 4.0
        self.hotel.number_of_rooms = 10


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()