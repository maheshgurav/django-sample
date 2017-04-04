'''
Created on Dec 14, 2016

@author: Mahesh.Gurav
'''

from search.search_base import BaseSearch
from data.searcher import search_by_distance
import logging
logger = logging.getLogger(__name__)

class FuzzySearch(BaseSearch):
    def search(self, search_field, search_term):
        '''
        
        :param search_field:
        :param search_term:
        '''
        try:
            search_term_list = search_term.split("~")
            search_term = search_term.split("~")[0]
            if len(search_term_list) > 1:
                #Got this error while unit testing the code
                #required_distance = search_term.split("~")[len(search_term_list) - 1]
                required_distance = search_term_list[len(search_term_list) - 1]
                return search_by_distance(search_term, required_distance)
            return search_by_distance(search_term)
        except Exception, ex:
            logger.exception(ex)
            raise ex
