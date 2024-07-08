#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_moduleB
   Description :
   date：          2024/7/8
-------------------------------------------------
   Change Activity:
                   2024/7/8:
-------------------------------------------------
"""

from .context import fileb


class TestModuleB():
    @classmethod
    def test_func3(cls):
        fileb.func3()

    @classmethod
    def test_func4(cls):
        fileb.func4()
