#!/usr/bin/env python

"""
功能：手动生成所有SKU的静态detail html文件
"""

import sys

sys.path.insert(0, '../')
sys.path.insert(0, '../meiduo_mall/apps')

import os

if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'meiduo_mall.settings.dev'

# 让django进行初始化设置
import django

django.setup()

from contents.crons import generate_static_index_html

if __name__ == '__main__':
    generate_static_index_html()
