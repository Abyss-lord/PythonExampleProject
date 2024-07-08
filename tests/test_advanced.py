#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_advanced
   Description :
   date：          2024/7/8
-------------------------------------------------
   Change Activity:
                   2024/7/8:
-------------------------------------------------
"""

from .context import filec, filed


class TestModuleB():
    @classmethod
    def test_func5(cls):
        filec.func5()

    @classmethod
    def test_func6(cls):
        filec.func6()
