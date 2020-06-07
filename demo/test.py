# -*- coding: utf-8 -*-
# @File   : test.py
# @license: Copyright(C) 2020 FNEP-Tech
# @Author : fox 
# @Date   : 2020/5/14
# @Desc   : 

# import hashlib

# authkey = "x59nsNpczdXE"
# key = 'test' + authkey
# key = key.encode(encoding='utf-8')
# key = hashlib.md5(key)
# key = key.hexdigest()

# def test2(func):
#     print('new 第一层')
#     def inner(*args,**kwargs):
#         print('new 第二层')
#         print(args,kwargs)
#         return func(args,kwargs)
#
#     return inner

# def test2(**kwargs):
#     print('new 第一层')
#     def inner(func):
#         print('new 第二层')
#         return func(2)
#
#     return inner


# def test(**kwargs):
#     print(kwargs)
#     print('第一层')
#
#     def inner(func):
#         print('第二层')
#
#         @test2
#         def wrap(*args, **kwargs):
#             print('第三层')
#             print('args', args)
#             print(type(args[0]))
#             print('kwargs', kwargs)
#             return func(*args, **kwargs)
#
#         return wrap
#
#     return inner

controller_list = {}

# def test(cls):
#     property_list = {}
#     print('类名',cls.__name__)
#     print('类',cls)
#     property_list[cls.__name__] = cls
#     for key,value in vars(cls).items():
#         print('属性',key,value)
#         property_list[key] = value
#     # controller_pool.append()
#     controller_list[cls.__name__] = property_list
#     print(controller_list)
#     return cls

# @test
# class C(object):
#     x = 1
#
#     def f(self, x):
#         print(x)


# if __name__ == '__main__':
#     x = C()
#     x.f(2)
