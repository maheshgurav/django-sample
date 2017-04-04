'''
Created on Dec 18, 2016

@author: Mahesh.Gurav
'''
from models.user_types import UserType

class User(object):
    def __init__(self):
        self._user_id = ''
        self._user_name = ''
        self._password = ''
        self._user_type = UserType.CLIENTS

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    @user_id.deleter
    def user_id(self):
        del self._user_id

    @property
    def user_name(self):
        return self._user_name
    
    @user_name.setter
    def user_name(self, value):
        self._user_name = value
    
    @user_name.deleter
    def user_name(self):
        del self._user_name

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value):
        self._password = value
    
    @password.deleter
    def password(self):
        del self._password

    @property
    def user_type(self):
        return self._user_type
    
    @user_type.setter
    def user_type(self, value):
        self._user_type = value
    
    @user_type.deleter
    def user_type(self):
        del self._user_type
