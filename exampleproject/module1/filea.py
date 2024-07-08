#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     filea
   Description :
   date：          2024/7/8
-------------------------------------------------
   Change Activity:
                   2024/7/8:
-------------------------------------------------
"""
import copy
from exampleproject import config


def func1():
    config_run = copy.deepcopy(config.BASE_CONFIG)
    print("func1")


def func2():
    config_run = copy.deepcopy(config.BASE_CONFIG)
    print("func2")
