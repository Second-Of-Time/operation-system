# -*- coding: utf-8 -*-

from distutils.core import setup
import py2exe

setup(
    # console和windows分别代表控制台和图形界面，按需求选择
    #console = [{"script" : 'comtrade.py'}], 
    windows = [{"script":"login.py", "icon_resources": [(1, "logo.ico")]} ],
    name = 'comtrade',# 生成的exe文件名
    version = '1.0', 
    options={}, # 括号内填入的为项目所需的依赖库和会造成报错的文件
    data_files={})# 括号内输入的为项目所需的依赖文件
