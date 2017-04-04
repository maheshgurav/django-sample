'''
Created on Dec 7, 2016

@author: Mahesh.Gurav
'''

class Hotel(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._hotel_id = ''
        self._name = ''
        self._country = ''
        self._city = ''
        self._street = ''
        self._description = ''
        self._telephone_number = ''
        self._star_ranking = 0.0
        self._number_of_rooms = 0

    @property
    def hotel_id(self):
        return self._hotel_id

    @hotel_id.setter
    def hotel_id(self, value):
        self._hotel_id = value

    @hotel_id.deleter
    def hotel_id(self):
        del self._hotel_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value

    @country.deleter
    def country(self):
        del self._country        
        
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @city.deleter
    def city(self):
        del self._city
        
    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, value):
        self._street = value

    @street.deleter
    def street(self):
        del self._street

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @description.deleter
    def description(self):
        del self._description
        
    @property
    def telephone_number(self):
        return self._telephone_number

    @telephone_number.setter
    def telephone_number(self, value):
        self._telephone_number = value

    @telephone_number.deleter
    def telephone_number(self):
        del self._telephone_number
        
    @property
    def star_ranking(self):
        return self._star_ranking

    @star_ranking.setter
    def star_ranking(self, value):
        self._star_ranking = value

    @star_ranking.deleter
    def star_ranking(self):
        del self._star_ranking
        
    @property
    def number_of_rooms(self):
        return self._number_of_rooms

    @number_of_rooms.setter
    def number_of_rooms(self, value):
        self._number_of_rooms = value

    @number_of_rooms.deleter
    def number_of_rooms(self):
        del self._number_of_rooms
