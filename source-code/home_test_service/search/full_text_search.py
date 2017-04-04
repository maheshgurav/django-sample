'''
Created on Dec 14, 2016

@author: Mahesh.Gurav
'''

from search.search_base import BaseSearch
from data.searcher import search_hotels_from_city_indexer,\
    search_hotels_from_star_indexer, search_hotel_by_id
import logging
logger = logging.getLogger(__name__)

class FullTextSearch(BaseSearch):    
    def search(self, search_field, search_term):
        '''
        
        :param search_field:
        :param search_term:
        '''
        try:
            if search_field == 'id':
                return search_hotel_by_id(search_term)
            if search_field == 'city':
                return search_hotels_from_city_indexer(search_term)
            if search_field == 'star_ranking':
                return search_hotels_from_star_indexer(search_term)
        except Exception, ex:
            logger.exception(ex)
            raise ex
