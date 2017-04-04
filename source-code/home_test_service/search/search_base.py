'''
Created on Dec 14, 2016

@author: Mahesh.Gurav
'''

from abc import abstractmethod

class BaseSearch():
    @abstractmethod
    def search(self, search_field, search_term):
        raise NotImplementedError
