'''
Created on Dec 20, 2016

@author: Mahesh.Gurav
'''

from data.data_operations import insert_value, search
from common.common_methods import build_hotel_object, build_search_json

def add_hotel(request):
    '''
    
    :param request:
    '''
    return insert_value(build_hotel_object(request.body))


def update_hotel(request):
    '''
    
    :param request:
    '''


def delete_hotel(request):
    '''
    
    :param request:
    '''


def search_hotel(request):
    '''
    
    :param request:
    '''
    search_dict = build_search_json(request)
    return search(search_dict)
