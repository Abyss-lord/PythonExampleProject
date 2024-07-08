#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     setup.py
   Description :
   date：          2024/7/8
-------------------------------------------------
   Change Activity:
                   2024/7/8:
-------------------------------------------------
"""

from setuptools import setup, find_packages

setup(
    name="example-project",
    version="1.0.0",
    description="An example project",
    author="pancxenxi",
    author_email="p_lord@163.com",
    packages=find_packages(exclude=('tests', 'docs'))
)
