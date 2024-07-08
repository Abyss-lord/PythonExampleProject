#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     config
   Description :
   date：          2024/7/8
-------------------------------------------------
   Change Activity:
                   2024/7/8:
-------------------------------------------------
"""
import json

from exampleproject.component import StringUtil


def get_config():
    with open('conf/basic_config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
        return config


BASE_CONFIG = get_config()
