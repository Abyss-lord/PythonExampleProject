#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     utils
   Description :
   date：          2024/7/8
-------------------------------------------------
   Change Activity:
                   2024/7/8:
-------------------------------------------------
"""


class FileUtil(object):
    @staticmethod
    def read_file(file_path):
        print("read file_path:{}".format(file_path))

    @staticmethod
    def write_file(file_path, content):
        print("write file_path:{}".format(file_path))


class ParserUtil(object):
    @classmethod
    def parse_file(cls, file_path):
        print("parse file_path:{}".format(file_path))


class StringUtil(object):
    @classmethod
    def is_blank(cls, s: str) -> bool:
        return bool(s.strip())
