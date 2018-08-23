import requests
from social_core.backends.oauth import BaseOAuth2

class TimeCrowd(BaseOAuth2):
    name = 'timecrowd'
    ACCESS_TOKEN_METHOD = 'POST'
    
    def authorization_url(self):
        return 'https://timecrowd.net/oauth/authorize'
    
    def access_token_url(self):
        return 'https://timecrowd.net/oauth/token'

    def get_user_id(self, details, response):
        return details['user_id'] 

    def get_user_details(self, response):
        url = 'https://timecrowd.net/api/v1/user'
        headers = {'authorization': 'Bearer ' + response['access_token']}
        resp = requests.get(url, headers=headers)
        userinfo = resp.json()
        return {'username': userinfo['email'].split('@', 1)[0],
                'email': userinfo['email'],
                'fullname': userinfo['nickname'],
                'user_id': userinfo['id']}

