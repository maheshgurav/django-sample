'''
Created on Dec 7, 2016

@author: Mahesh.Gurav
'''

from models.hotel_details import Hotel
from data.data_operations import insert_value, search, delete_value

if __name__ == '__main__':
    hotel = Hotel()
    hotel.name = 'Park Estique'
    hotel.country = 'India'
    hotel.city = 'Mumbai'
    hotel.street = 'Bajirao Road'
    hotel.description = 'This is a very good hotel'
    hotel.telephone_number = 12345
    hotel.star_ranking = 4.0
    hotel.number_of_rooms = 10
    
    hotel1 = Hotel()
    hotel1.name = 'Sun And Sand Estique'
    hotel1.country = 'India'
    hotel1.city = 'Pune'
    hotel1.street = 'Shivaji Road'
    hotel1.description = 'This is a very good hotel with Swimming pool'
    hotel1.telephone_number = 12345
    hotel1.star_ranking = 4.5
    hotel1.number_of_rooms = 20
    
    insert_value(hotel)
    print hotel.hotel_id
    insert_value(hotel1)
    print hotel1.hotel_id
    print search({"search_type" : "fulltext_search", "search_field" : "id", "search_term": 1})
    print search({"search_type" : "fulltext_search", "search_field" : "city", "search_term": "Pune"})
    print search({"search_type" : "boolean_search", "search_field" : "hotel_name", "search_term": "park AND estique"})
    print search({"search_type" : "boolean_search", "search_field" : "hotel_name", "search_term": "park AND estique1"})
    print search({"search_type" : "boolean_search", "search_field" : "hotel_name", "search_term": "park OR estique1"})
    print search({"search_type" : "boolean_search", "search_field" : "hotel_name", "search_term": "park OR estique"})
    print search({"search_type" : "fielded_search", "search_field" : "hotel_name", "search_term": "DIF/Entry_Title:park estique"})
    print search({"search_type" : "fielded_search", "search_field" : "hotel_name", "search_term": "DIF/Entry_Title:park estique1"})
    print search({"search_type" : "wildcard_search", "search_field" : "hotel_name", "search_term": "p*rk"})
    print search({"search_type" : "wildcard_search", "search_field" : "hotel_name", "search_term": "p?rk"})
    print search({"search_type" : "fuzzy_search", "search_field" : "hotel_name", "search_term": "ark"})
    print search({"search_type" : "fuzzy_search", "search_field" : "hotel_name", "search_term": "ets"})

    delete_value(2)
    delete_value(1)