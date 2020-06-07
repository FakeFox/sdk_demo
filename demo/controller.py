# -*- coding: utf-8 -*-
# @File   : controller.py
# @license: Copyright(C) 2020 FNEP-Tech
# @Author : fox 
# @Date   : 2020/5/13
# @Desc   : 

from cullinan.controller import get_api, post_api


class Controller(object):
    @post_api(url=r'/auth', service='TestService', body_params=['id', 'userid', 'avatar', 'name', 'phone'],
              get_request_body=True)
    def auth(self, service, body_params):
        print(body_params)
        service.authentication(body_params)
        # service.authentication(body_params['id'], body_params['userid'], body_params['avatar'], body_params['name'],
                               # body_params['phone'])
        return service.response


    @get_api(url=r'/test', query_params=['id'])
    def auth(self, query_params):
        print('dir',dir(self))
        print('type',type(self))
        self.TestService2.auth(query_params)
        return self.TestService2.response
