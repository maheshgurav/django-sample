'''
Created on Dec 14, 2016

@author: Mahesh.Gurav
'''

from search.search_base import BaseSearch
from data.searcher import search_name_with_all_search_terms,\
    search_name_with_some_search_terms
import logging
logger = logging.getLogger(__name__)

class BooleanSearch(BaseSearch):
    def search(self, search_field, search_term):
        '''
        
        :param search_field:
        :param search_term:
        '''
        try:
            search_terms = search_term.split(" ")
            if search_field == "hotel_name":
                if "AND" in search_terms:
                    search_terms.remove("AND")
                    return search_name_with_all_search_terms(search_terms)
                if "OR" in search_terms:
                    return search_name_with_some_search_terms(search_terms)
        except Exception, ex:
            logger.exception(ex)
            raise ex
