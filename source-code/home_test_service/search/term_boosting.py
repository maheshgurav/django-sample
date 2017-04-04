'''
Created on Dec 14, 2016

@author: Mahesh.Gurav
'''

from search.search_base import BaseSearch
import logging
logger = logging.getLogger(__name__)

class BoostedSearch(BaseSearch):
    def search(self, search_field, search_term):
        raise NotImplementedError