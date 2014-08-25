#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import logging






class douban():
    def __init__(self, username, password):
        self.login_url = 'https://www.douban.com/j/app/login'
        self.channel_url = 'https://www.douban.com/j/app/radio/channels'
        self.api_url = 'https://www.douban.com/j/app/radio/people'
        self.app_name = 'radio_desktop_win'
        self.version = '100'
        self.username = username
        self.password = password
        self.expire = None
        self.token = None
        self.cookies = None



    def do_login(self):
        to_post = {'email': self.email, 'password': self.password, 'app_name': self.app_name, 'version': self.version}
        r = requests.post(self.login_url, params=to_post, headers={'Content-Type': 'application/x-www-form-urlencoded'})
        if r.json()['r'] == 0:
            self.username = r.json()['user_name']
            self.user_id = r.json()['user_id']
            self.expire = r.json()['expire']
            self.token = r.json()['token']
            print (r.cookies)
            self.cookies = r.cookies.get_dict()
            return True, None
        else:
            return False, r.json()['err']
