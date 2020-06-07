# -*- coding: utf-8 -*-
# @File   : service.py
# @license: Copyright(C) 2020 FNEP-Tech
# @Author : fox 
# @Date   : 2020/5/13
# @Desc   : 

import hashlib
from cullinan.service import Service, service


@service
class TestService(Service):
    def authentication(self, request_data):
        authkey = "x59nsNpczdXE"
        key = request_data['id'] + authkey
        print(key)
        key = key.encode(encoding='utf-8')
        key = hashlib.md5(key)
        key = key.hexdigest()
        data = {
            'a': "userAssign",
            'id': request_data['id'],
            'userid': request_data['userid'],
            'name': request_data['name'],
            'avatar': request_data['avatar'],
            'key': key,
        }
        self.response.set_body(data)
        return self.response

@service
class TestService2(Service):
    def auth(self, request_data):
        data = request_data
        self.response.set_body(data)
        return self.response


