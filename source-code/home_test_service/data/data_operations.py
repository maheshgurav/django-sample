'''
Created on Dec 7, 2016

@author: Mahesh.Gurav
'''

from models.data_store import DataStore
from indexer.data_indexer import run_indexer
from factory.search_factory import extract_and_search
from django.http.response import HttpResponse
import logging
logger = logging.getLogger(__name__)

def insert_value(hotel_details):
    '''
    
    :param hotel_details:
    '''
    response = HttpResponse()
    try:
        hotel_details.hotel_id = len(DataStore().data) + 1
        run_indexer(hotel_details)
        DataStore().data[hotel_details.hotel_id] = hotel_details
        response.content = "Hotel Added Successfully"
    except Exception, ex:
        response.status_code = 500        
        logger.exception(ex)
        raise ex
    return response


def delete_value(hotel_id):
    '''
    
    :param hotel_id:
    '''
    response = HttpResponse()
    try:
        del DataStore().data[hotel_id]
    except Exception, ex:
        response.status_code = 500
        logger.exception(ex)
        raise ex
    return response


def update_value(hotel_id, hotel_details):
    '''
    
    :param hotel_id:
    :param hotel_details:
    '''
    response = HttpResponse()
    try:
        DataStore().data[hotel_details.hotel_id] = hotel_details
    except Exception, ex:
        response.status_code = 500
        logger.exception(ex)
        raise ex
    return response


def search(search_query):
    '''
    
    :param search_query:
    '''
    response = HttpResponse()
    try:
        response.content = extract_and_search(search_query)
    except Exception, ex:
        response.status_code = 500
        logger.exception(ex)
    return response
