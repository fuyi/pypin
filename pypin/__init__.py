""" Module doc string """

import json
import requests
import urllib.request

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
        # print (request.json())
        if request.status_code in [200, 201]:
            return request.json()['data']
        else:
            raise RuntimeError('API request return status code '+str(request.status_code))

    def get_me(self):
        """Get the authenticated user's Pinterest account info"""
        api_endpoint = PyPin.API_HOST + self.api_verson +'/me/'
        request_url = api_endpoint + '?access_token=' + self.accesstoken
        return PyPin.call(request_url)

    def get_likes(self):
        """Get the pins that the authenticated user likes"""
        api_endpoint = PyPin.API_HOST + self.api_verson +'/me/likes/'
        request_url = api_endpoint + '?access_token=' + self.accesstoken
        return PyPin.call(request_url)

    def get_followers(self):
        """Get the authenticated user's followers"""
        api_endpoint = PyPin.API_HOST + self.api_verson +'/me/followers/'
        request_url = api_endpoint + '?access_token=' + self.accesstoken
        return PyPin.call(request_url)

    def get_following_boards(self):
        """Get the boards that the authenticated user follows"""
        api_endpoint = PyPin.API_HOST + self.api_verson +'/me/following/boards/'
        request_url = api_endpoint + '?access_token=' + self.accesstoken
        return PyPin.call(request_url)

    def get_following_users(self):
        """Get the Pinterest users that the authenticated user follows"""
        api_endpoint = PyPin.API_HOST + self.api_verson +'/me/following/users/'
        request_url = api_endpoint + '?access_token=' + self.accesstoken
        return PyPin.call(request_url)

    def get_following_interests(self):
        """Get the interests that the authenticated user follows"""
        api_endpoint = PyPin.API_HOST + self.api_verson +'/me/following/interests/'
        request_url = api_endpoint + '?access_token=' + self.accesstoken
        return PyPin.call(request_url)

    def follow_user(self, user_name):
        """Follow a user
		parameters:
             name: 'user_name',
             description: 'user name'
		"""
        api_endpoint = PyPin.API_HOST + self.api_verson +'/me/following/users/'
        request_url = api_endpoint + '?access_token=' + self.accesstoken
        return PyPin.call(request_url, 'post', { 'user': user_name })


    def unfollow_user(self, user_name):
        """Unfollow a user
		parameters:
             name: 'user_name',
             description: 'user name'
		"""
        api_endpoint = PyPin.API_HOST + self.api_verson +'/me/following/users/' + user_name
        request_url = api_endpoint + '?access_token=' + self.accesstoken
        return PyPin.call(request_url, 'delete')

    def follow_board(self, board_id):
        """Follow a board
		parameters:
             name: 'board_id',
             description: 'board name'
		"""
        api_endpoint = PyPin.API_HOST + self.api_verson +'/me/following/boards/'
        request_url = api_endpoint + '?access_token=' + self.accesstoken
        return PyPin.call(request_url, 'post', { 'board': board_id })

    def unfollow_board(self, board_id):
        """Unfollow a board
		parameters:
             name: 'board_id',
             description: 'board name'
		"""
        api_endpoint = PyPin.API_HOST + self.api_verson +'/me/following/boards/' + board_id
        request_url = api_endpoint + '?access_token=' + self.accesstoken
        return PyPin.call(request_url, 'delete')

    def get_pins(self):
        """Get all of authenticated users's pins"""
        api_endpoint = PyPin.API_HOST + self.api_verson +'/me/pins/'
        request_url = api_endpoint + '?access_token=' + self.accesstoken
        return PyPin.call(request_url)

    def get_boards(self):
        """Get all of authenticated users's boards"""
        api_endpoint = PyPin.API_HOST + self.api_verson +'/me/boards/'
        request_url = api_endpoint + '?access_token=' + self.accesstoken
        return PyPin.call(request_url, 'get')

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
