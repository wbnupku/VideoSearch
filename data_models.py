# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
#
###############################################################################
"""
Models for data.

Authors: wangxiao05(wangxiao05@baidu.com)
Date:    2018/08/19 23:28:10
"""


import attr


@attr.s
class VideoData(object):

    rid = attr.ib(init=True, type=str)
    title = attr.ib(init=True, type=unicode)
    popularity = attr.ib(init=True, type=int)
    rsc_size = attr.ib(init=True, type=int, metadata={'doc': 'in MB'})

    def get_url(self):
        return "https://zhongzishenqi.cc/show/{}.html".format(self.rid)

