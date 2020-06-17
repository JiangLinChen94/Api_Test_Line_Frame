#!/usr/bin/env python
# encoding: utf-8
# @author: Alin
# @file: .py
# @time: 2020/6/13 11:03

import requests
from utils.config_utils import local_config


def get_access_token_api(grant_type, appid, secret):
    token_path = '/cgi-bin/token'
    api_url = local_config.host + token_path
    get_param_data = {
        'grant_type': grant_type,
        'appid': appid,
        'secret': secret
    }
    response_obj = requests.get(url=api_url,
                                params=get_param_data
                                )
    return response_obj


def get_access_token_value():
    response_obj = get_access_token_api('client_credential',
                                        'wxec83eaada223a9c8',
                                        '1867d7f1cabb3bafae0b7304e8251a09')
    return response_obj.json()['access_token']


def create_user_tag_api(token_id, tag_name):
    token_path = '/cgi-bin/tags/create'
    api_url = local_config.host + token_path
    get_param_data = {
        'access_token': token_id
    }
    header_info = {
        'Content-Type': 'application/json'
    }
    post_param_data = {"tag": {"name": tag_name}}
    response_obj = requests.post(url=api_url,
                                 params=get_param_data,
                                 headers=header_info,
                                 json=post_param_data
                                 )
    return response_obj
