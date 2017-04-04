'''
Created on Dec 14, 2016

@author: Mahesh.Gurav
'''

from search.search_base import BaseSearch
from data.searcher import search_by_regex
import logging
logger = logging.getLogger(__name__)

class WildCardSearch(BaseSearch):
    def search(self, search_field, search_term):
        '''
        
        :param search_field:
        :param search_term:
        '''
        try:
            return search_by_regex(search_term)
        except Exception, ex:
            logger.exception(ex)
            raise ex
