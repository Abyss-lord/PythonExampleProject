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

from .context import filea, fileb


class TestModuleA():
    @classmethod
    def test_func1(cls):
        filea.func1()

    @classmethod
    def test_func2(cls):
        filea.func2()
