""" Module doc string """

import json
import requests

class PyPin(object):
    """Python client consume Pinterest API"""
    TIMEOUT = 5
    API_HOST = 'https://api.pinterest.com/'

    def __init__(self, accesstoken, version='v1'):
        self.accesstoken = accesstoken
        self.api_verson = version

    @staticmethod
    def call(url, method='get', params=None):
        """
        API call to Pinterest
            url: String, API endpoint with access token attached
            method:  String, HTTP method, get post put delete
            params: Dict, optional, supply necessary parameters
            fields: String, optional, expected return fields,
                will return default fields if not specified
        """
        request = getattr(requests, method)(url, timeout=PyPin.TIMEOUT, data=params)
        print request.json()
        if request.status_code in [200, 201]:
            return request.json()['data']
        else:
            raise RuntimeError('API request return status code '+str(request.status_code))

    def get_me(self):
        """Get the authenticated user's Pinterest account info"""
        api_endpoint = PyPin.API_HOST + self.api_verson +'/me/'
        request_url = api_endpoint + '?access_token=' + self.accesstoken
        return PyPin.call(request_url)

    def getlikes(self):
        """Get the pins that the authenticated user likes"""
        pass

    def get_followers(self):
        """Get the authenticated user's followers"""
        pass

    def get_followed_boards(self):
        """Get the boards that the authenticated user follows"""
        pass

    def get_followed_users(self):
        """Get the Pinterest users that the authenticated user follows"""
        pass

    def get_followed_interests(self):
        """Get the interests that the authenticated user follows"""
        pass

    def follow_user(self, username):
        """Follow a user"""
        pass

    def unfollow_user(self, username):
        """Unfollow a user"""
        pass

    def follow_board(self, board_id):
        """Follow a board"""
        pass

    def unfollow_board(self, board_id):
        """Unfollow a board"""
        pass

    def follow_interest(self, interest_id):
        """Follow an interest"""
        pass

    def unfollow_interest(self, interest_id):
        """Unfollow an interest"""
        pass

    def get_pins(self):
        """Get all of authenticated users's pins"""
        pass

    def get_boards(self):
        """Get all of authenticated users's boards"""
        pass

    def get_user(self, username):
        """Get the account info for a Pinterest user"""
        pass

    def create_board(self, board_info):
        """Create a new board
        parameters:
             name: 'board name',
             description: 'Board description, optional'
        """
        api_endpoint = PyPin.API_HOST + self.api_verson +'/boards/'
        request_url = api_endpoint + '?access_token=' + self.accesstoken
        return PyPin.call(request_url, 'post', board_info)

    def create_pin(self, pin_info):
        """Create a pin on a board
        pinInfo structure:
             board: '<username>/<board_name>' OR '<board_id>',
             note: 'My note'
             link: 'https://www.google.com',
             image_url: 'http://marketingland.com/pinterest-logo-white-1920.png'
        """
        api_endpoint = PyPin.API_HOST + self.api_verson +'/pins/'
        request_url = api_endpoint + '?access_token=' + self.accesstoken
        return PyPin.call(request_url, 'post', pin_info)
