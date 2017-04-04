'''
Created on Dec 14, 2016

@author: Mahesh.Gurav
'''

from models.data_store import DataStore
from common.common_methods import remove_common_words
from sortedcontainers.sortedset import SortedSet
import logging
logger = logging.getLogger(__name__)

def run_indexer(hotel_details):
    '''
    
    :param hotel_details:
    '''
    try:
        index_by_city(hotel_details)
        index_by_stars(hotel_details)
        index_by_hotel_name(hotel_details)
    except Exception, ex:
        logger.exception(ex)
        raise ex


def index_by_city(hotel_details):
    '''
    
    :param hotel_details:
    '''
    try:
        if DataStore().city_indexed_data.get(hotel_details.city) is not None:
            DataStore().city_indexed_data[hotel_details.city].append(hotel_details.hotel_id)
        else:
            hotel_id_list = []
            hotel_id_list.append(hotel_details.hotel_id)
            DataStore().city_indexed_data[hotel_details.city] = hotel_id_list
    except Exception, ex:
        logger.exception(ex)
        raise ex

        
def index_by_stars(hotel_details):
    '''
    
    :param hotel_details:
    '''
    try:
        if DataStore().star_ranking_indexed_data.get(hotel_details.star_ranking) is not None:
            DataStore().star_ranking_indexed_data[hotel_details.star_ranking].append(hotel_details.hotel_id)
        else:
            hotel_id_list = []
            hotel_id_list.append(hotel_details.hotel_id)
            DataStore().star_ranking_indexed_data[hotel_details.star_ranking] = hotel_id_list
    except Exception, ex:
        logger.exception(ex)
        raise ex


def index_by_hotel_name(hotel_details):
    '''
    
    :param hotel_details:
    '''
    try:
        hotel_name_words = remove_common_words(hotel_details.name)
        for word in hotel_name_words:
            index_search_terms(word, hotel_details)
            add_search_term(word)
            if DataStore().hotel_name_indexed_data.get(word) is not None:
                DataStore().hotel_name_indexed_data[word.lower()].append(hotel_details.hotel_id)
            else:
                hotel_id_list = []
                hotel_id_list.append(hotel_details.hotel_id)
                DataStore().hotel_name_indexed_data[word.lower()] = hotel_id_list
    except Exception, ex:
        logger.exception(ex)
        raise ex


def add_search_term(word):
    '''
    
    :param word:
    '''
    try:
        DataStore().search_terms.add(word)
    except Exception, ex:
        logger.exception(ex)
        raise ex


def index_search_terms(word, hotel_details):
    '''
    
    :param word:
    :param hotel_details:
    '''
    try:    
        if DataStore().indexed_search_terms.get(word) is not None:
            DataStore().indexed_search_terms[word.lower()].append(hotel_details.hotel_id)
        else:
            hotel_names = SortedSet()
            hotel_names.add(word.lower())
            word_len = len(word)
            DataStore().indexed_search_terms[word.lower()[0:(word_len if word_len <= 1 else 2)]] = word
    except Exception, ex:
        logger.exception(ex)
        raise ex
