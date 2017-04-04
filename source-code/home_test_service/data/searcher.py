'''
Created on Dec 17, 2016

@author: Mahesh.Gurav
'''

from models.data_store import DataStore
from common.common_methods import remove_common_words, build_regex
import distance
import logging
logger = logging.getLogger(__name__)

def search_hotel_by_id(hotel_id):
    '''
    
    :param hotel_id:
    '''
    try:
        result = []
        result.append(DataStore().data.get(int(hotel_id)))
        return result
    except Exception, ex:
        logger.exception(ex)
        raise ex


def search_hotels_from_city_indexer(search_term):
    '''
    
    :param search_term:
    '''
    result = []
    try:
        hotel_id_list = DataStore().city_indexed_data.get(search_term)
        for hotel_id in hotel_id_list:
            result.append(DataStore().data.get(hotel_id))
    except Exception, ex:
        logger.exception(ex)
        raise ex
    return result


def search_hotels_from_star_indexer(search_term):
    '''
    
    :param search_term:
    '''
    result = []
    try:
        hotel_id_list = DataStore().star_ranking_indexed_data.get(search_term)
        for hotel_id in hotel_id_list:
            result.append(DataStore().data.get(hotel_id))
    except Exception, ex:
        logger.exception(ex)
        raise ex
    return result


def search_hotels_from_name_indexer(search_term):
    '''
    
    :param search_term:
    '''
    result = []
    try:
        hotel_id_list = DataStore().hotel_name_indexed_data.get(search_term)
        for hotel_id in hotel_id_list:
            result.append(DataStore().data.get(hotel_id))
    except Exception, ex:
        logger.exception(ex)
        raise ex
    return result


def search_name_with_all_search_terms(search_terms):
    '''
    
    :param search_terms:
    '''
    result = []
    try:
        hotel_id_list = get_hotel_id_list(search_terms)
        for hotel_id in hotel_id_list:
            hotel_info = DataStore().data.get(hotel_id)
            terms_from_name = remove_common_words(hotel_info.name)
            all_terms_present = True
            for term in terms_from_name:
                if term not in search_terms:
                    all_terms_present = False
                    break
            if all_terms_present:
                result.append(hotel_info)
    except Exception, ex:
        logger.exception(ex)
        raise ex
    return result


def search_name_with_some_search_terms(search_terms):
    '''
    
    :param search_terms:
    '''
    result = []
    try:
        hotel_id_list = get_hotel_id_list(search_terms)
        for hotel_id in hotel_id_list:
            hotel_info = DataStore().data.get(hotel_id)
            result.append(hotel_info)
    except Exception, ex:
        logger.exception(ex)
        raise ex
    return result


def get_hotel_id_list(search_terms):
    '''
    
    :param search_terms:
    '''
    try:
        hotel_id_list = []
        for search_term in search_terms:
            id_list = DataStore().hotel_name_indexed_data.get(search_term)
            if id_list is not None:
                hotel_id_list += id_list
        return list(set(hotel_id_list))
    except Exception, ex:
        logger.exception(ex)
        raise ex
    

def search_by_regex(search_term):
    '''
    
    :param search_term:
    '''
    result = []
    try:
        regex = build_regex(search_term)
        search_terms = [item.group(0) for term in DataStore().search_terms for item in [regex.search(term)] if item]
        if search_terms is not None and len(search_terms) > 0:
            result = search_name_with_some_search_terms(search_terms)
    except Exception, ex:
        logger.exception(ex)
        raise ex
    return result


def get_seach_terms_by_distance(search_term, required_distance):
    '''
    
    :param search_term:
    :param required_distance:
    '''
    search_terms = []
    try:
        for term in DataStore().search_terms:
            if distance.nlevenshtein(search_term, term) <= required_distance:
                search_terms.append(term)
    except Exception, ex:
        logger.exception(ex)
        raise ex
    return search_terms


def search_by_distance(search_term, required_distance = 0.5):
    '''
    
    :param search_term:
    :param required_distance:
    '''
    result = []
    try:
        search_terms = get_seach_terms_by_distance(search_term, required_distance)
        if search_terms is not None and len(search_terms) > 0:
            result = search_name_with_some_search_terms(search_terms)
    except Exception, ex:
        logger.exception(ex)
        raise ex
    return result


def search_by_range(search_term):
    '''
    
    :param search_term:
    '''
    try:
        search_terms = search_term[len('DIF/Entry_Title:{'), len(search_term) - 1].strip()
        search_terms_list = search_terms.split(" ")
        search_terms_list.remove("TO")
        sorted_search_terms = sorted(search_terms_list)
        return search_name_with_some_search_terms(get_search_range_terms(sorted_search_terms[0], sorted_search_terms[1]))
    except Exception, ex:
        logger.exception(ex)
        raise ex


def get_search_range_terms(start_search_term, end_search_term):
    '''
    
    :param start_search_term:
    :param end_search_term:
    '''
    try:
        start_index = DataStore().hotel_names.index(start_search_term)
        end_index = DataStore().hotel_names.index(start_search_term)
        return DataStore().hotel_names[start_index + 1 : end_index - 1]
    except Exception, ex:
        logger.exception(ex)
        raise ex
