import requests
import json

class PyPin:
    """Python client consume Pinterest API"""
    TIMEOUT = 5

    @staticmethod
    def call(url, method = 'get', params = []):
        """
        API call to Pinterest
            url: API endpoint with access token attached
            method:  HTTP method
            params: optional, supply necessary parameters
        """
        r = getattr(requests, method)(url, timeout=PyPin.TIMEOUT)
        if r.status_code == 200:
            return r.json()['data']
        else: # TODO: Add more specific error info for each status code
            raise RuntimeError('API request to Pinterest return with status code ' + str(r.status_code))

    def __init__(self, accesstoken):
        self.accesstoken = accesstoken

    def me(self):
        """Get the authenticated user's Pinterest account info"""
        apiEndpoint = 'https://api.pinterest.com/v1/me/'
        requestUrl = apiEndpoint + '?access_token=' + self.accesstoken
        return PyPin.call(requestUrl)

    def get_likes():
        """Get the pins that the authenticated user likes"""
        pass

    def get_followers():
        """Get the authenticated user's followers"""
        pass

    def get_followed_boards():
        """Get the boards that the authenticated user follows"""
        pass

    def get_followed_users():
        """Get the Pinterest users that the authenticated user follows"""
        pass

    def get_followed_interests():
        """Get the interests that the authenticated user follows"""
        pass

    def follow_user(username):
        """Follow a user"""
        pass

    def unfollow_user(username):
        """Unfollow a user"""
        pass

    def follow_board(boardId):
        """Follow a board"""
        pass

    def unfollow_board(boardId):
        """Unfollow a board"""
        pass

    def follow_interest(interestId):
        """Follow an interest"""
        pass

    def unfollow_interest(interestId):
        """Unfollow an interest"""
        pass

    def get_pins():
        """Get all of authenticated users's pins"""
        pass

    def get_boards():
        """Get all of authenticated users's boards"""
        pass

    def get_user(username):
        """Get the account info for a Pinterest user"""
        pass

    def create_pin(pinInfo):
        """Get the account info for a Pinterest user
        pinInfo structure:
             board: '<username>/<board_name>' OR '<board_id>',
             note: 'My note'
             link: 'https://www.google.com',
             image_url: 'http://marketingland.com/wp-content/ml-loads/2014/07/pinterest-logo-white-1920.png'
        """
        pass
