#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     errors
   Description :
   date：          2024/7/8
-------------------------------------------------
   Change Activity:
                   2024/7/8:
-------------------------------------------------
"""


class NotSupportError(Exception):
    def __init__(self):
        super(NotSupportError, self).__init__()
