# -*- coding: utf-8 -*-

#!/usr/bin/env python
import requests
def main():
    def request_handler():
        url = ''
        requests.get(url, auth=MyAuth())
        

class MyAuth(requests.auth.AuthBase):
    def __call__(self, r):
        
        return r