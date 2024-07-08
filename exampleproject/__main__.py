#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     __main__.py
   Description :
   date：          2024/7/8
-------------------------------------------------
   Change Activity:
                   2024/7/8:
-------------------------------------------------
"""
import sys
from exampleproject import config


def main():
    c = config.BASE_CONFIG
    print(f"{c=}")
    for i, v in enumerate(sys.path):
        print(f"{i=}, {v=}")


if __name__ == "__main__":
    main()
