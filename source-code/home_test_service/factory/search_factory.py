'''
Created on Dec 14, 2016

@author: Mahesh.Gurav
'''

from search.full_text_search import FullTextSearch
from search.boolean_search import BooleanSearch
from search.fielded_search import FieldedSearch
from search.fuzzy_search import FuzzySearch
from search.range_search import RangeSearch
from search.term_boosting import BoostedSearch
from search.wildcard_search import WildCardSearch
import logging
from common.common_methods import build_hotel_json
logger = logging.getLogger(__name__)

search_objects = {
                  "boolean_search" : BooleanSearch(),
                  "fielded_search" : FieldedSearch(),
                  "fulltext_search" : FullTextSearch(),
                  "fuzzy_search" : FuzzySearch(),
                  "range_search" : RangeSearch(),
                  "termboosting_search" : BoostedSearch(),
                  "wildcard_search" : WildCardSearch(),
                  }

def extract_and_search(search_query):
    '''
    
    :param search_query:
    '''
    try:
        search = get_search_object(search_query.get("search_type"))
        result = search.search(search_query.get("search_field"), search_query.get("search_term"))
        if result is not None and len(result) > 0:
            return build_hotel_json(result)
        return "{'result' : 'No Hotels Found'}"
    except Exception, ex:
        logger.exception(ex)
        raise ex


def get_search_object(search_type):
    '''
    
    :param search_type:
    '''
    try:
        if search_type is None:
            search_type = "fulltext_search"
        return search_objects.get(search_type)
    except Exception, ex:
        logger.exception(ex)
        raise ex
