'''
Created on Dec 20, 2016

@author: Mahesh.Gurav
'''

class TokenAuthentication(object):
    valid_auth_tokens = {"token_1" : "admin", "token_2" : "client"}
    
    def process_request(self, request):
        if request.META.get('HTTP_AUTHORIZATION') is None and str(request.META.get('HTTP_AUTHORIZATION')) not in self.valid_auth_tokens.keys():
            raise Exception("You are not authorised person to call this resource")
        if str(request.META.get('HTTP_AUTHORIZATION')) in self.valid_auth_tokens.keys():
            return None

    
    def check_user_rights_on_url(self, url, user_type):
        if user_type == "admin":
            admin_urls = ['/hotel-finder/add/', '/hotel-finder/delete/', '/hotel-finder/search/']
            return url in admin_urls
        if user_type == "client":
            client_urls = ['/hotel-finder/search/']
            return url in client_urls