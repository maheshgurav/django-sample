'''
Created on Dec 14, 2016

@author: Mahesh.Gurav
'''

from search.search_base import BaseSearch
from common.common_methods import update_search_term
from data.searcher import search_name_with_all_search_terms
import logging
logger = logging.getLogger(__name__)

class FieldedSearch(BaseSearch):
    def search(self, search_field, search_term):
        '''
        
        :param search_field:
        :param search_term:
        '''
        try:
            return search_name_with_all_search_terms(self.get_search_term(search_term))
        except Exception, ex:
            logger.exception(ex)
            raise ex
 

    def get_search_term(self, search_term):
        try:
            search_terms = []
            exact_search_term = search_term[len('DIF/Entry_Title:'):len(search_term)].strip()
            if len(exact_search_term) <= 1:
                search_terms += update_search_term(search_term)
            return exact_search_term.split(" ")
        except Exception, ex:
            logger.exception(ex)
            raise ex
