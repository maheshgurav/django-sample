'''
Created on Dec 7, 2016

@author: Mahesh.Gurav
'''
from sortedcontainers.sortedset import SortedSet

class DataStore:
    class __DataStore:
        def __init__(self):
            self.data = {}
            self.city_indexed_data = {}
            self.star_ranking_indexed_data = {}
            self.hotel_name_indexed_data = {}
            self.search_terms = SortedSet()
            self.indexed_search_terms = {}
        def __str__(self):
            return ""
    instance = None
    def __init__(self):
        if not DataStore.instance:
            DataStore.instance = DataStore.__DataStore()
    def __getattr__(self, name):
        return getattr(self.instance, name)
