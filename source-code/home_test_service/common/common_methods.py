'''
Created on Dec 7, 2016

@author: Mahesh.Gurav
'''

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re
import logging
from models.hotel_details import Hotel
import json
logger = logging.getLogger(__name__)

def remove_common_words(query):
    '''
    
    :param query:
    '''
    try:
        common_words = set(stopwords.words('english'))
        common_words.add("hotel")
        common_words.add("lodge")
        querywords = query.lower().split()
        resultwords  = [word for word in querywords if word.lower() not in common_words]
        return resultwords        
    except Exception, ex:
        logger.exception(ex)
        raise ex
    

def get_stem_words(word_list):
    '''
    
    :param word_list:
    '''
    result = []
    try:
        porter_stemmer = PorterStemmer()
        for word in word_list:
            result.append(porter_stemmer.stem(word))
    except Exception, ex:
        logger.exception(ex)
        raise ex
    return result    


def add_letters_in_term(value_to_update):
    '''
    
    :param value_to_update:
    '''
    result = []
    try:
        terms_to_append = ("a", "e", "i", "o", "u", "j", "1","2", "3", "4", "5", "6", "7", "8", "9", "&")
        for term in terms_to_append:
            result.append(value_to_update + term)
    except Exception, ex:
        logger.exception(ex)
        raise ex
    return result


def update_search_term(search_term):
    '''
    
    :param search_term:
    '''
    try:
        return add_letters_in_term(search_term)
    except Exception, ex:
        logger.exception(ex)
        raise ex


def build_regex(search_term):
    '''
    
    :param search_term:
    '''
    try:
        search_term = search_term.replace("*", ".*")
        search_term = search_term.replace("?", ".?")
        return re.compile(search_term)
    except Exception, ex:
        logger.exception(ex)
        raise ex


def build_hotel_object(json_str):
    '''
    
    :param json_str:
    '''
    hotel_json = json.loads(json_str)
    hotel = Hotel()
    hotel.name = str(hotel_json.get("name"))
    hotel.country = str(hotel_json.get("country"))
    hotel.city = str(hotel_json.get("city"))
    hotel.street = str(hotel_json.get("street"))
    hotel.description = str(hotel_json.get("description"))
    hotel.telephone_number = str(hotel_json.get("telephone_number"))
    hotel.star_ranking = int(hotel_json.get("star_ranking"))
    hotel.number_of_rooms = int(hotel_json.get("number_of_rooms"))
    return hotel


def build_hotel_json(result):
    result_json = {}
    result_list = []
    for hotel_info in result:
        hotel_json = {}
        hotel_json["hotel_id"] = hotel_info.hotel_id
        hotel_json["hotel_name"] = hotel_info.name
        hotel_json["name"] = hotel_info.name
        hotel_json["country"] = hotel_info.country
        hotel_json["city"] = hotel_info.city
        hotel_json["street"] = hotel_info.street
        hotel_json["description"] = hotel_info.description
        hotel_json["telephone_number"] = hotel_info.telephone_number
        hotel_json["star_ranking"] = hotel_info.star_ranking
        hotel_json["number_of_rooms"] = hotel_info.number_of_rooms
        result_list.append(hotel_json)
    result_json["hotels"] = result_list 
    return json.dumps(result_json)


def build_search_json(request):
    '''
    
    :param request:
    '''
    search_json = {}
    search_json["search_type"] = str(request.GET['search_type'])
    search_json["search_field"] = str(request.GET['search_field'])
    search_json["search_term"] = str(request.GET['search_term'])
    return search_json
